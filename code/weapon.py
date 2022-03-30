import pygame

class Dagger(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)
       
        self.image = pygame.Surface((40,40))
        self.rect = self.image.get_rect(center = (player.rect.center[0], player.rect.center[1] + 40 ))