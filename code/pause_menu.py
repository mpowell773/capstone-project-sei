import pygame
from settings import *

class Pause:
    def __init__(self):

        #get display surface
        self.display_surface = pygame.display.get_surface()

        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        self.option_list = ['resume', 'exit']

        #selection system
        self.selection_index = 0
        self.selection_time = None
        self.can_move = True

    def input(self):
        #store key presses in variable
        keys = pygame.key.get_pressed()


        #move up or down in menu
        if self.can_move:
            #press down and make sure index is less than the length of the list
            if keys[pygame.K_DOWN] and self.selection_index < len(self.option_list) - 1:
                self.selection_index += 1
                #start timer
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
            #press up and make sure the index is at least greater than 1 or equal to one
            elif keys[pygame.K_UP] and self.selection_index >= 1:
                self.selection_index -= 1
                #start timer
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()

            #select option in menu
            if keys[pygame.K_z]:
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
                print(self.selection_index)


    def selection_cooldown(self):
        if not self.can_move:
            current_time = pygame.time.get_ticks()
            if current_time - self.selection_time >= 300:
                self.can_move = True
  
            
    def display(self):
       
        #draw pause menu background
        bg_rectangle = pygame.Rect(800, 50, 400, 550)
        #base rectangle
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rectangle)
        #rectangle border
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rectangle, 2)

        self.input()
        self.selection_cooldown()

