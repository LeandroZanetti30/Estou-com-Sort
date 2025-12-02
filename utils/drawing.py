import pygame
from constants import *

# Inicialização de fontes
pygame.init()
font_large = pygame.font.SysFont("Segoe UI", 36, bold=True)
font_medium = pygame.font.SysFont("Segoe UI", 24)
font_small = pygame.font.SysFont("Segoe UI", 18)
font_tiny = pygame.font.SysFont("Segoe UI", 14)

def draw_text(surface, text, pos, size="medium", center=False, color=FONT_COLOR, wrap_width=None):
    font_map = {
        "large": font_large,
        "medium": font_medium,
        "small": font_small,
        "tiny": font_tiny
    }
    font = font_map.get(size, font_medium)
    
    if wrap_width:
        words = text.split(' ')
        lines = []
        current_line = []
        
        for word in words:
            test_line = ' '.join(current_line + [word])
            if font.size(test_line)[0] <= wrap_width:
                current_line.append(word)
            else:
                lines.append(' '.join(current_line))
                current_line = [word]
        lines.append(' '.join(current_line))
        
        y_offset = 0
        for line in lines:
            render = font.render(line, True, color)
            rect = render.get_rect()
            if center:
                rect.center = (pos[0], pos[1] + y_offset)
            else:
                rect.topleft = (pos[0], pos[1] + y_offset)
            surface.blit(render, rect)
            y_offset += font.get_linesize()
    else:
        render = font.render(text, True, color)
        rect = render.get_rect()
        if center:
            rect.center = pos
        else:
            rect.topleft = pos
        surface.blit(render, rect)


def draw_bars(surface, arr, highlight=[], special_highlights={}, partition=None, explanation=""):
    # REMOVA esta linha que limpa a tela:
    # surface.fill(BACKGROUND_COLOR)
    
    # Em vez disso, crie uma superfície temporária para as barras
    bars_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    
    # Desenhar explicação atual (na superfície temporária)
    if explanation:
        pygame.draw.rect(bars_surface, WHITE, (50, 30, WIDTH-100, 80), border_radius=BORDER_RADIUS)
        pygame.draw.rect(bars_surface, BLACK, (50, 30, WIDTH-100, 80), 2, border_radius=BORDER_RADIUS)
        draw_text(bars_surface, explanation, (60, 40), size="small", wrap_width=WIDTH-120)
    
    if not arr:
        surface.blit(bars_surface, (0, 0))
        return
    
    bar_width = (WIDTH - 100) // len(arr)
    max_val = max(arr) if arr else 1
    base_y = HEIGHT - 150
    
    if partition:
        l, r = partition
        pygame.draw.rect(bars_surface, (230, 230, 250), 
                        (50 + l * bar_width, 130, (r - l + 1) * bar_width, base_y - 130), 
                        border_radius=5)
    
    for i, val in enumerate(arr):
        x = 50 + i * bar_width
        height = (val / max_val) * (base_y - 180) if max_val != 0 else 0
        y = base_y - height
        
        if i in special_highlights:
            color = special_highlights[i]
        elif i in highlight:
            color = HIGHLIGHT_COLOR
        else:
            color = BAR_COLOR
        
        pygame.draw.rect(bars_surface, color, (x + 2, y, bar_width - 4, height), border_radius=5)
        
        if bar_width > 30:
            draw_text(bars_surface, str(val), (x + bar_width//2, y - 25), size="tiny", center=True)
    
    # Desenha as barras na tela principal
    surface.blit(bars_surface, (0, 0))