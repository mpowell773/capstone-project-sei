import pygame
from settings import *

class UI:
    def __init__(self):
       
       #general variables
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        #health setup
        self.heart_full = pygame.image.load(HEART_FULL)
        self.heart_full = pygame.transform.rotozoom(self.heart_full, 0, .75)
        self.heart_half = pygame.image.load(HEART_HALF)
        self.heart_half = pygame.transform.rotozoom(self.heart_half, 0, .75)
        self.heart_empty = pygame.image.load(HEART_EMPTY)
        self.heart_empty = pygame.transform.rotozoom(self.heart_empty, 0, .75)
        
        
        
    def heart_bar(self):
        #define three hearts
        self.heart_1 = self.heart_full
        self.heart_2 = self.heart_full
        self.heart_3 = self.heart_full

        self.display_surface.blit(self.heart_1, (15,10))
        self.display_surface.blit(self.heart_2, (60, 10))
        self.display_surface.blit(self.heart_3, (105, 10))

    def display(self, player):
        self.heart_bar()