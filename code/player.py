import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        #need to inherit from sprite class via super
        super().__init__(groups)

        #get image for tile and add rectangle to it
        self.image = pygame.image.load('../assets/graphics/frames/lizard_m_idle_anim_f1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = position)