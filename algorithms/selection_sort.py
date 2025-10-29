from utils.drawing import draw_bars
from constants import *

def selection_sort(arr, screen, update_explanation, wait_func, update_counters):
    comparisons = 0
    swaps = 0
    update_explanation("Selection Sort: Começando a ordenação. Vamos selecionar o menor elemento a cada iteração.")
    update_counters(comparisons, swaps)
    draw_bars(screen, arr)
    yield arr
    wait_func()
    
    for i in range(len(arr)):
        update_explanation(f"Selection Sort: Procurando o menor elemento a partir da posição {i}.")
        update_counters(comparisons, swaps)
        min_idx = i
        draw_bars(screen, arr, [i])
        yield arr
        wait_func()
        
        for j in range(i+1, len(arr)):
            comparisons += 1
            update_explanation(f"Selection Sort: Comparando {arr[j]} com o atual menor {arr[min_idx]}.")
            update_counters(comparisons, swaps)
            draw_bars(screen, arr, [i, j, min_idx])
            yield arr
            wait_func()
            
            if arr[j] < arr[min_idx]:
                min_idx = j
                update_explanation(f"Selection Sort: Novo menor encontrado: {arr[j]} na posição {j}.")
                update_counters(comparisons, swaps)
                draw_bars(screen, arr, [i, j])
                yield arr
                wait_func()
        
        if min_idx != i:
            swaps += 1
            update_explanation(f"Selection Sort: Trocando {arr[i]} (posição {i}) com {arr[min_idx]} (posição {min_idx}).")
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            update_counters(comparisons, swaps)
            draw_bars(screen, arr, [i, min_idx])
            yield arr
            wait_func()
    
    update_explanation(f"Selection Sort: Ordenação concluída! Comparações: {comparisons}, Trocas: {swaps}")
    update_counters(comparisons, swaps)
    draw_bars(screen, arr)
    yield arr
    wait_func(1000)