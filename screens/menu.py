import pygame
from constants import *
from utils.drawing import draw_text
from utils.buttons import Button

def create_menu_buttons(switch_screen, quit_app):
    return [
        Button("Inserir Vetor", WIDTH//2-150, 350, 300, 50, 
              lambda: switch_screen(INPUT_SCREEN), (100, 149, 237)),
        Button("Gerar Aleatório", WIDTH//2-150, 420, 300, 50, 
              lambda: switch_screen(SIZE_SELECTION_SCREEN), (60, 179, 113)),
        Button("Sobre", WIDTH//2-150, 490, 140, 40, 
              lambda: switch_screen(ABOUT_SCREEN), (220, 220, 220)),
        Button("Sair", WIDTH//2+10, 490, 140, 40, 
              quit_app, (220, 220, 220))
    ]

def draw_menu_screen(surface, buttons):
    # Fundo gradiente
    for y in range(HEIGHT):
        color = (
            int(240 - y/HEIGHT*40),
            int(248 - y/HEIGHT*48),
            int(255 - y/HEIGHT*55)
        )
        pygame.draw.line(surface, color, (0, y), (WIDTH, y))
    
    # Título com efeito
    title_text = "Estou com Sort"
    for i, shadow in enumerate([(3,3), (2,2), (1,1)]):
        draw_text(surface, title_text, (WIDTH//2+shadow[0], 80+shadow[1]), "large", True, (30+i*20, 30+i*20, 30+i*20))
    draw_text(surface, title_text, (WIDTH//2, 80), "large", True, (70, 130, 180))
    
    # Subtítulo
    draw_text(surface, "Um Ambiente Interativo para o Ensino e Benchmarking de Algoritmos de Ordenação", 
             (WIDTH//2, 140), "medium", True, (100, 100, 100))
    
    # Ícones/ilustrações
    pygame.draw.rect(surface, (100, 200, 100), (WIDTH//2-150, 200, 300, 10))
    pygame.draw.rect(surface, (200, 100, 100), (WIDTH//2-150, 220, 200, 10))
    pygame.draw.rect(surface, (100, 100, 200), (WIDTH//2-150, 240, 250, 10))
    pygame.draw.rect(surface, (200, 200, 100), (WIDTH//2-150, 260, 180, 10))
    pygame.draw.rect(surface, (200, 100, 200), (WIDTH//2-150, 280, 300, 10))
    
    for btn in buttons:
        btn.draw(surface)