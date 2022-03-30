import pygame
from settings import *

class Dagger(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)

        #variables
        direction = player.direction_weapon
        
    
       #graphic of dagger
        full_path = f'../assets/graphics/organized_scaled_tile_set/weapons/dagger/{direction}.png'
        self.image = pygame.image.load(full_path).convert_alpha()

        #placement of weapon
        #offsets due to weird hitbox
        weapon_horizontal_offset = 45
        weapon_vertical_offset = 75

        if direction == 'right':
            #place weapon to from it's center left on the player's center right
            self.rect = self.image.get_rect(midleft = (player.rect.midright[0], player.rect.midright[1] + weapon_horizontal_offset ))
        elif direction == 'left':
            self.rect = self.image.get_rect(midright = (player.rect.midleft[0], player.rect.midleft[1] + weapon_horizontal_offset))
        elif direction == 'up':
            self.rect = self.image.get_rect(midbottom = (player.rect.midtop[0], player.rect.midtop[1] + weapon_vertical_offset))
        elif direction == 'down':
            self.rect = self.image.get_rect(midtop = (player.rect.midbottom[0], player.rect.midbottom[1]))