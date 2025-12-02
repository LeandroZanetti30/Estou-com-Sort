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

def draw_algorithm_screen(surface, vector, algorithm_buttons, back_button, 
                          sorting_active, sorting_speed, comparisons=0, swaps=0, speed_button=None):
    """Tela de escolha do algoritmo"""
    surface.fill(BACKGROUND_COLOR)
    
    # Título
    draw_text(surface, "Escolha o Algoritmo de Ordenação", (WIDTH//2, 80), "large", True)
    
    # Informações do vetor
    if vector:
        draw_text(surface, f"Vetor ({len(vector)} elementos):", (WIDTH//2, 120), "medium", True)
        draw_text(surface, " ".join(map(str, vector)), (WIDTH//2, 150), "small", True)
    
    # Velocidade configurada (no canto superior direito)
    draw_text(surface, f"Velocidade: {sorting_speed}ms", 
             (WIDTH - 170, 70), "small", False, (70, 130, 180))
    
    # Mostra contadores se estiver ordenando
    if sorting_active:
        draw_text(surface, f"Comparações: {comparisons}, Trocas: {swaps}", 
                 (WIDTH//2, 210), "small", True, (100, 100, 100))
    
    # Botão para alterar velocidade (canto inferior direito)
    if not sorting_active and speed_button:
        speed_button.draw(surface)
    
    # Botões dos algoritmos (mantidos no centro)
    for btn in algorithm_buttons:
        btn.draw(surface)
    
    # Botão de voltar (canto superior esquerdo)
    back_button.draw(surface)