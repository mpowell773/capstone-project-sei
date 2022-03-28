import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        #need to inherit from sprite class via super
        super().__init__()

        #get image for tile and add rectangle to it
        self.image = pygame.image.load('../assets/Graphics/frames/elf_m_idle_anim_f0.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = position)