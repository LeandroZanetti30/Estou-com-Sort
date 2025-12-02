import pygame
import sys
import time
import random
from constants import *
from utils.drawing import draw_text, draw_bars
from utils.buttons import Button
from screens.menu import create_menu_buttons, draw_menu_screen
from screens.input import handle_input_screen_events, draw_input_screen
from screens.algorithm import create_algorithm_buttons, draw_algorithm_screen
from screens.about import draw_about_screen
from screens.size_selection import handle_size_selection_events, draw_size_selection_screen
from screens.speed_selection import create_speed_selection_buttons, draw_speed_selection_screen
from screens.report import show_report, save_report
from algorithms import insertion_sort, selection_sort, bubble_sort, quick_sort, merge_sort, bucket_sort, smooth_sort

class SortingVisualizer:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Estou com Sort")
        
        self.current_screen = MENU_SCREEN
        self.input_text = ""
        self.vector = []
        self.sorting_speed = DEFAULT_SPEED
        self.paused = False
        self.step_mode = False
        self.current_explanation = ""
        self.sorting_active = False
        self.algorithm_name = ""
        self.error_message = ""
        self.sorting_generator = None
        self.sorting_done = False
        self.comparisons = 0
        self.swaps = 0
        
        # Initialize buttons
        self.back_button = Button("← Voltar", 20, 20, 120, 40, self.switch_screen_menu)
        self.menu_buttons = create_menu_buttons(self.switch_screen, self.quit_app)
        self.algorithm_buttons = create_algorithm_buttons(self.sort_with_timer)
        
        # Botão de pausa (visível apenas durante ordenação)
        self.pause_button = Button("⏸ Pausar", WIDTH - 180, HEIGHT - 70, 150, 40, self.toggle_pause)
        
        # Botão para selecionar velocidade (NO CANTO INFERIOR DIREITO)
        self.speed_button = Button(
            f"⚙ {self.sorting_speed}ms",  # Texto mais compacto
            WIDTH - 170,  # Canto direito (170px da borda direita)
            HEIGHT - 70,  # Canto inferior (70px da borda inferior)
            150,  # Largura
            40,   # Altura
            lambda: self.switch_screen(SPEED_SELECTION_SCREEN),
            (220, 220, 220)  # Cor cinza
        )
        
        # Botões de seleção de velocidade
        self.speed_buttons = []

    def switch_screen(self, screen_name):
        self.current_screen = screen_name
        self.sorting_active = False
        self.sorting_generator = None
        self.sorting_done = False
        self.comparisons = 0
        self.swaps = 0
        self.paused = False
        if screen_name != ALGORITHM_SCREEN:
            self.current_explanation = ""

    def switch_screen_menu(self):
        self.switch_screen(MENU_SCREEN)

    def quit_app(self):
        pygame.quit()
        sys.exit()

    def toggle_pause(self):
        """Alterna entre pausado e continuar"""
        self.paused = not self.paused
        self.pause_button.text = "▶ Continuar" if self.paused else "⏸ Pausar"

    def set_sorting_speed(self, new_speed):
        """Define a nova velocidade de ordenação e atualiza o botão"""
        self.sorting_speed = new_speed
        self.speed_button.text = f"⚙ {new_speed}ms"  # Texto atualizado
        self.switch_screen(ALGORITHM_SCREEN)

    def wait(self, delay=None):
        """Função de espera com suporte a pausa"""
        if delay is None:
            delay = self.sorting_speed
        
        if self.paused:
            # Loop de espera enquanto pausado
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.quit_app()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        self.toggle_pause()
                        if not self.paused:
                            waiting = False
                    self.pause_button.check_click(event)
                
                # Desenha o botão de pausa durante a espera
                self.pause_button.draw(self.screen)
                pygame.display.flip()
                pygame.time.delay(100)
        
        pygame.time.delay(delay)

    def update_explanation(self, text):
        self.current_explanation = text

    def update_counters(self, comparisons, swaps):
        self.comparisons = comparisons
        self.swaps = swaps

    def sort_with_timer(self, name, tempo, espaco, insitu, estavel):
        self.algorithm_name = name
        self.sorting_active = True
        self.sorting_done = False
        self.comparisons = 0
        self.swaps = 0
        self.paused = False  # Garante que não inicie pausado
        
        # SALVA UMA CÓPIA do vetor original ANTES de ordenar
        vetor_original = self.vector.copy()
        
        algorithm_map = {
            "Insertion Sort": insertion_sort,
            "Selection Sort": selection_sort,
            "Bubble Sort": bubble_sort,
            "Quick Sort": quick_sort,
            "Merge Sort": merge_sort,
            "Bucket Sort": bucket_sort,
            "Smooth Sort": smooth_sort
        }
        
        sort_func = algorithm_map.get(name)
        if not sort_func:
            return
        
        self.sorting_generator = sort_func(
            self.vector.copy(),  # Trabalha com uma cópia
            self.screen, 
            self.update_explanation, 
            self.wait,
            self.update_counters
        )
        
        self.sorting_start_time = time.time()
        self.vetor_original = vetor_original  # Guarda o original

    def show_report(self, name, tempo, espaco, insitu, estavel, vetor_original ,vetor_ordenado, exec_time):
        save_and_exit_btn = show_report(
            self.screen, name, tempo, espaco, insitu, estavel, 
            vetor_original, vetor_ordenado, exec_time, self.comparisons, self.swaps,
            self.switch_screen, save_report
        )
        
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_app()
                
                if save_and_exit_btn.check_click(event):
                    waiting = False
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    waiting = False
                    self.switch_screen(MENU_SCREEN)
            
            pygame.display.update()

    def run(self):
        clock = pygame.time.Clock()
        
        while True:
            # Draw current screen
            if self.current_screen == MENU_SCREEN:
                draw_menu_screen(self.screen, self.menu_buttons)
                
            elif self.current_screen == INPUT_SCREEN:
                # Desenha a tela de input (apenas com campo de texto e botão Confirmar)
                draw_input_screen(self.screen, self.input_text, self.error_message, self.back_button)
                
            elif self.current_screen == SIZE_SELECTION_SCREEN:
                size_buttons = [
                    Button("Confirmar", WIDTH//2 - 100, 280, 200, 50, lambda: None, (100, 149, 237)),
                    self.back_button
                ]
                draw_size_selection_screen(self.screen, self.input_text, self.error_message, size_buttons)
                
            elif self.current_screen == ALGORITHM_SCREEN:
                # PRIMEIRO: sempre limpa a tela
                self.screen.fill(BACKGROUND_COLOR)
                
                # SEGUNDO: se estiver ordenando, desenha as barras
                if self.sorting_active:
                    draw_bars(
                        self.screen, 
                        self.vector, 
                        explanation=self.current_explanation
                    )
                    
                    # TERCEIRO: desenha o botão de pause POR CIMA das barras
                    self.pause_button.draw(self.screen)
                    
                    # Executa a ordenação (se não estiver pausado)
                    if not self.paused and not self.sorting_done:
                        try:
                            self.vector = next(self.sorting_generator)
                        except StopIteration:
                            self.sorting_done = True
                            duration = time.time() - self.sorting_start_time
                            self.show_report(
                                self.algorithm_name,
                                "O(n + k)" if self.algorithm_name == "Bucket Sort" else
                                "O(n log n)" if self.algorithm_name in ["Quick Sort", "Merge Sort", "Smooth Sort"] else
                                "O(n²)",
                                "O(n + k)" if self.algorithm_name == "Bucket Sort" else
                                "O(n)" if self.algorithm_name == "Merge Sort" else
                                "O(log n)" if self.algorithm_name == "Quick Sort" else
                                "O(1)",
                                "Não" if self.algorithm_name in ["Merge Sort", "Bucket Sort"] else "Sim",
                                "Não" if self.algorithm_name in ["Selection Sort", "Quick Sort", "Smooth Sort"] else "Sim",
                                self.vetor_original,
                                self.vector,
                                duration
                            )
                else:
                    # Se NÃO está ordenando, mostra a tela normal
                    draw_algorithm_screen(
                        self.screen, self.vector, self.algorithm_buttons, 
                        self.back_button, self.sorting_active, self.sorting_speed,
                        self.comparisons, self.swaps, self.speed_button
                    )
                
            elif self.current_screen == SPEED_SELECTION_SCREEN:
                # Cria os botões de velocidade se necessário
                if not self.speed_buttons:
                    self.speed_buttons = create_speed_selection_buttons(
                        self.sorting_speed, 
                        self.set_sorting_speed
                    )
                
                draw_speed_selection_screen(
                    self.screen, 
                    self.sorting_speed, 
                    self.back_button, 
                    self.speed_buttons
                )
                
            elif self.current_screen == ABOUT_SCREEN:
                draw_about_screen(self.screen, self.back_button)
            
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_app()
                
                # Tecla espaço para pausar/continuar (somente durante ordenação)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    if self.sorting_active:
                        self.toggle_pause()
                
                if self.current_screen == MENU_SCREEN:
                    for btn in self.menu_buttons:
                        btn.check_click(event)
                    self.back_button.check_click(event)
                
                elif self.current_screen == INPUT_SCREEN:
                    self.input_text, self.vector, self.error_message, _ = handle_input_screen_events(
                        event, self.input_text, self.vector, self.switch_screen, self.back_button
                    )
                
                elif self.current_screen == SIZE_SELECTION_SCREEN:
                    size_buttons = [
                        Button("Confirmar", WIDTH//2 - 100, 280, 200, 50, lambda: None, (100, 149, 237)),
                        self.back_button
                    ]
                    self.input_text, self.error_message, should_continue = handle_size_selection_events(
                        event, self.input_text, self.switch_screen, 
                        lambda v: setattr(self, 'vector', v),
                        size_buttons
                    )
                    if not should_continue:
                        continue
                
                elif self.current_screen == ALGORITHM_SCREEN:
                    if self.back_button.check_click(event):
                        self.sorting_active = False
                        self.sorting_generator = None
                    
                    if not self.sorting_active:
                        for btn in self.algorithm_buttons:
                            btn.check_click(event)
                        self.speed_button.check_click(event)
                    
                    # Botão de pausa (só funciona durante ordenação)
                    if self.sorting_active:
                        self.pause_button.check_click(event)
                
                elif self.current_screen == SPEED_SELECTION_SCREEN:
                    self.back_button.check_click(event)
                    for btn in self.speed_buttons:
                        if btn.check_click(event):
                            # O callback do botão já chama set_sorting_speed
                            break
                
                elif self.current_screen == ABOUT_SCREEN:
                    self.back_button.check_click(event)
            
            pygame.display.update()
            clock.tick(60)

if __name__ == "__main__":
    app = SortingVisualizer()
    app.run()