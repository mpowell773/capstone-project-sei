import pygame

#class that displays sprites of current room and also handles their interactions
class Room:
    def __init__(self):

        #sprite group settings
        self.visible_sprites = pygame.sprite.Group
        self.obstacle_sprites = pygame.sprite.Group