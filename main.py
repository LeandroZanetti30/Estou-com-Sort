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
from screens.report import show_report, save_report
from algorithms import insertion_sort, selection_sort, bubble_sort, quick_sort, merge_sort

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
        
        # Initialize buttons
        self.back_button = Button("← Voltar", 20, 20, 120, 40, self.switch_screen_menu)
        self.menu_buttons = create_menu_buttons(self.switch_screen, self.quit_app)
        self.algorithm_buttons = create_algorithm_buttons(self.sort_with_timer)
        
        # Control buttons
        #self.pause_button = Button("⏸ Pausar", WIDTH-250, 20, 100, 40, self.toggle_pause)
        #self.step_button = Button("⏭ Passo", WIDTH-140, 20, 100, 40, self.do_step)

    def switch_screen(self, screen_name):
        self.current_screen = screen_name
        self.sorting_active = False
        self.sorting_generator = None
        if screen_name != ALGORITHM_SCREEN:
            self.current_explanation = ""

    def switch_screen_menu(self):
        self.switch_screen(MENU_SCREEN)

    def quit_app(self):
        pygame.quit()
        sys.exit()

    def toggle_pause(self):
        self.paused = not self.paused
        #self.pause_button.text = "▶ Continuar" if self.paused else "⏸ Pausar"

    def do_step(self):
        self.step_mode = True

    def wait(self, delay=None):
        if delay is None:
            delay = self.sorting_speed
        
        if self.paused or self.step_mode:
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.quit_app()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        self.toggle_pause()
                    if event.type == pygame.MOUSEBUTTONDOWN and self.step_mode:
                        waiting = False
                
                self.pause_button.draw(self.screen)
                self.step_button.draw(self.screen)
                pygame.display.flip()
                pygame.time.delay(100)
            
            self.step_mode = False
        
        pygame.time.delay(delay)

    def update_explanation(self, text):
        self.current_explanation = text

    def sort_with_timer(self, name, tempo, espaco, insitu, estavel):
        self.algorithm_name = name
        self.sorting_active = True
        self.sorting_done = False
        
        # SALVA UMA CÓPIA do vetor original ANTES de ordenar
        vetor_original = self.vector.copy()
        
        algorithm_map = {
            "Insertion Sort": insertion_sort,
            "Selection Sort": selection_sort,
            "Bubble Sort": bubble_sort,
            "Quick Sort": quick_sort,
            "Merge Sort": merge_sort
        }
        
        sort_func = algorithm_map.get(name)
        if not sort_func:
            return
        
        self.sorting_generator = sort_func(
            self.vector.copy(),  # Trabalha com uma cópia
            self.screen, 
            self.update_explanation, 
            self.wait
        )
        
        self.sorting_start_time = time.time()
        self.vetor_original = vetor_original  # Guarda o original

    def show_report(self, name, tempo, espaco, insitu, estavel, vetor_original ,vetor_ordenado, exec_time):
        save_and_exit_btn = show_report(
            self.screen, name, tempo, espaco, insitu, estavel, 
            vetor_original, vetor_ordenado, exec_time, self.switch_screen, save_report
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
                
                # Tratamento de eventos
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.quit_app()
                    
                    # Atualiza o input_text e verifica cliques
                    self.input_text, self.vector, self.error_message, _ = handle_input_screen_events(
                        event,  # Passa o evento individual
                        self.input_text, 
                        self.vector, 
                        self.switch_screen, 
                        self.back_button
                    )
                
            elif self.current_screen == SIZE_SELECTION_SCREEN:
                size_buttons = [
                    Button("Confirmar", WIDTH//2 - 100, 280, 200, 50, lambda: None, (100, 149, 237)),
                    self.back_button
                ]
                draw_size_selection_screen(self.screen, self.input_text, self.error_message, size_buttons)
                
            elif self.current_screen == ALGORITHM_SCREEN:
                draw_algorithm_screen(
                    self.screen, self.vector, self.algorithm_buttons, 
                    self.back_button, self.sorting_active, self.sorting_speed
                )
                
                # Draw control buttons if sorting is active
                #if self.sorting_active:
                #    self.pause_button.draw(self.screen)
                #    self.step_button.draw(self.screen)
                
                # Execute sorting step by step
# Dentro do método run(), onde executa o algoritmo:
                if self.sorting_active and not self.sorting_done and not self.paused:
                    try:
                        self.vector = next(self.sorting_generator)
                        draw_bars(
                            self.screen, 
                            self.vector, 
                            explanation=self.current_explanation
                        )
                    except StopIteration:
                        self.sorting_done = True
                        duration = time.time() - self.sorting_start_time
                        self.show_report(
                            self.algorithm_name,
                            "O(n²)" if self.algorithm_name in ["Insertion Sort", "Selection Sort", "Bubble Sort"] else "O(n log n)",
                            "O(1)" if self.algorithm_name != "Merge Sort" else "O(n)",
                            "Não" if self.algorithm_name == "Merge Sort" else "Sim",
                            "Não" if self.algorithm_name in ["Selection Sort", "Quick Sort"] else "Sim",
                            self.vetor_original,  # Original
                            self.vector,          # Ordenado,          # Ordenado
                            duration
                        )
                
            elif self.current_screen == ABOUT_SCREEN:
                draw_about_screen(self.screen, self.back_button)
            
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_app()
                
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.toggle_pause()
                
                if self.current_screen == MENU_SCREEN:
                    for btn in self.menu_buttons:
                        btn.check_click(event)
                
                elif self.current_screen == INPUT_SCREEN:
                    self.input_text, self.vector, self.error_message, _ = handle_input_screen_events(
                        event, self.input_text, self.vector, self.switch_screen, [
                            Button("Confirmar", WIDTH//2 - 150, 300, 300, 50, lambda: None, (100, 149, 237)),
                            Button("Gerar Aleatório", WIDTH//2 - 150, 370, 300, 50, lambda: None, (60, 179, 113)),
                            self.back_button
                        ]
                    )
                
                elif self.current_screen == SIZE_SELECTION_SCREEN:
                    self.input_text, self.error_message, should_continue = handle_size_selection_events(
                        event, self.input_text, self.switch_screen, 
                        lambda v: setattr(self, 'vector', v),
                        [
                            Button("Confirmar", WIDTH//2 - 100, 280, 200, 50, lambda: None, (100, 149, 237)),
                            self.back_button
                        ]
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
                    
                    #if self.sorting_active:
                    #    self.pause_button.check_click(event)
                    #    self.step_button.check_click(event)
                
                elif self.current_screen == ABOUT_SCREEN:
                    self.back_button.check_click(event)
            
            pygame.display.update()
            clock.tick(60)

if __name__ == "__main__":
    app = SortingVisualizer()
    app.run()