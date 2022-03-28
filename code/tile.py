import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, position, groups, sprite_type, surface = pygame.Surface((TILESIZE, TILESIZE))):
        #need to inherit from sprite class via super
        super().__init__(groups)

        #allows different sprites to be mapped through the tile class
        self.sprite_type = sprite_type

        #get image for tile and add rectangle to it
        self.image = surface
        self.rect = self.image.get_rect(topleft = position)

        #reducing rect so that player can overlap with obstacle
        self.hitbox = self.rect.inflate(0 , -6)