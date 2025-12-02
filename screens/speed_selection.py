import pygame
from constants import *
from utils.buttons import Button
from utils.drawing import draw_text

def create_speed_selection_buttons(current_speed, set_speed_callback):
    """Cria os botões para selecionar velocidade"""
    speeds = [
        ("Muito Rápido", 100),
        ("Rápido", 300),
        ("Normal", 1100),
        ("Lento", 1500),
        ("Muito Lento", 2000)
    ]
    
    buttons = []
    for i, (label, speed) in enumerate(speeds):
        # Destaque a velocidade atual
        is_current = (current_speed == speed)
        color = (70, 130, 180) if is_current else (100, 149, 237)
        
        btn = Button(
            f"{label} ({speed}ms)", 
            WIDTH//2 - 150, 
            200 + i * 60, 
            300, 
            50, 
            lambda s=speed: set_speed_callback(s),
            color
        )
        buttons.append(btn)
    
    return buttons

def draw_speed_selection_screen(surface, current_speed, back_button, speed_buttons):
    """Desenha a tela de seleção de velocidade"""
    surface.fill(BACKGROUND_COLOR)
    
    # Título
    draw_text(surface, "Selecionar Velocidade", (WIDTH//2, 80), "large", True)
    draw_text(surface, "Escolha a velocidade para visualização:", (WIDTH//2, 130), "medium", True)
    
    # Velocidade atual
    draw_text(surface, f"Velocidade atual: {current_speed}ms", 
             (WIDTH//2, 170), "small", True, (100, 100, 100))
    
    # Botões de velocidade (centralizados)
    for btn in speed_buttons:
        btn.draw(surface)
    
    # Botão de voltar (canto superior esquerdo)
    back_button.draw(surface)