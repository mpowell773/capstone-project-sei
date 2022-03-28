import pygame, sys
from settings import *


#class object to set up base game functionality such as running and exiting
class Game:
    def __init__(self):

        pygame.init()
        #screen changes size of game window
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        #changes name of window
        pygame.display.set_caption('The Legend of Python')
        #initiate clock to control framerate
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            #user event loop
            for event in pygame.event.get():
                #exits out of game with exit window button
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.screen.fill('black')      
            #draw updated elements
            pygame.display.update()
            #framerate ceiling
            self.clock.tick(FPS)

#if main file, create an instance of game and then run it
if __name__ == '__main__':
    game = Game()
    game.run()