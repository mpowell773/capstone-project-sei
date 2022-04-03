import pygame
from settings import *

class Pause:
    def __init__(self):

        #get display surface
        self.display_surface = pygame.display.get_surface()

    def input(self):
        #store key presses in variable
        keys = pygame.key.get_pressed()

        #move up or down in menu
        if keys[pygame.K_UP]:
            pass
        elif keys[pygame.K_DOWN]:
            pass

        #select option in menu
        if keys[pygame.K_z]:
            pass
            
    def display(self):
       
        #draw pause menu background
        bg_rectangle = pygame.Rect(800, 50, 400, 550)
        #base rectangle
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rectangle)
        #rectangle border
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rectangle, 2)

