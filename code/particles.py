import pygame
from misc_functions import import_folder

class AnimationPlayer:
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
    
    def create_smoke(self, position, groups):
        #get specific frames from crate
        animation_frames = self.frames['crate']
        #pass these variables into Particle Effect class
        #additionally placing smoke a bit lower due to height of crate
        ParticleEffect((position[0], position[1] + 25), animation_frames, groups)




class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self, position, animation_frames, groups):
        super().__init__(groups)

        #animation variables
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center = position)
        #moving all particle effects down 20 pixels
        

    def animate(self):
        #quite similar to other animation functions except once the length of the animation if completed, destroy the sprite
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self):
        self.animate()