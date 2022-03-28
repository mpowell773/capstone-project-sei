import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        #need to inherit from sprite class via super
        super().__init__(groups)

        #get image for tile and add rectangle to it
        self.image = pygame.image.load('../assets/graphics/scaled_images/wall_scaled.png')
        self.rect = self.image.get_rect(topleft = position)

        #reducing rect so that player can overlap with obstacle
        self.hitbox = self.rect.inflate(0 , -6)