import pygame
from settings import *

class Pause:
    def __init__(self):

        #get display surface
        self.display_surface = pygame.display.get_surface()

    def display(self):
        self.display_surface.fill('black')