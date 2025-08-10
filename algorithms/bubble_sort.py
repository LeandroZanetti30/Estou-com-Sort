from utils.drawing import draw_bars
from constants import *

def bubble_sort(arr, screen, update_explanation, wait_func):
    update_explanation("Bubble Sort: Começando a ordenação. Vamos comparar pares adjacentes e trocar se estiverem fora de ordem.")
    draw_bars(screen, arr)
    yield arr
    wait_func()
    
    n = len(arr)
    for i in range(n):
        update_explanation(f"Bubble Sort: Passagem {i+1}. Os maiores elementos vão 'flutuar' para o final.")
        draw_bars(screen, arr)
        yield arr
        wait_func()
        
        for j in range(0, n-i-1):
            update_explanation(f"Bubble Sort: Comparando {arr[j]} (posição {j}) com {arr[j+1]} (posição {j+1}).")
            draw_bars(screen, arr, [j, j+1])
            yield arr
            wait_func()
            
            if arr[j] > arr[j+1]:
                update_explanation(f"Bubble Sort: Trocando {arr[j]} e {arr[j+1]} pois estão fora de ordem.")
                arr[j], arr[j+1] = arr[j+1], arr[j]
                draw_bars(screen, arr, [j, j+1])
                yield arr
                wait_func()
    
    update_explanation("Bubble Sort: Ordenação concluída com sucesso!")
    draw_bars(screen, arr)
    yield arr
    wait_func(1000)