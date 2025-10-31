import pygame
from constants import *
from utils.drawing import draw_text, draw_bars
from utils.buttons import Button

def create_algorithm_buttons(sort_with_timer):
    return [
        Button("Insertion Sort", WIDTH//2-300, 150, 250, 40, 
              lambda: sort_with_timer("Insertion Sort", "O(n²)", "O(1)", "Sim", "Sim"), 
              (100, 149, 237)),
        Button("Selection Sort", WIDTH//2-300, 200, 250, 40, 
              lambda: sort_with_timer("Selection Sort", "O(n²)", "O(1)", "Sim", "Não"), 
              (60, 179, 113)),
        Button("Bubble Sort", WIDTH//2-300, 250, 250, 40, 
              lambda: sort_with_timer("Bubble Sort", "O(n²)", "O(1)", "Sim", "Sim"), 
              (70, 130, 180)),
        Button("Quick Sort", WIDTH//2-300, 300, 250, 40, 
              lambda: sort_with_timer("Quick Sort", "O(n log n)", "O(log n)", "Sim", "Não"), 
              (138, 43, 226)),
        Button("Merge Sort", WIDTH//2-300, 350, 250, 40, 
              lambda: sort_with_timer("Merge Sort", "O(n log n)", "O(n)", "Não", "Sim"), 
              (72, 209, 204)),
        Button("Bucket Sort", WIDTH//2-300, 400, 250, 40, 
              lambda: sort_with_timer("Bucket Sort", "O(n + k)", "O(n + k)", "Não", "Sim"), 
              (255, 165, 0)),
        Button("Smooth Sort", WIDTH//2-300, 450, 250, 40, 
              lambda: sort_with_timer("Smooth Sort", "O(n log n)", "O(1)", "Sim", "Não"), 
              (199, 21, 133)),  # Cor magenta/violeta
    ]

def draw_algorithm_screen(surface, vector, buttons, back_button, sorting_active, sorting_speed, comparisons=0, swaps=0):
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
        
    # Mostra contadores de comparações e trocas durante a ordenação
    if sorting_active:
        draw_text(surface, f"Comparações: {comparisons}", (WIDTH-550, 60))
        draw_text(surface, f"Trocas: {swaps}", (WIDTH-550, 90))