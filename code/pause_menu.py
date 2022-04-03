import pygame, sys
from settings import *


class Pause:
    def __init__(self, toggle_menu):

        #get display surface
        self.display_surface = pygame.display.get_surface()

        self.font = pygame.font.Font(UI_FONT, UI_PAUSE_FONT_SIZE)
        self.option_list = ['Resume', 'Exit']

        #selection system
        self.selection_index = 0
        self.selection_time = None
        self.can_move = True
        self.toggle_menu = toggle_menu

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
            if keys[pygame.K_c]:
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
                
                #resume game
                if self.selection_index == 0:
                    self.toggle_menu()
                #shut down game
                else:
                    pygame.quit()
                    sys.exit()


    def selection_cooldown(self):
        #if can_move is false, start the timer
        if not self.can_move:
            current_time = pygame.time.get_ticks()
            #set cooldown of keypress here
            if current_time - self.selection_time >= 200:
                self.can_move = True
    
    def draw_options(self):      
        #draw pause menu background
        bg_rectangle = pygame.Rect(800, 50, 400, 550)
        #base rectangle
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rectangle)
        #rectangle border
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rectangle, 2)

        #add resume text
        resume_surface = self.font.render(
            self.option_list[0],
            False,
            #hard-coded for the time being, but something to refactor if menu gets larger
            HIGHLIGHTED_TEXT_COLOR if self.selection_index == 0 else TEXT_COLOR)
        resume_rectangle = resume_surface.get_rect(topright = bg_rectangle.topright + pygame.math.Vector2(-50, 15))
    
        #add exit text
        exit_surface = self.font.render(
            self.option_list[1],
            False,
            #hard-coded for the time being, but something to expand if menu gets larger
            HIGHLIGHTED_TEXT_COLOR if self.selection_index == 1 else TEXT_COLOR)
        exit_rectangle = exit_surface.get_rect(topright = bg_rectangle.topright + pygame.math.Vector2(-50, 65)) 

        #draw text
        self.display_surface.blit(resume_surface, resume_rectangle)
        self.display_surface.blit(exit_surface, exit_rectangle)


    def display(self):
        #invoke functions, draw pause menu
        self.input()
        self.selection_cooldown()
        self.draw_options()