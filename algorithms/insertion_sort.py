from utils.drawing import draw_bars
from constants import *

def insertion_sort(arr, screen, update_explanation, wait_func, update_counters):
    comparisons = 0
    swaps = 0
    explanation = "Insertion Sort: Começando a ordenação."
    update_explanation(explanation)
    update_counters(comparisons, swaps)
    draw_bars(screen, arr, explanation=explanation)
    yield arr
    wait_func()
    
    for i in range(1, len(arr)):
        explanation = f"Analisando elemento {arr[i]} (posição {i})"
        update_explanation(explanation)
        update_counters(comparisons, swaps)
        draw_bars(screen, arr, [i], explanation=explanation)
        yield arr
        wait_func()
        
        key = arr[i]
        j = i - 1
        
        while j >= 0:
            comparisons += 1
            explanation = f"Comparando {arr[j]} (posição {j}) com {key}"
            update_explanation(explanation)
            update_counters(comparisons, swaps)
            draw_bars(screen, arr, [j, i], explanation=explanation)
            yield arr
            wait_func()
            
            if arr[j] > key:
                explanation = f"Movendo {arr[j]} para direita (posição {j+1})"
                update_explanation(explanation)
                arr[j + 1] = arr[j]
                swaps += 1
                update_counters(comparisons, swaps)
                draw_bars(screen, arr, [j, j+1], explanation=explanation)
                yield arr
                wait_func()
                j -= 1
            else:
                break
        
        if j + 1 != i:
            arr[j + 1] = key
            swaps += 1
            explanation = f"Elemento {key} inserido na posição {j+1}"
        else:
            explanation = f"Elemento {key} já está na posição correta"
        
        update_explanation(explanation)
        update_counters(comparisons, swaps)
        draw_bars(screen, arr, [j+1, i], explanation=explanation)
        yield arr
        wait_func()
    
    explanation = f"Ordenação concluída! Comparações: {comparisons}, Trocas: {swaps}"
    update_explanation(explanation)
    update_counters(comparisons, swaps)
    draw_bars(screen, arr, explanation=explanation)
    yield arr
    wait_func(1000)