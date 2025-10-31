from utils.drawing import draw_bars
from constants import *

def smooth_sort(arr, screen, update_explanation, wait_func, update_counters):
    comparisons = 0
    swaps = 0
    
    def sift_down(arr, start, end):
        nonlocal comparisons, swaps
        
        root = start
        while 2 * root + 1 <= end:
            child = 2 * root + 1
            swap_index = root
            
            comparisons += 1
            update_explanation(f"Smooth Sort: Comparando {arr[swap_index]} com filho esquerdo {arr[child]}.")
            update_counters(comparisons, swaps)
            draw_bars(screen, arr, [swap_index, child])
            yield arr
            wait_func()
            
            if arr[swap_index] < arr[child]:
                swap_index = child
            
            if child + 1 <= end:
                comparisons += 1
                update_explanation(f"Smooth Sort: Comparando {arr[swap_index]} com filho direito {arr[child + 1]}.")
                update_counters(comparisons, swaps)
                draw_bars(screen, arr, [swap_index, child + 1])
                yield arr
                wait_func()
                
                if arr[swap_index] < arr[child + 1]:
                    swap_index = child + 1
            
            if swap_index == root:
                return
            
            swaps += 1
            update_explanation(f"Smooth Sort: Trocando {arr[root]} com {arr[swap_index]}.")
            arr[root], arr[swap_index] = arr[swap_index], arr[root]
            update_counters(comparisons, swaps)
            draw_bars(screen, arr, [root, swap_index])
            yield arr
            wait_func()
            
            root = swap_index

    update_explanation("Smooth Sort: Iniciando ordenação por heaps adaptativos.")
    update_counters(comparisons, swaps)
    draw_bars(screen, arr)
    yield arr
    wait_func()

    n = len(arr)
    
    # Construir heap máximo (para ordenação crescente)
    update_explanation("Smooth Sort: Construindo heap máximo.")
    update_counters(comparisons, swaps)
    draw_bars(screen, arr)
    yield arr
    wait_func()
    
    for start in range((n - 2) // 2, -1, -1):
        yield from sift_down(arr, start, n - 1)

    # Extrair elementos do heap
    update_explanation("Smooth Sort: Extraindo elementos do heap em ordem crescente.")
    update_counters(comparisons, swaps)
    draw_bars(screen, arr)
    yield arr
    wait_func()
    
    for end in range(n - 1, 0, -1):
        swaps += 1
        update_explanation(f"Smooth Sort: Movendo maior elemento {arr[0]} para posição {end}.")
        arr[0], arr[end] = arr[end], arr[0]
        update_counters(comparisons, swaps)
        draw_bars(screen, arr, [0, end])
        yield arr
        wait_func()
        
        yield from sift_down(arr, 0, end - 1)

    update_explanation(f"Smooth Sort: Ordenação concluída! Comparações: {comparisons}, Trocas: {swaps}")
    update_counters(comparisons, swaps)
    draw_bars(screen, arr)
    yield arr
    wait_func(1000)