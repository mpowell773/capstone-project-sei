import pygame, sys
from settings import *
from dungeon import Dungeon




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

        self.dungeon = Dungeon()

    def run(self):
        while True:
            #user event loop
            for event in pygame.event.get():
                #exits out of game with exit window button
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            
            self.screen.fill('black')  
            
            #create instance of room in main game
            self.dungeon.run()

            #scale up screen
            # self.scaled_screen = pygame.transform.scale(self.native_screen, self.screen.get_size())   
            # self.screen.blit(self.scaled_screen, (0,0))
            #draw updated elements
            pygame.display.update()
            #framerate ceiling
            self.clock.tick(FPS)

#if main file, create an instance of game and then run it
if __name__ == '__main__':
    game = Game()
    game.run()