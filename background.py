import pygame
import constants
import random


class Stars(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size = 2
        self.image = pygame.Surface([self.size, self.size])
        self.image.fill(constants.WHITE)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 1
        if self.rect.y > constants.SCREEN_HEIGHT + self.size:
            self.reset_pos()

    def reset_pos(self):
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(0, constants.SCREEN_WIDTH)
