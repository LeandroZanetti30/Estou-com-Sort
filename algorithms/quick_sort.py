from utils.drawing import draw_bars
from constants import *

def quick_sort(arr, screen, update_explanation, wait_func, update_counters):
    comparisons = 0
    swaps = 0
    
    def _quick_sort(arr, low, high):
        nonlocal comparisons, swaps
        
        if low < high:
            update_explanation(f"Quick Sort: Particionando o subvetor de {low} a {high}. Escolhendo pivô {arr[high]}.")
            update_counters(comparisons, swaps)
            draw_bars(screen, arr, [], {}, (low, high))
            yield arr
            wait_func()
            
            pi = yield from partition(arr, low, high)
            
            update_explanation(f"Quick Sort: Pivô {arr[pi]} colocado na posição correta {pi}. Agora ordenando os subvetores.")
            update_counters(comparisons, swaps)
            draw_bars(screen, arr, [pi], {pi: QUICK_COLOR})
            yield arr
            wait_func()
            
            yield from _quick_sort(arr, low, pi - 1)
            yield from _quick_sort(arr, pi + 1, high)
    
    def partition(arr, low, high):
        nonlocal comparisons, swaps
        
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            comparisons += 1
            update_explanation(f"Quick Sort: Comparando {arr[j]} com o pivô {pivot}.")
            update_counters(comparisons, swaps)
            draw_bars(screen, arr, [j, high], {high: QUICK_COLOR}, (low, high))
            yield arr
            wait_func()
            
            if arr[j] < pivot:
                i += 1
                if i != j:
                    swaps += 1
                    update_explanation(f"Quick Sort: Trocando {arr[i]} e {arr[j]} para colocar elementos menores que o pivô à esquerda.")
                    arr[i], arr[j] = arr[j], arr[i]
                    update_counters(comparisons, swaps)
                    draw_bars(screen, arr, [i, j], {high: QUICK_COLOR}, (low, high))
                    yield arr
                    wait_func()
        
        swaps += 1
        update_explanation(f"Quick Sort: Movendo o pivô {pivot} para sua posição final {i+1}.")
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        update_counters(comparisons, swaps)
        draw_bars(screen, arr, [i+1, high], {i+1: QUICK_COLOR}, (low, high))
        yield arr
        wait_func()
        
        return i + 1
    
    update_explanation("Quick Sort: Iniciando ordenação com o algoritmo Quick Sort (recursivo).")
    update_counters(comparisons, swaps)
    draw_bars(screen, arr)
    yield arr
    wait_func()
    
    yield from _quick_sort(arr, 0, len(arr) - 1)
    
    update_explanation(f"Quick Sort: Ordenação concluída! Comparações: {comparisons}, Trocas: {swaps}")
    update_counters(comparisons, swaps)
    draw_bars(screen, arr)
    yield arr
    wait_func(1000)