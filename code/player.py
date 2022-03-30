import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, position, groups, obstacle_sprites):
        #need to inherit from sprite class via super
        super().__init__(groups)

        #get image for player and add rectangle to it
        self.image = pygame.image.load('../assets/graphics/scaled_images/scaled_cropped_lizard.png').convert_alpha()
        
        self.rect = self.image.get_rect(topleft = position)
        print(self.rect)
     



        #reducing rect and returning new variable so that player image can overlap with obstacles
        self.hitbox = self.rect.inflate(0, -26)

        #movement variables
        self.direction = pygame.math.Vector2()
        self.speed = 5

        #need obstacle_sprites to check for collisions
        self.obstacle_sprites = obstacle_sprites

    def input(self):
        #storing input from player in keys
        keys = pygame.key.get_pressed()

        #movement input
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
        elif keys[pygame.K_LEFT]:
            #move left
            self.direction.x = -1
        else:
            #stand still
            self.direction.x = 0

        #attack input
        if keys[pygame.K_z]:
            print('attack')

        #bow input
        if keys[pygame.K_x]:
            print('bow')

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
	
    def update(self):
        self.input()
        self.move(self.speed)

