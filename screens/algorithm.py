import pygame
from constants import *
from utils.drawing import draw_text, draw_bars
from utils.buttons import Button

def create_algorithm_buttons(sort_with_timer):
    return [
        Button("Insertion Sort", WIDTH//2-300, 180, 250, 45, 
              lambda: sort_with_timer("Insertion Sort", "O(n²)", "O(1)", "Sim", "Sim"), 
              (100, 149, 237)),
        Button("Selection Sort", WIDTH//2-300, 240, 250, 45, 
              lambda: sort_with_timer("Selection Sort", "O(n²)", "O(1)", "Sim", "Não"), 
              (60, 179, 113)),
        Button("Bubble Sort", WIDTH//2-300, 300, 250, 45, 
              lambda: sort_with_timer("Bubble Sort", "O(n²)", "O(1)", "Sim", "Sim"), 
              (70, 130, 180)),
        Button("Quick Sort", WIDTH//2-300, 360, 250, 45, 
              lambda: sort_with_timer("Quick Sort", "O(n log n)", "O(log n)", "Sim", "Não"), 
              (138, 43, 226)),
        Button("Merge Sort", WIDTH//2-300, 420, 250, 45, 
              lambda: sort_with_timer("Merge Sort", "O(n log n)", "O(n)", "Não", "Sim"), 
              (72, 209, 204)),
    ]

def draw_algorithm_screen(surface, vector, buttons, back_button, sorting_active, sorting_speed):
    surface.fill(BACKGROUND_COLOR)
    
    # Título
    draw_text(surface, "Escolha o Algoritmo de Ordenação", (WIDTH//2, 80), "large", True)
    
    # Mostra vetor atual
    if vector:
        draw_text(surface, "Vetor atual:", (WIDTH//2, 120), "medium", True)
        draw_text(surface, " ".join(map(str, vector)), (WIDTH//2, 150), "small", True)
    else:
        draw_text(surface, "Nenhum vetor definido!", (WIDTH//2, 130), "medium", True, (200, 0, 0))
    
    # Desenha botões dos algoritmos
    for btn in buttons:
        btn.draw(surface)
    
    back_button.draw(surface)
    
    # Botões de controle
    if sorting_active:
        draw_text(surface, f"Velocidade: {sorting_speed}ms", (WIDTH-550, 30))