from utils.drawing import draw_bars
from constants import *
import math

def bucket_sort(arr, screen, update_explanation, wait_func, update_counters):
    comparisons = 0
    swaps = 0
    
    if not arr:
        update_explanation("Bucket Sort: Vetor vazio. Nada para ordenar.")
        update_counters(comparisons, swaps)
        draw_bars(screen, arr)
        yield arr
        return
    
    update_explanation("Bucket Sort: Iniciando ordenação. Dividindo os elementos em baldes (buckets).")
    update_counters(comparisons, swaps)
    draw_bars(screen, arr)
    yield arr
    wait_func()
    
    # Encontrar valores mínimo e máximo
    min_val = min(arr)
    max_val = max(arr)
    
    update_explanation(f"Bucket Sort: Valor mínimo: {min_val}, Valor máximo: {max_val}. Calculando número de baldes.")
    update_counters(comparisons, swaps)
    draw_bars(screen, arr)
    yield arr
    wait_func()
    
    # Número de baldes - usando raiz quadrada do tamanho do array
    num_buckets = max(1, int(math.sqrt(len(arr))))
    bucket_range = (max_val - min_val + 1) / num_buckets
    
    update_explanation(f"Bucket Sort: Criando {num_buckets} baldes. Cada balde cobre intervalo de {bucket_range:.2f}.")
    update_counters(comparisons, swaps)
    draw_bars(screen, arr)
    yield arr
    wait_func()
    
    # Criar baldes
    buckets = [[] for _ in range(num_buckets)]
    
    # Distribuir elementos nos baldes
    for i, value in enumerate(arr):
        if bucket_range > 0:
            bucket_index = min(int((value - min_val) / bucket_range), num_buckets - 1)
        else:
            bucket_index = 0
            
        buckets[bucket_index].append(value)
        swaps += 1
        
        update_explanation(f"Bucket Sort: Elemento {value} adicionado ao balde {bucket_index+1}.")
        update_counters(comparisons, swaps)
        
        # Visualização dos baldes sendo preenchidos
        highlights = {}
        for b_idx, bucket in enumerate(buckets):
            if bucket:
                color_val = 100 + (b_idx * 155 // num_buckets)
                highlights[b_idx] = (color_val, color_val, 255)
        
        draw_bars(screen, arr, [i], highlights)
        yield arr
        wait_func()
    
    update_explanation(f"Bucket Sort: Distribuição concluída. Ordenando individualmente cada balde.")
    update_counters(comparisons, swaps)
    draw_bars(screen, arr)
    yield arr
    wait_func()
    
    # Ordenar cada balde e reconstruir o array
    sorted_index = 0
    
    for bucket_idx, bucket in enumerate(buckets):
        if bucket:
            update_explanation(f"Bucket Sort: Ordenando balde {bucket_idx+1} com {len(bucket)} elementos: {bucket}")
            update_counters(comparisons, swaps)
            
            # Visualizar o balde atual sendo processado
            highlights = {bucket_idx: (255, 200, 100)}
            draw_bars(screen, arr, [], highlights)
            yield arr
            wait_func()
            
            # Ordenar o balde (usando insertion sort para pequenos conjuntos)
            sorted_bucket = insertion_sort_bucket(bucket, screen, update_explanation, wait_func, 
                                                update_counters, comparisons, swaps, bucket_idx, len(buckets))
            
            for value in sorted_bucket:
                arr[sorted_index] = value
                swaps += 1
                sorted_index += 1
                
                update_explanation(f"Bucket Sort: Inserindo elemento {value} do balde {bucket_idx+1} na posição {sorted_index-1}.")
                update_counters(comparisons, swaps)
                draw_bars(screen, arr, [sorted_index-1], {bucket_idx: (255, 200, 100)})
                yield arr
                wait_func()
    
    update_explanation(f"Bucket Sort: Ordenação concluída! Comparações: {comparisons}, Trocas: {swaps}")
    update_counters(comparisons, swaps)
    draw_bars(screen, arr)
    yield arr
    wait_func(1000)

def insertion_sort_bucket(bucket, screen, update_explanation, wait_func, update_counters, 
                         parent_comparisons, parent_swaps, bucket_idx, total_buckets):
    """Função auxiliar para ordenar baldes individuais com Insertion Sort"""
    comparisons = parent_comparisons
    swaps = parent_swaps
    
    if len(bucket) <= 1:
        return bucket
    
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        
        comparisons += 1
        update_explanation(f"Bucket Sort (Balde {bucket_idx+1}): Comparando {key} com elementos do balde.")
        update_counters(comparisons, swaps)
        wait_func()
        
        while j >= 0 and bucket[j] > key:
            comparisons += 1
            bucket[j + 1] = bucket[j]
            swaps += 1
            j -= 1
            
            update_explanation(f"Bucket Sort (Balde {bucket_idx+1}): Movendo elementos dentro do balde.")
            update_counters(comparisons, swaps)
            wait_func()
        
        bucket[j + 1] = key
        swaps += 1
        
        update_explanation(f"Bucket Sort (Balde {bucket_idx+1}): Elemento {key} posicionado no balde.")
        update_counters(comparisons, swaps)
        wait_func()
    
    return bucket