import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug
from misc_functions import import_csv_layout, import_folder



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
       
        #dict of layouts 
        layout = {
            'boundary': import_csv_layout('../levels/dungeon/dungeon_FloorBlock.csv'),
            'walls': import_csv_layout('../levels/dungeon/dungeon_Walls.csv'),
            'detail': import_csv_layout('../levels/dungeon/dungeon_Detail.csv'),
            'crates': import_csv_layout('../levels/dungeon/dungeon_Crates.csv'),
            'chests': import_csv_layout('../levels/dungeon/dungeon_Chests.csv'),
            'objects': import_csv_layout('../levels/dungeon/dungeon_Objects.csv'),
        }

        #dict of graphics
        graphics = {
            'all_graphics' : import_folder('../assets/graphics/scaled_tile_set')
        }

        #for loop to cycle through our layout dict
        for style, layout in layout.items():
            # enumerating to get both row and index
            for row_index, row in enumerate(layout):
                #enumerating individual row to get column and element within row
                for column_index, column in enumerate(row):
                    #csv uses -1 as white space instead of ' ', so we must ignore it
                    if column != '-1':
                        #defining x,y position of each tile     
                        x = column_index * TILESIZE
                        y = row_index * TILESIZE
                
                        #checking what key in dict is and then assigning the sprite to the mapped layout, in this case, boundary
                        if style == 'boundary':
                            Tile((x,y), [self.obstacle_sprites], 'invisible')

                        if style == 'walls':
                            #go through graphics list
                            wall_image = graphics['all_graphics'][int(column)]
                            Tile((x,y), [self.visible_sprites], 'walls', wall_image)
                
        #         #if 'x' map Tile sprite to visible_sprites group in proper position
        #         if column == 'x':
        #             Tile((x,y), [self.visible_sprites, self.obstacle_sprites])
        #         if column == 'p':
        #             #store player in variable to be targetable
        #             self.player = Player((x,y), [self.visible_sprites], self.obstacle_sprites)
        self.player = Player((1600, 3000), [self.visible_sprites], self.obstacle_sprites)

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


        #create floor
        self.floor_surface = pygame.image.load('../assets/graphics/exported_images/dungeon_floor_no_walls.png').convert()
        self.floor_rect = self.floor_surface.get_rect(topleft = (0,0))


    #method to draw with our camera
    def custom_draw(self, player):

        #finding offset by getting center of player rect and subtracting respective value to half of screen
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        #draw floor
        offset_position_floor = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surface, offset_position_floor)

        #for each sprite in group sort them by their y position
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            #subtract offset from sprite rect
            offset_position = sprite.rect.topleft - self.offset
            #draw them on screen
            self.display_surface.blit(sprite.image, offset_position)



