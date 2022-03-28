import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug



#class that displays sprites of current room and also handles their interactions
class Dungeon:
    def __init__(self):

        #get display surface
        self.display_surf = pygame.display.get_surface()

        #sprite group settings
        self.visible_sprites = YSortCameraGroup()
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
                    self.player = Player((x,y), [self.visible_sprites], self.obstacle_sprites)

    def run(self):
        # update/draw game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        debug(self.player.direction)

#camera for game
class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        #inherit sprite group init
        super().__init__()
        
        #store main screen in variable
        self.display_surface = pygame.display.get_surface()
        
        #get center of screen by dividing half and storing respective values into variables
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
       
        #vector to move camera
        self.offset = pygame.math.Vector2()

    #method to draw with our camera
    def custom_draw(self, player):

        #finding offset by getting center of player rect and subtracting respective value to half of screen
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        #for each sprite in group
        for sprite in self.sprites():
            #subtract offset from sprite rect
            offset_position = sprite.rect.topleft - self.offset
            #draw them on screen
            self.display_surface.blit(sprite.image, offset_position)



