import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        #need to inherit from sprite class via super
        super().__init__(groups)

        #get image for player and add rectangle to it
        self.image = pygame.image.load('../assets/graphics/frames/lizard_m_idle_anim_f1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = position)

        self.direction = pygame.math.Vector2()
        self.speed = 5

    def input(self):
        #storing input from player in keys
        keys = pygame.key.get_pressed()


        if keys[pygame.K_UP]:
            #move up
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            #move down
            self.direction.y = 1
        else:
            #stand still
            self.direction.y = 0

        if keys[pygame.K_LEFT]:
            #move left
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            #move right
            self.direction.x = 1
        else:
            #stand still
            self.direction.x = 0

    def update(self):
        self.input()
