import pygame
from settings import *
from entity import Entity
from misc_functions import import_folder

class Enemy(Entity):
    def __init__(self, enemy_name, position, groups):
        #general setup
        super().__init__(groups)
        self.sprite_type = 'enemy'

        #graphics
        self.import_assets(enemy_name)
        #starting movement status of enemy
        self.status = 'idle'
        #inheriting frame_index from entity class
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(topleft = position)

    def import_assets(self, name):
        #defining dict of different animations states
        self.animations = {'idle': [], 'move': [], 'attack': []}
        #variable to store flexible path to whatever asset
        main_path = f'../assets/graphics/organized_scaled_tile_set/entities/{name}/'
        #loop through different keys and fill out lists with graphics
        for animation in self.animations.keys():
            self.animations[animation] = import_folder(main_path + animation)
    


