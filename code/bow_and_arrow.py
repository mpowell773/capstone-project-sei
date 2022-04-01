import pygame
from settings import *

class Bow_and_Arrow(pygame.sprite.Sprite):
    
    def __init__(self, player, groups):
        super().__init__(groups)
        self.player_direction = player.status.split('_')[0]
        print(self.player_direction)

       #graphic of bow
        full_path_bow = f'../assets/graphics/organized_scaled_tile_set/weapons/bow/{self.player_direction}.png'
        self.image = pygame.image.load(full_path_bow).convert_alpha()

        #graphic of arrow
        full_path_arrow = f'../assets/graphics/organized_scaled_tile_set/weapons/arrow/{self.player_direction}.png'
        self.arrow_image = pygame.image.load(full_path_arrow).convert_alpha()

        #placement of weapon
        #offsets due to weird hitbox
        weapon_horizontal_offset = 45
        weapon_vertical_offset = 75

        if  self.player_direction == 'right':
            #place weapon to from it's center left on the player's center right
            self.rect = self.image.get_rect(midleft = (player.rect.midright[0], player.rect.midright[1] + weapon_horizontal_offset ))
        elif self.player_direction == 'left':
            self.rect = self.image.get_rect(midright = (player.rect.midleft[0], player.rect.midleft[1] + weapon_horizontal_offset))
        elif self.player_direction == 'up':
            self.rect = self.image.get_rect(midbottom = (player.rect.midtop[0], player.rect.midtop[1] + weapon_vertical_offset))
        elif self.player_direction == 'down':
            self.rect = self.image.get_rect(midtop = (player.rect.midbottom[0], player.rect.midbottom[1]))


    def arrow(self):
        #get direction of player
        #splitting the _idle/attack off of status
        if self.player_direction == 'right':
            arrow_direction = pygame.math.Vector2(1,0)
        elif self.player_direction.status.split('_')[0] == 'left':
            arrow_direction = pygame.math.Vector2(-1,0)
        elif self.player_direction.status.split('_')[0] == 'down':
            arrow_direction = pygame.math.Vector2(0,1)
        else:
            arrow_direction = pygame.math.Vector2(0,-1)
        
        if arrow_direction.x:
            print('shoot horizontal')
        else: 
            print('shoot vertical')