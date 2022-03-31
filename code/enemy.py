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

        #player interaction
        self.can_attack = True
        self.attack_time = None
        self.attack_cooldown = 1000

    def import_assets(self, name):
        #defining dict of different animations states
        self.animations = {'left_idle' : [], 'right_idle' : [], 'left': [], 'right' : [], 'left_attack' : [], 'right_attack' : []}
        #variable to store flexible path to whatever asset
        main_path = f'../assets/graphics/organized_scaled_tile_set/entities/{name}/'
        #loop through different keys and fill out lists with graphics
        for animation in self.animations.keys():
            self.animations[animation] = import_folder(main_path + animation)
    
    def get_player_distance_direction(self,player):
        #declaring variables to hold vector of enemy position and player player
        enemy_vector = pygame.math.Vector2(self.rect.center)
        player_vector = pygame.math.Vector2(player.rect.center)

        #vector.magnitude converts vector into distance
        distance = (player_vector - enemy_vector).magnitude()

        #vector.normalize  reduces length of vector to 1
        #speed then can be easily multipled into it and not give strange results
        if distance > 0:
            direction = (player_vector - enemy_vector).normalize()
        #if player and enemy in same position, give empty vector
        else:
            direction = pygame.math.Vector2()

        return (distance, direction)

    def get_status(self, player):
        #invoke method to get distance to player
        distance = self.get_player_distance_direction(player)[0]

        #conditional logic to check enemy's distance from player. Change status of enemy if condition satisfied
        if distance <= self.attack_radius and self.can_attack:
            #conditional to make sure frame is at 0 cooldown is not attack
            if self.status != 'attack':
                self.frame_index = 0
            self.status = 'attack'
        elif distance <= self.notice_radius:
            self.status = 'move'
        else:
            self.status = 'idle'

    def actions(self, player):
        if self.status == 'attack':
            #set to false so enemy can't keep attacking
            self.can_attack = False
            #start attack_timer
            self.attack_time = pygame.time.get_ticks()
            print('attack')
        elif self.status == 'move':
            self.direction = self.get_player_distance_direction(player)[1]
            print(self.direction)
        else:
            #insurance line to make sure direction sets to 0
            self.direction = pygame.math.Vector2()

    def cooldowns(self):
        if not self.can_attack:
            current_time = pygame.time.get_ticks()

            #attack cooldown
            if current_time - self.attack_time >= self.attack_cooldown:
                self.can_attack = True

    def animate(self):
        animation = self.animations[self.status]
        #getting animation_speed from entity class
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)


    def update(self):
        self.move(self.speed)
        self.animate()
        self.cooldowns()

    def enemy_update(self, player):
        self.get_status(player)
        self.actions(player)

