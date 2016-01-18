import pygame
import sys
import constants
import lasers
import random
import data
import background
from player import Player
import asteroids


def main():
    # setup
    pygame.init()
    pygame.mouse.set_visible(False)
    size = (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Space Shooter")

    # create background
    create_background(50)
    # create asteroid field
    create_asteroids(15)
    # create player
    player = Player()
    data.all_sprites_list.add(player)
    data.player_list.add(player)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                create_laser(1, player)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                create_laser(2, player)

        data.all_sprites_list.update()
        screen.fill(constants.BLACK)

        for group in data.all_lists:  # loop to draw player last to avoid background from becoming foreground
            group.draw(screen)
        clock.tick(60)
        pygame.display.flip()


def create_laser(type_laser, player):
    if type_laser == 1:
        laser = lasers.BasicLaser()
    elif type_laser == 2:
        laser = lasers.HeavyLaser()
    else:
        laser = lasers.BasicLaser()
    laser.rect.centerx = player.rect.centerx
    laser.rect.centery = player.rect.centery
    data.all_sprites_list.add(laser)
    data.laser_list.add(laser)


def create_background(n):
    for i in range(n):
        star = background.Stars()
        star.rect.x = random.randrange(constants.SCREEN_WIDTH)
        star.rect.y = random.randrange(constants.SCREEN_HEIGHT)
        data.all_sprites_list.add(star)
        data.background_list.add(star)


def create_asteroids(n):
    for i in range(n):
        asteroid = asteroids.Asteroid(random.randrange(40, 100), random.randrange(2, 7))
        asteroid.reset_pos()
        data.all_sprites_list.add(asteroid)
        data.asteroid_list.add(asteroid)

if __name__ == "__main__":
    main()
