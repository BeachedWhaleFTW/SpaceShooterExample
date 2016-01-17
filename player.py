import pygame
import constants
#from spritesheet_functions import SpriteSheet

class Player(pygame.sprite.Sprite):

	def __init__(self):

		super().__init__()

		#insert some sprite sheet animation bullshit later

		self.image = pygame.Surface([20,20])
		self.image.fill(constants.RED)

		self.rect = self.image.get_rect()

	def update(self):
		pos = pygame.mouse.get_pos()

		self.rect.x = pos[0]
		self.rect.y = pos[1]
