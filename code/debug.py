import pygame
from settings import NATIVE_SCREEN
pygame.init()
font = pygame.font.Font(None, 30)

#1st arg allows variables or whatever to be passed in
def debug(info, y = 10, x = 10):
    #grabbing main screen of game
    display_surf = NATIVE_SCREEN
   
    #creating surface and rectangle 
    debug_surf = font.render(str(info), True, 'White')
    debug_rect = debug_surf.get_rect(topleft = (x, y))

    #draw the rectangle and have update on main surface
    pygame.draw.rect(display_surf, 'Black', debug_rect)
    display_surf.blit(debug_surf, debug_rect)

