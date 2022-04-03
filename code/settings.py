import pygame

#Main Game Variables
WIDTH = 1280
HEIGHT = 720
FPS = 60
TILESIZE = 64
NATIVE_SCREEN = pygame.Surface((WIDTH , HEIGHT))

#UI
HEART_SIZE = .75
HEART_SPACING = 45
HEART_STARTING_POSITION = 15
HEART_FULL = '../assets/graphics/organized_scaled_tile_set/ui/full.png'
HEART_HALF = '../assets/graphics/organized_scaled_tile_set/ui/half.png'
HEART_EMPTY = '../assets/graphics/organized_scaled_tile_set/ui/empty.png'

MAX_AMMO_COLOR = '#DED07D'

UI_FONT = '../assets/font/Pixellettersfull-BnJ5.ttf'
UI_FONT_SIZE = 36
UI_AMMO_FONT_SIZE = 24

ITEM_BOX_SIZE = 80

#UI Colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#333333'
UI_BORDER_COLOR = '#DADADA'
TEXT_COLOR = '#DADADA'

#===#
#Data
#===#

#Weapons
dagger = {'cooldown' : 300, 'damage': 2, 'graphic': '../assets/graphics/organized_scaled_tile_set/weapons/dagger/up.png' }

bow = {'cooldown' : 500, 'damage': 1, 'cost': 1, 'speed': 10, 'graphic': '../assets/graphics/organized_scaled_tile_set/weapons/bow/right.png'}

#Enemies
enemy_data = {
    'skoolie' : {'health': 4, 'damage': 1, 'attack_type': 'slash', 'attack_sound': 'path', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 360},
    'slime' : {'health': 6, 'damage': 2, 'attack_type': 'slime_attack', 'attack_sound': 'path', 'speed': 1, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 300},
    'grelmo' : {'health': 16, 'damage': 3, 'attack_type': 'claw', 'attack_sound': 'path', 'speed': 1, 'resistance': 3, 'attack_radius': 100, 
    'notice_radius': 400},
}