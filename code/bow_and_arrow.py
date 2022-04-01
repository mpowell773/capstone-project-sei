import pygame
from settings import *

class Bow(pygame.sprite.Sprite):
    
    def __init__(self, player, groups):
        super().__init__(groups)
        #for the bow, only want left or right
        self.player = player
        self.class_groups = groups
        self.player_direction = player.status.split('_')[0]
        #for arrow, we need up, down, left, or right
        self.weapon_facing = player.direction_weapon


       #graphic of bow
        full_path_bow = f'../assets/graphics/organized_scaled_tile_set/weapons/bow/{self.player_direction}.png'
        self.image = pygame.image.load(full_path_bow).convert_alpha()
        #make bow smaller
        self.image = pygame.transform.rotozoom(self.image, 0, 0.75)

        #placement of bow
        if  self.player_direction == 'right':
            #place weapon to from it's center left on the player's center right
            #using a vector to adjust bow's position on player sprite
            self.rect = self.image.get_rect(midleft = (player.rect.midright + pygame.math.Vector2(-25, 35)))
        elif self.player_direction == 'left':
            self.rect = self.image.get_rect(midright = (player.rect.midleft + 
            pygame.math.Vector2(25, 35)))
        
        



    def shoot_arrow(self):
        #get direction of player
        if self.weapon_facing == 'right':
            arrow_direction = pygame.math.Vector2(1,0).normalize()
        elif self.weapon_facing == 'left':
            arrow_direction = pygame.math.Vector2(-1,0).normalize()
        elif self.weapon_facing == 'down':
            arrow_direction = pygame.math.Vector2(0,1).normalize()
        else:
            arrow_direction = pygame.math.Vector2(0,-1).normalize()
        
        #spawn and move arrow
        if arrow_direction.x:
            spawned_arrow = Arrow(self.player, self.class_groups)
            spawned_arrow.rect.center += arrow_direction * bow['speed']
            print(spawned_arrow.rect.center)
        else: 
            Arrow(self.player, self.class_groups)
    
    def update(self):
        self.shoot_arrow()

class Arrow(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)
        #for arrow, we need up, down, left, or right
        self.weapon_facing = player.direction_weapon
        print(self.weapon_facing)

        #graphic of arrow
        full_path_arrow = f'../assets/graphics/organized_scaled_tile_set/weapons/arrow/{self.weapon_facing}.png'
        self.image = pygame.image.load(full_path_arrow).convert_alpha()
        self.rect = self.image.get_rect(center = player.rect.center + pygame.math.Vector2(0, 35))
    


