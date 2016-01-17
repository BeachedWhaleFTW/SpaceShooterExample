import pygame
import constants
import lasers
import random
from background import Stars
from player import Player
from asteroids import Asteroid

def main():
	#setup
	pygame.init()

	pygame.mouse.set_visible(False)

	size = (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
	screen = pygame.display.set_mode(size)

	pygame.display.set_caption("Space Shooter")

	#init all sprites for start
	all_sprites_list = pygame.sprite.Group()
	laser_list = pygame.sprite.Group()
	background_list = pygame.sprite.Group()
	player_list = pygame.sprite.Group()
	asteroid_list = pygame.sprite.Group()

	all_lists = [background_list, asteroid_list, laser_list,  player_list]

	for i in range(25):
		star = Stars()
		star.rect.x = random.randrange(constants.SCREEN_WIDTH)
		star.rect.y = random.randrange(constants.SCREEN_HEIGHT)
		all_sprites_list.add(star)
		background_list.add(star)

	for i in range(10):
		asteroid = Asteroid(random.randrange(10, 30), random.randrange(2, 7))
		asteroid.reset_pos()
		all_sprites_list.add(asteroid)
		asteroid_list.add(asteroid)

	player = Player()
	all_sprites_list.add(player)
	player_list.add(player)

	#stuff for gameloop
	done = False

	clock = pygame.time.Clock()

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			
			elif event.type == pygame.MOUSEBUTTONDOWN:
					laser = lasers.BasicLaser(lasers.basic_laser)

					laser.rect.x = player.rect.x
					laser.rect.y = player.rect.y

					all_sprites_list.add(laser)
					laser_list.add(laser)
		
		all_sprites_list.update()

		screen.fill(constants.BLACK)

		#loop to draw player last to avoid background from becoming foreground 
		for list in all_lists:
			list.draw(screen)

		clock.tick(30)
		pygame.display.flip()

	pygame.quit()

if __name__ == "__main__":
	main()