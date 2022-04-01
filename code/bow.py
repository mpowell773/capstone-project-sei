import pygame
from settings import *

class Bow:
    def __init__(self, animation_player):
        self.animation_player = animation_player

    def arrow(self, player, groups):
        #get direction of player
        #splitting the _idle/attack off of status
        if player.status.split('_')[0] == 'right':
            direction = pygame.math.Vector2(1,0)
        elif player.status.split('_')[0] == 'left':
            direction = pygame.math.Vector2(-1,0)
        elif player.status.split('_')[0] == 'down':
            direction = pygame.math.Vector2(0,1)
        else:
            direction = pygame.math.Vector2(0,-1)
        
