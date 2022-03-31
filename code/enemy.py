from re import X
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
        self.status = 'left'
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

        #i-frame timer
        self.vulnerable = True
        self.hit_time = None
        self.invincibility_duration = 450

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
        #invoke method to get distance and direction to player
        distance = self.get_player_distance_direction(player)[0]
        x_direction = self.get_player_distance_direction(player)[1][0]
        
        #store direction in variable to prepend to other states
        self.facing = 'left'

        #conditional to check whether player is to the left or right of enemy
        if x_direction < 0:
            self.facing ='left'
        else:
            self.facing ='right'

        #conditional logic to check enemy's distance from player. Change status of enemy if condition satisfied
        if distance <= self.attack_radius and self.can_attack:
            self.status = f'{self.facing}_attack'
        elif distance <= self.notice_radius:
            self.status = f'{self.facing}'
        else:
            self.status = f'{self.facing}_idle'

    def actions(self, player):
        if self.status == f'{self.facing}_attack':
            #set to false so enemy can't keep attacking
            self.can_attack = False
            #start attack_timer
            self.attack_time = pygame.time.get_ticks()
            print('attack')
        elif self.status == f'{self.facing}':
            #have enemy move towards player 
            #self.direction is inherited from the move function in entity, this is where the logic of moving the sprite lives
            #this line is just setting the direction the enemy must go
            self.direction = self.get_player_distance_direction(player)[1]
        else:
            #insurance line to make sure direction sets to 0
            self.direction = pygame.math.Vector2()

    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        #attack cooldown
        if not self.can_attack:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.can_attack = True

        #i-frame timer
        if not self.vulnerable:
            if current_time - self.hit_time >= self.invincibility_duration:
                self.vulnerable = True


    def get_damage(self, player, attack_type):
        if self.vulnerable:
            #update self.direction for hit_reaction
            self.direction = self.get_player_distance_direction(player)[1]
            #check to see if we're using our dagger
            if attack_type == 'dagger':
                #subtract hp by dagger damage
                self.health -= dagger['damage']
            else:
                pass
                #bow damage
            #start timer and make enemy invulnerable  
            self.hit_time = pygame.time.get_ticks()
            self.vulnerable = False

    def check_death(self):
        if self.health <= 0:
            self.kill()

    def hit_reaction(self):
        if not self.vulnerable:
            #enemy is pushed back in opposite direction during i-frame window
            self.direction *= -self.resistance

    def animate(self):
        animation = self.animations[self.status]
        #getting animation_speed from entity class
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)


    def update(self):
        self.hit_reaction()
        self.move(self.speed)
        self.animate()
        self.cooldowns()
        self.check_death()

    def enemy_update(self, player):
        self.get_status(player)
        self.actions(player)

