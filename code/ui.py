import pygame
from settings import *

class UI:
    def __init__(self):
       
       #general variables
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        #health setup
        self.heart_full = pygame.image.load(HEART_FULL)
        self.heart_full = pygame.transform.rotozoom(self.heart_full, 0, HEART_SIZE)
        self.heart_half = pygame.image.load(HEART_HALF)
        self.heart_half = pygame.transform.rotozoom(self.heart_half, 0, HEART_SIZE)
        self.heart_empty = pygame.image.load(HEART_EMPTY)
        self.heart_empty = pygame.transform.rotozoom(self.heart_empty, 0, HEART_SIZE)    
        
    def heart_bar(self, health):
        #define three hearts
        self.heart_1 = self.heart_full
        self.heart_2 = self.heart_full
        self.heart_3 = self.heart_full

        #conditional logic to update current amount of hearts
        #this is very hard coded, wet, and something to refactor later
        if health == 6:
            self.heart_1 = self.heart_full
            self.heart_2 = self.heart_full
            self.heart_3 = self.heart_full
        elif health == 5:
            self.heart_1 = self.heart_full
            self.heart_2 = self.heart_full
            self.heart_3 = self.heart_half
        elif health == 4:
            self.heart_1 = self.heart_full
            self.heart_2 = self.heart_full
            self.heart_3 = self.heart_empty           
        elif health == 3:
            self.heart_1 = self.heart_full
            self.heart_2 = self.heart_half
            self.heart_3 = self.heart_empty
        elif health == 2:
            self.heart_1 = self.heart_full
            self.heart_2 = self.heart_empty
            self.heart_3 = self.heart_empty
        elif health == 1:
            self.heart_1 = self.heart_half
            self.heart_2 = self.heart_empty
            self.heart_3 = self.heart_empty
        else:
            self.heart_1 = self.heart_empty
            self.heart_2 = self.heart_empty
            self.heart_3 = self.heart_empty

        #render hearts (to change position of bar and spacing, go to settings)
        self.display_surface.blit(self.heart_1, (HEART_STARTING_POSITION, 10))
        self.display_surface.blit(self.heart_2, (HEART_STARTING_POSITION + HEART_SPACING, 10))
        self.display_surface.blit(self.heart_3, (HEART_STARTING_POSITION + (HEART_SPACING * 2), 10))

    def ammo_count(self, ammo):
        #create text surface and rect for ammo count
        text_surface = self.font.render(
            'Arrows: ' + str(ammo),
            False,
            HIGHLIGHTED_TEXT_COLOR if ammo == 15 else TEXT_COLOR)
        text_rectangle = text_surface.get_rect(topleft = (25, 65))

        #display text for ammo count
        self.display_surface.blit(text_surface, text_rectangle)


    def selection_box(self, left, top):
        #create and draw a rectangle to hold equipped item
        bg_rectangle = pygame.Rect(left, top, ITEM_BOX_SIZE, ITEM_BOX_SIZE )
        #base rectangle
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rectangle)
        #rectangle border
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rectangle, 2)
        
        return bg_rectangle

    def dagger_overlay(self):
        #return of selection_box gives the rectangle
        bg_rectangle = self.selection_box(15, 625)  
       
        #dagger image import 
        dagger_surface = pygame.image.load(dagger['graphic']).convert_alpha()
        #create dagger_rectangle and use bg_rectangle as reference
        dagger_rectangle = dagger_surface.get_rect(center = bg_rectangle.center)
        
        #add key command text
        text_surface = self.font.render('Z', False, TEXT_COLOR)
        #using Vector2 to move the text a tad to the left
        text_rectangle = text_surface.get_rect(bottomright = bg_rectangle.bottomright + pygame.math.Vector2(-5, 0))
        
        #render dagger and text
        self.display_surface.blit(dagger_surface, dagger_rectangle)
        self.display_surface.blit(text_surface, text_rectangle)

    def bow_overlay(self):
        #return of selection_box gives the rectangle
        bg_rectangle = self.selection_box(80, 605)  
       
        #bow image import 
        bow_surface = pygame.image.load(bow['graphic']).convert_alpha()
        #bow is larger sprite so scaling down
        bow_surface = pygame.transform.rotozoom(bow_surface, 0, .6)

        #create bow_rectangle and use bg_rectangle as reference
        bow_rectangle = bow_surface.get_rect(center = bg_rectangle.center)
        
        #add key command text
        text_surface = self.font.render('X', False, TEXT_COLOR)
        #using Vector2 to move the text a tad to the left
        text_rectangle = text_surface.get_rect(bottomright = bg_rectangle.bottomright + pygame.math.Vector2(-5, 0))
        
        #render dagger and text
        self.display_surface.blit(bow_surface, bow_rectangle)
        self.display_surface.blit(text_surface, text_rectangle)
    
    def display(self, player):
        self.heart_bar(player.health)
        self.ammo_count(player.ammo)
        self.bow_overlay()
        self.dagger_overlay()

        