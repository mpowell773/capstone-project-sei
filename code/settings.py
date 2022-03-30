import pygame

#Main Game Variables
WIDTH = 1280
HEIGHT = 720
FPS = 60
TILESIZE = 64
NATIVE_SCREEN = pygame.Surface((WIDTH , HEIGHT))

# weapon
dagger = {'cooldown' : 100, 'damage': 5, 'graphic': '../assets/graphics/organized_scaled_tile_set/weapons/03_dagger.png' }