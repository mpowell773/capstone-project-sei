import pygame

from settings import ROOM_1

#class that displays sprites of current room and also handles their interactions
class Room:
    def __init__(self):

        #get display surface
        self.display_surf = pygame.display.get_surface()

        #sprite group settings
        self.visible_sprites = pygame.sprite.Group
        self.obstacle_sprites = pygame.sprite.Group

        #run create_map method to display sprites
        self.create_map()

    #method to loop through maps in settings.py to display sprites 
    def create_map(self):
        #enumerating to get both row and index
        for row_index, row in enumerate(ROOM_1):
            #enumerating individual row to get column and element within row
            for column_index, column in enumerate(row):
                pass
                

    def run(self):
        # update/draw game
        pass

