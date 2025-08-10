import pygame
from constants import *
from utils.drawing import draw_text

def draw_about_screen(surface, back_button):
    surface.fill(BACKGROUND_COLOR)
    
    # Título
    draw_text(surface, "Sobre o Visualizador de Ordenação", (WIDTH//2, 80), "large", True)
    
    # Container
    pygame.draw.rect(surface, WHITE, (100, 120, WIDTH-200, HEIGHT-240), border_radius=BORDER_RADIUS)
    pygame.draw.rect(surface, BLACK, (100, 120, WIDTH-200, HEIGHT-240), 2, border_radius=BORDER_RADIUS)
    
    # Conteúdo
    about_text = [
        "Este software foi desenvolvido como parte de um Trabalho de Conclusão de Curso (TCC)",
        "com o objetivo de ajudar estudantes de computação a entender algoritmos de ordenação.",
        "",
        "Funcionalidades:",
        "- Visualização passo a passo de 5 algoritmos de ordenação",
        "- Explicações detalhadas durante a execução",
        "- Comparação de complexidade e características",
        "- Interface interativa e intuitiva",
        "",
        "Desenvolvido por: Leandro Marcos Mendes Zanetti",
        "Orientador: [Nome do Orientador]",
        "Instituição: UFOP",
        "Ano: 2025"
    ]
    
    for i, line in enumerate(about_text):
        draw_text(surface, line, (120, 150 + i*30), "small")
    
    back_button.draw(surface)