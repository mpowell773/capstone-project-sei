import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, groups):
        #inherit __init__ from Sprite class
        super().__init__(groups)

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
        #update rect to be hitbox subtracting from the y to adjust for strange pixel height
        self.rect.center = (self.hitbox.center[0], self.hitbox.center[1] - 20)
    
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
