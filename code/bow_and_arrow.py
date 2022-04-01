import pygame
from settings import *

class Bow_and_Arrow(pygame.sprite.Sprite):
    
    def __init__(self, player, groups):
        super().__init__(groups)
        #for the bow, only want left or right
        self.player_direction = player.status.split('_')[0]
        #for arrow, we need up, down, left, or right
        self.weapon_facing = player.direction_weapon

       #graphic of bow
        full_path_bow = f'../assets/graphics/organized_scaled_tile_set/weapons/bow/{self.player_direction}.png'
        self.image = pygame.image.load(full_path_bow).convert_alpha()

        #graphic of arrow
        full_path_arrow = f'../assets/graphics/organized_scaled_tile_set/weapons/arrow/{self.player_direction}.png'
        self.arrow_image = pygame.image.load(full_path_arrow).convert_alpha()

        #placement of bow

        if  self.player_direction == 'right':
            #place weapon to from it's center left on the player's center right
            self.rect = self.image.get_rect(midleft = (player.rect.midright + pygame.math.Vector2(-25,0)))
        elif self.player_direction == 'left':
            self.rect = self.image.get_rect(midright = (player.rect.midleft + pygame.math.Vector2(20,0)))



    def arrow(self):
        #get direction of player
        #splitting the _idle/attack off of status
        if self.weapon_facing == 'right':
            arrow_direction = pygame.math.Vector2(1,0)
        elif self.weapon_facing == 'left':
            arrow_direction = pygame.math.Vector2(-1,0)
        elif self.weapon_facing == 'down':
            arrow_direction = pygame.math.Vector2(0,1)
        else:
            arrow_direction = pygame.math.Vector2(0,-1)
        
        if arrow_direction.x:
            print('shoot horizontal')
        else: 
            print('shoot vertical')