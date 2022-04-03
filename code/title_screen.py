import pygame
from settings import *

class Title_Screen:
    def __init__(self, start_game):

        #get display surface
        self.display_surface = pygame.display.get_surface()
       
        #center of screen 
        self.center_width = WIDTH // 2
        self.center_height = HEIGHT // 2

        #method to start the game
        self.start_game = start_game
        #store font 
        self.title_font = pygame.font.Font(UI_FONT, TITLE_FONT_SIZE)
        self.font = pygame.font.Font(UI_FONT, UI_PAUSE_FONT_SIZE)

    def input(self):
        #store key presses in variable
        keys = pygame.key.get_pressed()

        if keys[pygame.K_c]:
            self.start_game()

    def draw_screen(self):
            #create upper text
            title_text = self.title_font.render('The Legend of ', False, TEXT_COLOR)
            title_rect = title_text.get_rect(center = (self.center_width, 75))

            #python image
            python_surface = pygame.image.load('../assets/graphics/exported_images/1024px-Python-logo-notext.svg.png')
            python_surface = pygame.transform.rotozoom(python_surface, 0, .4)
            python_rect = python_surface.get_rect(center = (self.center_width, self.center_height))

            #create instruction text
            instruction_text = self.font.render("Press 'C' to continue", False, TEXT_COLOR)
            instruction_rect = instruction_text.get_rect(center = (self.center_width, 650))

            #render text and images
            self.display_surface.blit(title_text, title_rect)
            self.display_surface.blit(python_surface, python_rect)
            self.display_surface.blit(instruction_text, instruction_rect)

    def run(self):

        self.display_surface.fill('black')
        self.input()
        self.draw_screen()