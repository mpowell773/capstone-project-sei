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

UI_FONT = '../assets/font/Pixellettersfull-BnJ5.ttf'
UI_FONT_SIZE = 36

ITEM_BOX_SIZE = 80

#General colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#333333'
UI_BORDER_COLOR = '#DADADA'
TEXT_COLOR = '#DADADA'

#UI Colors
UI_BORDER_COLOR_ACTIVE = 'gold'

#Weapon
dagger = {'cooldown' : 100, 'damage': 5, 'graphic': '../assets/graphics/organized_scaled_tile_set/weapons/dagger/up.png' }