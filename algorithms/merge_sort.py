from utils.drawing import draw_bars
from constants import *

def merge_sort(arr, screen, update_explanation, wait_func, update_counters):
    comparisons = 0
    swaps = 0
    
    def _merge_sort(arr, l, r):
        nonlocal comparisons, swaps
        
        if l < r:
            m = (l + r) // 2
            update_explanation(f"Merge Sort: Dividindo o subvetor de {l} a {r} ao meio (índice {m}).")
            update_counters(comparisons, swaps)
            draw_bars(screen, arr, [], {}, (l, r))
            yield arr
            wait_func()
            
            yield from _merge_sort(arr, l, m)
            yield from _merge_sort(arr, m + 1, r)
            
            update_explanation(f"Merge Sort: Mesclando os subvetores ordenados de {l} a {m} e de {m+1} a {r}.")
            update_counters(comparisons, swaps)
            draw_bars(screen, arr, [], {}, (l, r))
            yield arr
            wait_func()
            
            yield from merge(arr, l, m, r)
    
    def merge(arr, l, m, r):
        nonlocal comparisons, swaps
        
        L = arr[l:m+1]
        R = arr[m+1:r+1]
        i = j = 0
        k = l
        
        while i < len(L) and j < len(R):
            comparisons += 1
            update_explanation(f"Merge Sort: Comparando {L[i]} (esquerda) com {R[j]} (direita).")
            update_counters(comparisons, swaps)
            highlights = {}
            if l + i <= m: highlights[l + i] = (100, 200, 100)
            if m + 1 + j <= r: highlights[m + 1 + j] = (200, 100, 100)
            draw_bars(screen, arr, [k], highlights, (l, r))
            yield arr
            wait_func()
            
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            
            swaps += 1
            update_explanation(f"Merge Sort: Copiando elemento {arr[k]} para posição {k}.")
            update_counters(comparisons, swaps)
            draw_bars(screen, arr, [k], highlights, (l, r))
            yield arr
            wait_func()
            k += 1
        
        while i < len(L):
            arr[k] = L[i]
            swaps += 1
            update_explanation(f"Merge Sort: Copiando elemento restante {L[i]} da esquerda para posição {k}.")
            update_counters(comparisons, swaps)
            draw_bars(screen, arr, [k], {l + i: (100, 200, 100)}, (l, r))
            yield arr
            wait_func()
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            swaps += 1
            update_explanation(f"Merge Sort: Copiando elemento restante {R[j]} da direita para posição {k}.")
            update_counters(comparisons, swaps)
            draw_bars(screen, arr, [k], {m + 1 + j: (200, 100, 100)}, (l, r))
            yield arr
            wait_func()
            j += 1
            k += 1
    
    update_explanation("Merge Sort: Iniciando ordenação com o algoritmo Merge Sort (dividir para conquistar).")
    update_counters(comparisons, swaps)
    draw_bars(screen, arr)
    yield arr
    wait_func()
    
    yield from _merge_sort(arr, 0, len(arr) - 1)
    
    update_explanation(f"Merge Sort: Ordenação concluída! Comparações: {comparisons}, Trocas: {swaps}")
    update_counters(comparisons, swaps)
    draw_bars(screen, arr)
    yield arr
    wait_func(1000)