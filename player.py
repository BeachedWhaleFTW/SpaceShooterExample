import pygame
import constants
import data


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/tie.png')
        #self.image.fill(constants.RED)
        self.rect = self.image.get_rect()

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

        if pygame.sprite.spritecollideany(self, data.asteroid_list):
            print('Asteroid Hit')
            self.take_damage()

    def take_damage(self):
        pass
