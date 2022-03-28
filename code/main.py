import pygame, sys
from settings import *

# class object to set up base game functionality such as running and exiting
class Game:
    def __init__(self):

        pygame.init()
        #screen changes size of game window
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
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
            
            #fill screen with black
            self.screen.fill('black')
            #draw updated elements
            pygame.display.update()
            #framerate ceiling
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()