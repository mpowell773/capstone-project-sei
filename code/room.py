import pygame

#class that displays sprites of current room and also handles their interactions
class Room:
    def __init__(self):

        #get display surface
        self.display_surf = pygame.display.get_surface()

        #sprite group settings
        self.visible_sprites = pygame.sprite.Group
        self.obstacle_sprites = pygame.sprite.Group



    def run(self):
        # update/draw game
        pass

