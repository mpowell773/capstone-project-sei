import pygame, sys
from settings import *
from dungeon import Dungeon
from death_screen import Death_Screen

#class object to set up base game functionality such as running and exiting
class Game:
    def __init__(self):

        pygame.init()
        #screen changes size of game window (scaling due to tileset size)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # self.native_screen = NATIVE_SCREEN
        #changes name of window
        pygame.display.set_caption('The Legend of Python')
        #initiate clock to control framerate
        self.clock = pygame.time.Clock()


        #game-state
        self.is_active = True

        #main gameplay instance
        self.dungeon = Dungeon(self.toggle_gameplay)
        #death screen
        self.death_screen = Death_Screen(self.toggle_gameplay)
 
    def toggle_gameplay(self):
        self.is_active = not self.is_active

    def run(self):
        while True:
            #user event loop
            for event in pygame.event.get():
                #exits out of game with exit window button
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    #pressing the escape key will open pause menu
                    if event.key == pygame.K_ESCAPE:
                        self.dungeon.toggle_menu()
        

            #fill screen with black so that weird rendering things don't happen with camera
            self.screen.fill('black')  
            
            if self.is_active:
                #create instance of room in main game
                self.dungeon.run()
            else:
                #display death screen
                self.death_screen.run()
                #reset dungeon
                self.dungeon.reset_instance()

            #draw updated elements
            pygame.display.update()
            #framerate ceiling
            self.clock.tick(FPS)

#if main file, create an instance of game and then run it
if __name__ == '__main__':
    game = Game()
    game.run()