import pygame
from settings import *
from entity import Entity
from misc_functions import import_folder

class Enemy(Entity):
    def __init__(self, enemy_name, position, groups, obstacle_sprites):
        #general setup
        super().__init__(groups)
        self.sprite_type = 'enemy'

        #graphics and rect
        self.import_assets(enemy_name)
        #starting movement status of enemy
        self.status = 'idle'
        #inheriting frame_index from entity class
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(topleft = position)
        self.hitbox = self.rect.inflate(0, -10)

        #variable need for collision which is being inherited from entity class
        self.obstacle_sprites = obstacle_sprites

        #stats
        self.enemy_name = enemy_name
        #importing enemy data from settings and storing specific enemy due to name
        enemy_info = enemy_data[self.enemy_name]
        self.health = enemy_info['health']
        self.speed = enemy_info['speed']
        self.attack_damage = enemy_info['damage']
        self.resistance = enemy_info['resistance']
        self.attack_radius = enemy_info['attack_radius']
        self.notice_radius = enemy_info['notice_radius']
        self.attack_type = enemy_info['attack_type']

    def import_assets(self, name):
        #defining dict of different animations states
        self.animations = {'idle': [], 'move': [], 'attack': []}
        #variable to store flexible path to whatever asset
        main_path = f'../assets/graphics/organized_scaled_tile_set/entities/{name}/'
        #loop through different keys and fill out lists with graphics
        for animation in self.animations.keys():
            self.animations[animation] = import_folder(main_path + animation)
    
    def update(self):
        self.move(self.speed)

