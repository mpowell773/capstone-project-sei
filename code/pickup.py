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
        if self.player.ammo <= self.player.stats['max_ammo']:
            self.player.ammo += 5
            if self.player.ammo > self.player.stats['max_ammo']:
                self.player.ammo = self.player.stats['max_ammo']
        #delete pickup
        self.kill()

#potion pickup is essentially same code as arrow bundle
#opportunity for refactor here       
class Potion(pygame.sprite.Sprite):
    def __init__(self, position, groups, player):
        super().__init__(groups)

        self.sprite_type = 'potion'
        self.player = player

        #graphic of potion
        full_path = '../assets/graphics/organized_scaled_tile_set/pickups/potion.png'
        self.image = pygame.image.load(full_path).convert_alpha()
        self.rect = self.image.get_rect(center = position)
    
    def pickup(self):
        if self.player.health < self.player.stats['max_health']:
            self.player.health += 2
            if self.player.health > self.player.stats['max_health']:
                self.player.health = self.player.stats['max_health']
        #delete potion
        self.kill()
        