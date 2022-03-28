import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug



#class that displays sprites of current room and also handles their interactions
class Room:
    def __init__(self):

        #get display surface
        self.display_surf = pygame.display.get_surface()

        #sprite group settings
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        #run create_map method to display sprites
        self.create_map()

    #method to loop through maps in settings.py to display sprites 
    def create_map(self):
        #enumerating to get both row and index
        for row_index, row in enumerate(ROOM_1):
            #enumerating individual row to get column and element within row
            for column_index, column in enumerate(row):
                #defining x,y position of each tile     
                x = column_index * TILESIZE
                y = row_index * TILESIZE
                
                #if 'x' map Tile sprite to visible_sprites group in proper position
                if column == 'x':
                    Tile((x,y), [self.visible_sprites, self.obstacle_sprites])
                if column == 'p':
                    #store player in variable to be targetable
                    self.player = Player((x,y), [self.visible_sprites])


                

    def run(self):
        # update/draw game
        self.visible_sprites.draw(self.display_surf)
        self.visible_sprites.update()
        debug(self.player.direction)

