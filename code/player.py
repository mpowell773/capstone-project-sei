import pygame
from settings import *
from misc_functions import import_folder

class Player(pygame.sprite.Sprite):
    def __init__(self, position, groups, obstacle_sprites):
        #need to inherit from sprite class via super
        super().__init__(groups)

        #get image for player and add rectangle to it
        self.image = pygame.image.load('../assets/graphics/scaled_images/scaled_cropped_lizard.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = position)
        #reducing rect and returning new variable so that player image can overlap with obstacles
        self.hitbox = self.rect.inflate(0, -50)


        #graphics setup
        self.import_player_assets()
        #player animation state
        self.status = 'right'
        self.frame_index = 0
        self.animation_speed = 0.1

        #movement variables
        self.direction = pygame.math.Vector2()
        self.speed = 5

        #attack variables
        self.attacking = False
        self.attack_cooldown = 450
        self.attack_time = None

        #need obstacle_sprites to check for collisions
        self.obstacle_sprites = obstacle_sprites

    def import_player_assets(self):
        #path to character images
        character_path = '../assets/graphics/organized_scaled_tile_set/entities/player'
        #different states of animation
        self.animations = {'left_idle' : [], 'right_idle' : [], 'left': [], 'right' : [], 'left_attack' : [], 'right_attack' : []}

        for animation in self.animations.keys():
            #importing files from our player folder into our animations dict
            self.animations[animation] = import_folder(character_path + '/' + animation)
            

    def input(self):
        #storing input from player in keys
        keys = pygame.key.get_pressed()
      
        #disable player input while attack happens
        if not self.attacking:
            #movement input
            if not self.attacking:
                if keys[pygame.K_UP]:
                    #move up
                    self.direction.y = -1
                elif keys[pygame.K_DOWN]:
                    #move down
                    self.direction.y = 1
                else:
                    #stand still
                    self.direction.y = 0

                if keys[pygame.K_RIGHT]:
                    #move right
                    self.direction.x = 1
                    self.status = 'right'
                elif keys[pygame.K_LEFT]:
                    #move left
                    self.direction.x = -1
                    self.status = 'left'
                else:
                    #stand still
                    self.direction.x = 0

            #attack input
            if keys[pygame.K_z]:
                #set to true so no more attacks happen
                self.attacking = True
                #creating a timer
                self.attack_time = pygame.time.get_ticks()
                print('attack')

            #bow input
            if keys[pygame.K_x]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                print('bow')

    def get_status(self):
        #idle and vertical move status status
        #if player is moving
        if self.direction.y != 0:
            self.status = self.status.replace('_idle', '')
        #if 0 on both axis, set to idle
        elif self.direction. x == 0 and self.direction.y == 0:
            #conditional to add idle only once
            if not 'idle' in self.status and not 'attack' in self.status:
                #this way of updating the status allows direction to not be overwritten
                self.status = self.status + '_idle'

        #attack status
        if self.attacking:
            #stop player movement
            self.direction.x = 0
            self.direction.y = 0
            if not 'attack' in self.status:
                if 'idle' in self.status:
                    #overwrite idle
                    self.status = self.status.replace('_idle','_attack')
                else:
                    self.status = self.status + '_attack'
        #switch back to idle after attack
        else:
            self.status = self.status.replace('_attack', '_idle')

    def move(self,speed):
        # does the vector have length?
        if self.direction.magnitude() != 0:
            #if so, set to one
            self.direction = self.direction.normalize()

        #apply movement to rect and also check for collisions
        self.hitbox.x += (self.direction.x * speed)
        self.collision('horizontal')
        self.hitbox.y += (self.direction.y * speed) 
        self.collision('vertical')
        self.rect.center = self.hitbox.center
    
    def collision(self, direction):
        if direction == 'horizontal':
            #check each sprite in obstacle sprite
            for sprite in self.obstacle_sprites:
                #if collision becomes true
                if sprite.hitbox.colliderect(self.hitbox):
                    #and if direction is to the right
                    if self.direction.x > 0:
                        #keep player sprite right side same as obstacle left side
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right

        #the following logic is the same as horizontal except applied to y axis
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom

    def cooldowns(self):
        #running infinite timer to compare attack/bow timers to it
        current_time = pygame.time.get_ticks()

        if self.attacking:
            #subtract total game time from when attack timer initiated
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False

    def animate(self):
        animation = self.animations[self.status]
        
        #loop over frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        #set image
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center= self.hitbox.center)
        
        
   
    def update(self):
        self.input()
        self.cooldowns()
        self.get_status()
        self.animate()
        self.move(self.speed)

