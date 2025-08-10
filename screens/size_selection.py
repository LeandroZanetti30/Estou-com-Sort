import pygame
import random
from constants import *
from utils.drawing import draw_text
from utils.buttons import Button

def handle_size_selection_events(event, input_text, switch_screen, set_vector, buttons):
    error_message = ""
    running = True
    
    for btn in buttons:
        if btn.check_click(event):
            if btn.text == "Confirmar":
                try:
                    if not input_text.strip():
                        raise ValueError("Digite um tamanho válido")
                        
                    size = int(input_text)
                    if MIN_VECTOR_SIZE <= size <= MAX_VECTOR_SIZE:
                        set_vector(random.sample(range(1, 100), size))
                        switch_screen(ALGORITHM_SCREEN)
                        running = False
                    else:
                        error_message = f"Tamanho deve ser entre {MIN_VECTOR_SIZE} e {MAX_VECTOR_SIZE}"
                except ValueError:
                    error_message = "Digite um número válido"
            elif btn.text == "← Voltar":
                switch_screen(MENU_SCREEN)
                running = False
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
            try:
                if not input_text.strip():
                    raise ValueError("Digite um tamanho válido")
                    
                size = int(input_text)
                if MIN_VECTOR_SIZE <= size <= MAX_VECTOR_SIZE:
                    set_vector(random.sample(range(1, 100), size))
                    switch_screen(ALGORITHM_SCREEN)
                    running = False
                else:
                    error_message = f"Tamanho deve ser entre {MIN_VECTOR_SIZE} e {MAX_VECTOR_SIZE}"
            except ValueError:
                error_message = "Digite um número válido"
        elif event.key == pygame.K_BACKSPACE:
            input_text = input_text[:-1]
        elif event.unicode.isdigit():
            input_text += event.unicode
    
    return input_text, error_message, running

def draw_size_selection_screen(surface, input_text, error_message, buttons):
    surface.fill(BACKGROUND_COLOR)
    
    # Título
    draw_text(surface, "Tamanho do Vetor", (WIDTH//2, 100), "large", True)
    draw_text(surface, f"Digite um tamanho entre {MIN_VECTOR_SIZE} e {MAX_VECTOR_SIZE}:", (WIDTH//2, 150), "medium", True)
    
    # Campo de entrada
    pygame.draw.rect(surface, WHITE, (WIDTH//2 - 100, 200, 200, 50), border_radius=BORDER_RADIUS)
    pygame.draw.rect(surface, BLACK, (WIDTH//2 - 100, 200, 200, 50), 2, border_radius=BORDER_RADIUS)
    draw_text(surface, input_text if input_text else "", (WIDTH//2, 225), "medium", True)
    
    # Mensagem de erro
    if error_message:
        draw_text(surface, error_message, (WIDTH//2, 350), "small", True, (200, 0, 0))
    
    for btn in buttons:
        btn.draw(surface)