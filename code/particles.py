import pygame
from misc_functions import import_folder

class AnimationPLayer:
    def __init__(self):
        #dict of all particle effects
        self.frames = {
            #attacks
            'claw' : import_folder('../assets/graphics/organized_scaled_tile_set/particles/claw'),
            'slash' : import_folder('../assets/graphics/organized_scaled_tile_set/particles/slash'),
            'slime_attack' : import_folder('../assets/graphics/organized_scaled_tile_set/particles/slime_attack'),
            'sparkle' : import_folder('../assets/graphics/organized_scaled_tile_set/particles/sparkle'),
            'thunder' : import_folder('../assets/graphics/organized_scaled_tile_set/particles/thunder'),

            #enemy deaths
            'grelmo' : import_folder('../assets/graphics/organized_scaled_tile_set/particles/nova'),
            'skoolie' : import_folder('../assets/graphics/organized_scaled_tile_set/particles/sparkle'),
            'slime' : import_folder('../assets/graphics/organized_scaled_tile_set/particles/slime_pool'),


            #crates
            'crate' : import_folder('../assets/graphics/organized_scaled_tile_set/particles/smoke2'),
        }
    

    


class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self, position, animation_frames, groups):
        super().__init__(groups)

        #animation variables
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.image.get_rect[self.frame_index]

    def animate(self):
        #quite similar to other animation functions except once the length of the animation if completed, destroy the sprite
        self.frame_index += self.animation_speed
        if self.frame >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self):
        self.animate()