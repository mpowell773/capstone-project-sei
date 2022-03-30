import pygame
from settings import *

class UI:
    def __init__(self):
       
       #general variables
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        #health setup
        self.heart_full = pygame.image.load(HEART_FULL)
        self.heart_full = pygame.transform.rotozoom(self.heart_full, 0, HEART_SIZE)
        self.heart_half = pygame.image.load(HEART_HALF)
        self.heart_half = pygame.transform.rotozoom(self.heart_half, 0, HEART_SIZE)
        self.heart_empty = pygame.image.load(HEART_EMPTY)
        self.heart_empty = pygame.transform.rotozoom(self.heart_empty, 0, HEART_SIZE)
        
        
        
    def heart_bar(self, health):
        #define three hearts
        self.heart_1 = self.heart_full
        self.heart_2 = self.heart_full
        self.heart_3 = self.heart_full

        if health == 6:
            self.heart_1 = self.heart_full
            self.heart_2 = self.heart_full
            self.heart_3 = self.heart_full
        elif health == 5:
            self.heart_1 = self.heart_full
            self.heart_2 = self.heart_full
            self.heart_3 = self.heart_half
        elif health == 4:
            self.heart_1 = self.heart_full
            self.heart_2 = self.heart_full
            self.heart_3 = self.heart_empty           
        elif health == 3:
            self.heart_1 = self.heart_full
            self.heart_2 = self.heart_half
            self.heart_3 = self.heart_empty
        elif health == 2:
            self.heart_1 = self.heart_full
            self.heart_2 = self.heart_empty
            self.heart_3 = self.heart_empty
        elif health == 1:
            self.heart_1 = self.heart_half
            self.heart_2 = self.heart_empty
            self.heart_3 = self.heart_empty
        else:
            self.heart_1 = self.heart_empty
            self.heart_2 = self.heart_empty
            self.heart_3 = self.heart_empty

        #render hearts (to change position of bar and spacing, go to settings)
        self.display_surface.blit(self.heart_1, (HEART_STARTING_POSITION,10))
        self.display_surface.blit(self.heart_2, (HEART_STARTING_POSITION + HEART_SPACING, 10))
        self.display_surface.blit(self.heart_3, (HEART_STARTING_POSITION + (HEART_SPACING * 2), 10))


    def display(self, player):
        self.heart_bar(player.health)