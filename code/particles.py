import pygame
from misc_functions import import_folder

class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self, position, animation_frames, groups):
        super().__init__(groups)

        #animation variables
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.image.get_rect[self.frame_index]
