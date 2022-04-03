import pygame, sys
from settings import *

class Death_Screen:
    def __init__(self, toggle_gameplay):

        #get display surface
        self.display_surface = pygame.display.get_surface()
       
        #center of screen 
        self.center_width = WIDTH // 2
        self.center_height = HEIGHT // 2

        #method to return to dungeon instance
        self.toggle_gameplay = toggle_gameplay
        #store font 
        self.font = pygame.font.Font(UI_FONT, UI_PAUSE_FONT_SIZE)


    def input(self):
        #store key presses in variable
        keys = pygame.key.get_pressed()

        if keys[pygame.K_c]:
            pygame.quit()
            sys.exit()


    def draw_screen(self):
            #create upper text
            death_text = self.font.render("You have died D:", False, TEXT_COLOR)
            death_rect = death_text.get_rect(center = (self.center_width, self.center_height) + pygame.math.Vector2(0, -100))

            #greemie image
            greemie_surface = pygame.image.load('../assets/graphics/organized_scaled_tile_set/entities/player/right_idle/lil-greemie_1.png')
            greemie_surface = pygame.transform.rotozoom(greemie_surface, 90, 1.3)
            greemie_rect = greemie_surface.get_rect(center = (self.center_width, self.center_height) + pygame.math.Vector2(-42, 0))

            #create instruction text
            instruction_text = self.font.render("Press 'C' to exit out of the game.", False, TEXT_COLOR)
            instruction_rect = instruction_text.get_rect(center = (self.center_width, self.center_height) + pygame.math.Vector2(0, 100))

            #render text and images
            self.display_surface.blit(death_text, death_rect)
            self.display_surface.blit(greemie_surface, greemie_rect)
            self.display_surface.blit(instruction_text, instruction_rect)

    def run(self):

        self.display_surface.fill('black')
        self.input()
        self.draw_screen()