import pygame
from particles import AnimationPlayer
from settings import *
from tile import Tile
from player import Player
from misc_functions import import_csv_layout, import_folder
from weapon import Dagger
from ui import UI
from enemy import Enemy
from bow_and_arrow import Bow
from pickup import Arrow_Bundle

#class that displays sprites of current room and also handles their interactions
class Dungeon:
    def __init__(self):

        #get display surface
        self.display_surf = pygame.display.get_surface()

        #sprite group settings
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        
        #attack sprites
        self.current_attack = None
        self.attack_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()

        #pickup sprites
        self.collector_sprite = pygame.sprite.Group()
        self.pickup_sprites = pygame.sprite.Group()

        #run create_map method to display sprites
        self.create_map()

        #user inteface
        self.ui = UI()

        #particles
        self.animation_player = AnimationPlayer()

    #method to loop through maps in settings.py to display sprites 
    def create_map(self):
       
        #dict of layouts 
        layout = {
            'boundary': import_csv_layout('../levels/dungeon/dungeon_clean_Floor_Block.csv'),
            'walls': import_csv_layout('../levels/dungeon/dungeon_clean_Walls.csv'),
            'details': import_csv_layout('../levels/dungeon/dungeon_clean_Details.csv'),
            'crates': import_csv_layout('../levels/dungeon/dungeon_clean_Crates.csv'),
            'chests': import_csv_layout('../levels/dungeon/dungeon_clean_Chests.csv'),
            'objects': import_csv_layout('../levels/dungeon/dungeon_clean_Objects.csv'),
            'doors': import_csv_layout('../levels/dungeon/dungeon_clean_Doors.csv'),
            'entities': import_csv_layout('../levels/dungeon/dungeon_clean_Entities.csv'),
        }

        #dict of graphics
        graphics = {
            'walls' : import_folder('../assets/graphics/organized_scaled_tile_set/walls'),
            'details' : import_folder('../assets/graphics/organized_scaled_tile_set/details'),
            'crates' : import_folder('../assets/graphics/organized_scaled_tile_set/crates'),
            'chests' : import_folder('../assets/graphics/organized_scaled_tile_set/chests'),
            'objects' : import_folder('../assets/graphics/organized_scaled_tile_set/objects'),
            'doors' : import_folder('../assets/graphics/organized_scaled_tile_set/doors'),
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
                            #go through graphics list and use index of list to properly assign images
                            wall_image = graphics['walls'][int(column)]
                            Tile((x,y), [self.visible_sprites], 'walls', wall_image)
                        
                        if style == 'details':
                            detail_image = graphics['details'][int(column)]
                            Tile((x,y), [self.visible_sprites], 'details', detail_image)
                
                        if style == 'crates':
                            crate_image = graphics['crates'][int(column)]
                            Tile((x,y), [self.visible_sprites, self.obstacle_sprites, self.attackable_sprites], 'crates', crate_image)

                        if style == 'chests':
                            chest_image = graphics['chests'][int(column)]
                            Tile((x,y), [self.visible_sprites, self.obstacle_sprites], 'chests', chest_image)
                        
                        if style == 'objects':
                            object_image = graphics['objects'][int(column)]
                            Tile((x,y), [self.visible_sprites, self.obstacle_sprites], 'objects', object_image)

                        if style == 'doors':
                            door_image = graphics['doors'][int(column)]
                            Tile((x,y), [self.visible_sprites], 'doors', door_image)

                        if style == 'entities':
                            if column == '0':
                                #spawn player into dungeon
                                self.player = Player(
                                    (x, y), 
                                    [self.visible_sprites, self.collector_sprite], 
                                    self.obstacle_sprites, 
                                    self.create_attack,
                                    self.destroy_attack,
                                    self.create_arrow)
                            else:
                                #spawn enemies onto map
                                #conditional logic to pass correct enemy name via csv file down to enemy class
                                if column == '1': enemy_name = 'skoolie'
                                elif column == '2': enemy_name = 'slime'
                                else: enemy_name = 'grelmo'

                                Enemy(
                                    enemy_name, 
                                    (x,y),
                                    [self.visible_sprites, self.attackable_sprites], 
                                    self.obstacle_sprites,
                                    self.damage_player,
                                    self.trigger_death_particles)
                                
    def create_attack(self):
        #when invoked, create this sprite and do its actions
        self.current_attack = Dagger(self.player, [self.visible_sprites, self.attack_sprites])

    def create_arrow(self):
        self.current_attack = Bow(
            self.player, 
            [self.visible_sprites], 
            self.attack_sprites,
            self.obstacle_sprites)

    def destroy_attack(self):
        #if variable has a data in it
        if self.current_attack:
            #destroy the weapon sprite
            self.current_attack.kill()
        #set to None afterwards
        self.current_attack = None

    def player_attack_logic(self):
        if self.attack_sprites:
            for attack_sprite in self.attack_sprites:
                #if our attack sprite hits any attackable sprite, store in collision_sprites
                collision_sprites = pygame.sprite.spritecollide(attack_sprite, self.attackable_sprites, False)
                #if there are sprites in collision_sprites
                if collision_sprites:
                    #cycle through them
                    for target_sprite in collision_sprites:
                        #if crates, destroy them in one hit
                        if target_sprite.sprite_type == 'crates':
                            #get the center of target sprite
                            position = target_sprite.rect.center
                            offset = pygame.math.Vector2(0, 20)
                            #play the smoke particle animation
                            self.animation_player.create_smoke(position + offset, [self.visible_sprites])
                            target_sprite.kill()
                            Arrow_Bundle(position + offset, [self.visible_sprites, self.pickup_sprites], self.player)

                        else:
                            #damage enemy sprite
                            target_sprite.get_damage(self.player, attack_sprite.sprite_type)
                            #if arrow hits enemy, destroy it
                            if attack_sprite.sprite_type == 'arrow':
                                attack_sprite.kill()                            
                            
    def player_pickup(self):
        #player is collector sprite
        if self.collector_sprite:
            for collector_sprite in self.collector_sprite:
                #if player collides with a pickup
                collision_sprites = pygame.sprite.spritecollide(collector_sprite, self.pickup_sprites, False)
                if collision_sprites:
                    #check the pickup-type
                    for target_sprite in collision_sprites:
                        if target_sprite.sprite_type == 'arrow_bundle':
                            target_sprite.pickup()
                            
    def damage_player(self, amount, attack_type):
        if self.player.vulnerable:
            #lower player health
            self.player.health -= amount
            #give player i-frames
            self.player.vulnerable = False
            #start timer for i-frames
            self.player.hurt_time = pygame.time.get_ticks()
            #play particles depending on enemy
            offset = pygame.math.Vector2(0, 20)
            self.animation_player.create_particles(attack_type, self.player.rect.center + offset, [self.visible_sprites])

    def trigger_death_particles(self, position, particle_type):
        #create method to pass down animation player to enemy.py
        self.animation_player.create_particles(particle_type, position, self.visible_sprites)

    def run(self):
        # update/draw game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.visible_sprites.enemy_update(self.player)
        self.player_attack_logic()
        self.player_pickup()
        self.ui.display(self.player)

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
        self.floor_surface = pygame.image.load('../assets/graphics/exported_images/dungeon_floor_03_31_22.png').convert()
        self.floor_rect = self.floor_surface.get_rect(topleft = (0,0))


    #adds false depth effect
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

    def enemy_update(self, player):
        #adding update method for enemy sprites. 
        #to get enemy sprites, we check through each sprites, make sure the attribute 'sprite_type' exists and then fill out list with the sprite_type 'enemy"
        enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'enemy']
        #For each of these sprites, pass in player property to enemy_update in enemy.py
        for sprite in enemy_sprites:
            sprite.enemy_update(player)