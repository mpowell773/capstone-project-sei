import pygame
from settings import *

class Arrow_Bundle(pygame.sprite.Sprite):
    def __init__(self, position, groups, player):
        super().__init__(groups)

        self.sprite_type = 'arrow_bundle'
        self.player = player

        #graphic of arrow bundle
        full_path = '../assets/graphics/organized_scaled_tile_set/weapons/arrow/up.png'
        self.image = pygame.image.load(full_path).convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, .6)
        self.rect = self.image.get_rect(center = position)
    
    def pickup(self):
        #conditionals to check ammo
        if self.player.ammo <= 15:
            self.player.ammo += 5
        else:
            self.player.ammo = 15
        #delete pickup
        self.kill()
        


