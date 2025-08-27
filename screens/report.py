import pygame
import time
from constants import *
from utils.drawing import draw_text
from utils.buttons import Button

def gerar_explicacao(name):
    explicacoes = {
        "Insertion Sort": (
            "Insertion Sort (Ordenação por Inserção) é um algoritmo simples que constrói a sequência ordenada "
            "um item de cada vez. Ele é eficiente para conjuntos de dados pequenos ou quase ordenados. "
            "Funciona como muitas pessoas ordenam cartas em um jogo de baralho - pega cada elemento e "
            "insere na posição correta entre os elementos já ordenados."
            "Complexidade:"
            "- Pior caso: O(n²) - quando o vetor está em ordem inversa"
            "- Melhor caso: O(n) - quando o vetor já está ordenado"
            "- Caso médio: O(n²)"
            "Características:"
            "- Estável: mantém a ordem de elementos iguais"
            "- In-situ: requer apenas uma quantidade constante de espaço adicional"
            "- Adaptável: se beneficia de vetores parcialmente ordenados"
        ),
        "Selection Sort": (
            "Selection Sort (Ordenação por Seleção) divide o vetor em duas partes: uma sublista ordenada "
            "e uma sublista não ordenada. A cada iteração, ele encontra o menor elemento na sublista não "
            "ordenada e o troca com o primeiro elemento da sublista não ordenada.\n\n"
            "Complexidade:\n"
            "- Pior caso: O(n²)\n"
            "- Melhor caso: O(n²)\n"
            "- Caso médio: O(n²)\n\n"
            "Características:\n"
            "- Não é estável: pode alterar a ordem de elementos iguais\n"
            "- In-situ: requer apenas uma quantidade constante de espaço adicional\n"
            "- Poucas trocas: no máximo n trocas (útil quando trocas são custosas)"
        ),
        "Bubble Sort": (
            "Bubble Sort (Ordenação por Bolha) é um dos algoritmos mais simples. Ele percorre o vetor "
            "repetidamente, compara elementos adjacentes e os troca se estiverem na ordem errada. "
            "O nome vem da forma como os elementos maiores 'borbulham' para o final do vetor.\n\n"
            "Complexidade:\n"
            "- Pior caso: O(n²)\n"
            "- Melhor caso: O(n) - com flag de verificação\n"
            "- Caso médio: O(n²)\n\n"
            "Características:\n"
            "- Estável: mantém a ordem de elementos iguais\n"
            "- In-situ: requer apenas uma quantidade constante de espaço adicional\n"
            "- Simples de implementar, mas ineficiente para listas grandes"
        ),
        "Quick Sort": (
            "Quick Sort (Ordenação Rápida) é um algoritmo eficiente que usa a estratégia 'dividir para "
            "conquistar'. Ele escolhe um elemento como pivô e particiona o vetor em dois subvetores - "
            "elementos menores que o pivô e elementos maiores que o pivô - e então ordena os subvetores "
            "recursivamente.\n\n"
            "Complexidade:\n"
            "- Pior caso: O(n²) - raro com boas escolhas de pivô\n"
            "- Melhor caso: O(n log n)\n"
            "- Caso médio: O(n log n)\n\n"
            "Características:\n"
            "- Não é estável\n"
            "- In-situ: requer apenas espaço adicional O(log n) para recursão\n"
            "- Geralmente o mais rápido na prática para grandes conjuntos de dados"
        ),
        "Merge Sort": (
            "Merge Sort (Ordenação por Mistura) é um algoritmo eficiente que também usa 'dividir para "
            "conquistar'. Ele divide o vetor em duas metades, ordena cada metade recursivamente e depois "
            "combina (merge) as duas metades ordenadas.\n\n"
            "Complexidade:\n"
            "- Pior caso: O(n log n)\n"
            "- Melhor caso: O(n log n)\n"
            "- Caso médio: O(n log n)\n\n"
            "Características:\n"
            "- Estável: mantém a ordem de elementos iguais\n"
            "- Não é in-situ: requer espaço adicional O(n)\n"
            "- Excelente para ordenar listas encadeadas e arquivos grandes"
        ),
    }
    return explicacoes.get(name, "Explicação não disponível para este algoritmo.")

