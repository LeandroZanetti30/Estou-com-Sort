from utils.drawing import draw_bars
from constants import *

def bubble_sort(arr, screen, update_explanation, wait_func, update_counters):
    comparisons = 0
    swaps = 0
    update_explanation("Bubble Sort: Começando a ordenação. Vamos comparar pares adjacentes e trocar se estiverem fora de ordem.")
    update_counters(comparisons, swaps)
    draw_bars(screen, arr)
    yield arr
    wait_func()
    
    n = len(arr)
    for i in range(n):
        update_explanation(f"Bubble Sort: Passagem {i+1}. Os maiores elementos vão 'flutuar' para o final.")
        update_counters(comparisons, swaps)
        draw_bars(screen, arr)
        yield arr
        wait_func()
        
        for j in range(0, n-i-1):
            comparisons += 1
            update_explanation(f"Bubble Sort: Comparando {arr[j]} (posição {j}) com {arr[j+1]} (posição {j+1}).")
            update_counters(comparisons, swaps)
            draw_bars(screen, arr, [j, j+1])
            yield arr
            wait_func()
            
            if arr[j] > arr[j+1]:
                swaps += 1
                update_explanation(f"Bubble Sort: Trocando {arr[j]} e {arr[j+1]} pois estão fora de ordem.")
                arr[j], arr[j+1] = arr[j+1], arr[j]
                update_counters(comparisons, swaps)
                draw_bars(screen, arr, [j, j+1])
                yield arr
                wait_func()
    
    update_explanation(f"Bubble Sort: Ordenação concluída! Comparações: {comparisons}, Trocas: {swaps}")
    update_counters(comparisons, swaps)
    draw_bars(screen, arr)
    yield arr
    wait_func(1000)