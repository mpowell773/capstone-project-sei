import pygame, sys
from settings import *

class Death_Screen:
    def __init__(self, toggle_gameplay):

        #get display surface
        self.display_surface = pygame.display.get_surface()

        #method to return to dungeon instance
        self.toggle_gameplay = toggle_gameplay


    def input(self):
        #store key presses in variable
        keys = pygame.key.get_pressed()

        if keys[pygame.K_c]:
            pygame.quit()
            sys.exit()

    def run(self):

        self.display_surface.fill('black')
        self.input()