def show_report(surface, name, tempo, espaco, insitu, estavel, vetor_original, vetor_ordenado, exec_time, switch_screen, save_report_func):
    # Tela de fundo
    surface.fill(BACKGROUND_COLOR)
    pygame.draw.rect(surface, (70, 130, 180), (0, 0, WIDTH, 80))
    draw_text(surface, f"Relatório: {name}", (WIDTH//2, 40), size="large", center=True, color=WHITE)
    
    # Container principal
    pygame.draw.rect(surface, WHITE, (50, 100, WIDTH-100, HEIGHT-180), border_radius=BORDER_RADIUS)
    pygame.draw.rect(surface, BLACK, (50, 100, WIDTH-100, HEIGHT-180), 2, border_radius=BORDER_RADIUS)
    
    # Informações técnicas
    draw_text(surface, "Informações Técnicas:", (80, 120), size="medium")
    draw_text(surface, f"Tempo teórico: {tempo}", (80, 160))
    draw_text(surface, f"Espaço: {espaco}", (80, 190))
    draw_text(surface, f"In-situ: {insitu}", (80, 220))
    draw_text(surface, f"Estável: {estavel}", (80, 250))
    draw_text(surface, f"Tempo de execução: {exec_time:.4f} segundos", (80, 280))
    
    # Visualização do vetor_ordenado
    bar_width = (WIDTH - 500) // len(vetor_ordenado)
    max_val = max(vetor_ordenado) if vetor_ordenado else 1
    base_y = HEIGHT - 200
    
    for i, val in enumerate(vetor_ordenado):
        x = 450 + i * bar_width
        height = (val / max_val) * 200
        y = base_y - height
        pygame.draw.rect(surface, BAR_COLOR, (x + 2, y, bar_width - 4, height), border_radius=5)
        if bar_width > 30:
            draw_text(surface, str(val), (x + bar_width//2, y - 25), size="tiny", center=True)
    
    # Explicação
    pygame.draw.rect(surface, (240, 240, 240), (80, 320, WIDTH-160, HEIGHT-420), border_radius=BORDER_RADIUS)
    pygame.draw.rect(surface, (200, 200, 200), (80, 320, WIDTH-160, HEIGHT-420), 1, border_radius=BORDER_RADIUS)
    draw_text(surface, "Explicação do Algoritmo:", (100, 340), size="medium")
    draw_text(surface, gerar_explicacao(name), (100, 380), size="small", wrap_width=WIDTH-180)
    
    # Botão
    save_and_exit_btn = Button("Salvar e Voltar ao Menu", WIDTH//2 - 150, HEIGHT - 100, 300, 50, 
                             lambda: [save_report_func(name, tempo, espaco, insitu, estavel, vetor_original, vetor_ordenado, exec_time),
                                      switch_screen(MENU_SCREEN)],
                             (76, 175, 80))
    save_and_exit_btn.draw(surface)
    
    return save_and_exit_btn

def save_report(name, tempo, espaco, insitu, estavel, vetor_original, vetor_ordenado, exec_time):
    import sys
    from pathlib import Path
    
    try:
        if getattr(sys, 'frozen', False):
            script_dir = Path(sys.executable).parent
        else:
            script_dir = Path(__file__).parent
        
        filename = script_dir / "relatorio_ordenacao.txt"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"Algoritmo utilizado: {name}\n")
            f.write(f"Vetor original: {vetor_original}\n")
            f.write(f"Vetor ordenado: {vetor_ordenado}\n\n")
            f.write(f"Tempo teórico: {tempo}\n")
            f.write(f"Espaço: {espaco}\n")
            f.write(f"In-situ: {insitu}\n")
            f.write(f"Estável: {estavel}\n")
            f.write(f"Tempo de execução: {exec_time:.2f} segundos\n\n")
            f.write("Explicação do algoritmo:\n")
            f.write(gerar_explicacao(name) + "\n")
        
        return True
        
    except Exception as e:
        print(f"Erro ao salvar relatório: {e}")
        return False