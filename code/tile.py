import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        #need to inherit from sprite class via super
        super().__init__(groups)

        #get image for tile and add rectangle to it
        self.image = pygame.image.load('assets/graphics/frames/wall_mid.png')
        self.rect = self.image.get_rect(topleft = position)