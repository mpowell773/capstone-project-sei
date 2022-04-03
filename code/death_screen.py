import pygame
from settings import *

class Death_Screen:
    def __init__(self):

        #get display surface
        self.display_surface = pygame.display.get_surface()
    
    def run(self):

        self.display_surface.fill('black')