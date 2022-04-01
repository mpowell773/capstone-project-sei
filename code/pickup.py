import pygame
from settings import *

class Arrow_Bundle(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)

        #graphic of arrow bundle
        full_path = '../assets/graphics/organized_scaled_tile_set/weapons/arrow/up.png'
        self.image = pygame.image.load(full_path).convert_alpha()
        # self.rect = self.image.get_rect(top)

    