import pygame
import random
from constants import *
from utils.drawing import draw_text
from utils.buttons import Button

def draw_input_screen(surface, input_text, error_message, back_button):
    surface.fill(BACKGROUND_COLOR)
    
    # Título
    draw_text(surface, "Entrada de Dados", (WIDTH//2, 80), "large", True)
    draw_text(surface, f"Digite números separados por espaço ({MIN_VECTOR_SIZE} a {MAX_VECTOR_SIZE} números)", 
             (WIDTH//2, 130), "small", True)
    
    # Campo de entrada
    pygame.draw.rect(surface, WHITE, (WIDTH//2 - 200, 180, 400, 50), border_radius=BORDER_RADIUS)
    pygame.draw.rect(surface, BLACK, (WIDTH//2 - 200, 180, 400, 50), 2, border_radius=BORDER_RADIUS)
    draw_text(surface, input_text if input_text else "Exemplo: 5 3 8 1 2", (WIDTH//2 - 190, 195), "medium")
    
    # Botão Confirmar
    confirm_button = Button("Confirmar", WIDTH//2 - 100, 250, 200, 50, lambda: None, (100, 149, 237))
    confirm_button.draw(surface)
    
    # Botão Voltar
    back_button.draw(surface)
    
    # Mensagem de erro
    if error_message:
        draw_text(surface, error_message, (WIDTH//2, 320), "small", True, (200, 0, 0))

def handle_input_screen_events(event, input_text, vector, switch_screen, back_button):
    error_message = ""
    running = True
    
    # Botão Confirmar
    confirm_button = Button("Confirmar", WIDTH//2 - 100, 250, 200, 50, lambda: None, (100, 149, 237))
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        if confirm_button.rect.collidepoint(event.pos):
            try:
                if not input_text.strip():
                    raise ValueError("Digite alguns números")
                    
                vector = [int(num) for num in input_text.strip().split()]
                
                if len(vector) < MIN_VECTOR_SIZE:
                    raise ValueError(f"Mínimo {MIN_VECTOR_SIZE} números")
                if len(vector) > MAX_VECTOR_SIZE:
                    raise ValueError(f"Máximo {MAX_VECTOR_SIZE} números")
                    
                switch_screen(ALGORITHM_SCREEN)
                
            except ValueError as e:
                error_message = f"Erro: {str(e)}"
                vector = []
        
        elif back_button.rect.collidepoint(event.pos):
            switch_screen(MENU_SCREEN)
    
    # Tratamento de teclado
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
            try:
                if not input_text.strip():
                    raise ValueError("Digite alguns números")
                    
                vector = [int(num) for num in input_text.strip().split()]
                
                if len(vector) < MIN_VECTOR_SIZE:
                    raise ValueError(f"Mínimo {MIN_VECTOR_SIZE} números")
                if len(vector) > MAX_VECTOR_SIZE:
                    raise ValueError(f"Máximo {MAX_VECTOR_SIZE} números")
                    
                switch_screen(ALGORITHM_SCREEN)
                
            except ValueError as e:
                error_message = f"Erro: {str(e)}"
                vector = []
        
        elif event.key == pygame.K_BACKSPACE:
            input_text = input_text[:-1]
        elif event.unicode.isdigit() or event.unicode.isspace():
            input_text += event.unicode
    
    return input_text, vector, error_message, running