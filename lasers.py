import pygame
import constants
import data


class BasicLaser(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 10
        self.height = 20
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(constants.GREEN)
        self.vel = -10
        self.rect = self.image.get_rect()
        self.damage = 1

    def update(self):
        self.rect.y += self.vel
        if pygame.sprite.spritecollideany(self, data.asteroid_list):
            data.laser_list.remove(self)
        if self.rect.y + self.height < 0:
                    data.laser_list.remove(self)


class HeavyLaser(BasicLaser):
    def __init__(self):
        super().__init__()
        self.width = 20
        self.height = 25
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(constants.GREEN)
        self.vel = -5
        self.damage = 3
