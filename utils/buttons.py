import pygame
from constants import *
from utils.drawing import draw_text

class Button:
    def __init__(self, text, x, y, w, h, callback, color=BUTTON_COLOR, hover_color=BUTTON_HOVER):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.callback = callback
        self.color = color
        self.hover_color = hover_color
        self.original_color = color
        self.clicked = False
    
    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        hover = self.rect.collidepoint(mouse_pos)
        
        color = self.hover_color if hover else self.color
        border_color = (min(color[0]+20, 255), min(color[1]+20, 255), min(color[2]+20, 255))
        
        if self.clicked:
            color = (max(color[0]-20, 0), max(color[1]-20, 0), max(color[2]-20, 0))
            border_color = color
        
        pygame.draw.rect(surface, color, self.rect, border_radius=BORDER_RADIUS)
        pygame.draw.rect(surface, border_color, self.rect, 2, border_radius=BORDER_RADIUS)
        
        text_pos = (self.rect.centerx, self.rect.centery - 1)
        draw_text(surface, self.text, text_pos, size="medium", center=True, color=(50, 50, 50))
        draw_text(surface, self.text, self.rect.center, size="medium", center=True)
        
        self.clicked = False
    
    def check_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.clicked = True
            self.callback()
            return True
        return False