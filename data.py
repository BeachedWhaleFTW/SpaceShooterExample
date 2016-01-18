# file to contain the global lists of sprites
import pygame

all_sprites_list = pygame.sprite.Group()
laser_list = pygame.sprite.Group()
background_list = pygame.sprite.Group()
player_list = pygame.sprite.Group()
asteroid_list = pygame.sprite.Group()

all_lists = [background_list, asteroid_list, laser_list, player_list]
