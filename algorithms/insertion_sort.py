from utils.drawing import draw_bars
from constants import *

def insertion_sort(arr, screen, update_explanation, wait_func):
    explanation = "Insertion Sort: Começando a ordenação."
    update_explanation(explanation)
    draw_bars(screen, arr, explanation=explanation)
    yield arr
    wait_func()
    
    for i in range(1, len(arr)):
        explanation = f"Analisando elemento {arr[i]} (posição {i})"
        update_explanation(explanation)
        draw_bars(screen, arr, [i], explanation=explanation)
        yield arr
        wait_func()
        
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            explanation = f"Movendo {arr[j]} para direita (posição {j+1})"
            update_explanation(explanation)
            arr[j + 1] = arr[j]
            draw_bars(screen, arr, [j, j+1], explanation=explanation)
            yield arr
            wait_func()
            j -= 1
        
        arr[j + 1] = key
        explanation = f"Elemento {key} inserido na posição {j+1}"
        update_explanation(explanation)
        draw_bars(screen, arr, [j+1, i], explanation=explanation)
        yield arr
        wait_func()
    
    explanation = "Ordenação concluída com sucesso!"
    update_explanation(explanation)
    draw_bars(screen, arr, explanation=explanation)
    yield arr
    wait_func(1000)