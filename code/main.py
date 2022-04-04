import pygame, sys
from settings import *
from dungeon import Dungeon
from death_screen import Death_Screen
from title_screen import Title_Screen

#class object to set up base game functionality such as running and exiting
class Game:
    def __init__(self):

        #initialize pygame mixer
        pygame.mixer.init()
        #initializes pygame
        pygame.init()
        #screen changes size of game window (scaling due to tileset size)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # self.native_screen = NATIVE_SCREEN
        #changes name of window
        pygame.display.set_caption('The Legend of Python')
        #initiate clock to control framerate
        self.clock = pygame.time.Clock()

        #game-state
        self.is_active = False
        self.is_dead = False

        #audio
        #dungeon ambience
        self.dungeon_ambience = pygame.mixer.Sound('../assets/audio/ambience_music/dungeon_ambience.wav')
        self.dungeon_ambience.set_volume(.1)
        #intro music
        self.intro_music = pygame.mixer.Sound('../assets/audio/ambience_music/intro_music_trimmed.wav')
        self.intro_music.set_volume(.5)
        #death hit
        self.death_hit = pygame.mixer.Sound('../assets/audio/ambience_music/death_hit_trimmed.wav')
        self.death_hit.set_volume(.5)   
        self.death_hit_has_played = False    

        #intro music loops until player starts game
        #loop is pretty questionable quality-wise
        #something to look at in the future
        self.intro_music.play(loops = -1)
                
        #main gameplay instance
        self.dungeon = Dungeon(self.toggle_death, self.dungeon_ambience)
        #death screen
        self.death_screen = Death_Screen(self.toggle_death)
        #title screen
        self.title_screen= Title_Screen(self.start_game)

    def toggle_death(self):
        self.is_active = not self.is_active
        self.is_dead = not self.is_dead

    def start_game(self):
        self.is_active = True
        self.is_dead = False

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
                #fade out music
                self.intro_music.fadeout(100)
                self.death_hit.fadeout(100)
                self.death_hit_has_played = False  
                #create instance of room in main game
                self.dungeon.run()        
            elif not self.is_active and self.is_dead:
                #display death screen
                self.death_screen.run()
                self.dungeon_ambience.fadeout(100)
                #conditional logic to prevent infinite plays 
                if not self.death_hit_has_played:
                    self.death_hit.play()
                    self.death_hit_has_played = True
                #reset dungeon
                self.dungeon.reset_instance()
            else:
                self.title_screen.run()
       

            #draw updated elements
            pygame.display.update()
            #framerate ceiling
            self.clock.tick(FPS)

#if main file, create an instance of game and then run it
if __name__ == '__main__':
    game = Game()
    game.run()