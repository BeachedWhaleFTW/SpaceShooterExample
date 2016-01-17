import constants
import pygame
import random

class Asteroid(pygame.sprite.Sprite):

	def __init__(self, size, speed):

		super().__init__()

		self.image = pygame.Surface([size, size])
		self.image.fill(constants.BLUE)
		self.rect = self.image.get_rect()

		self.size = size
		self.speed = speed

	def update(self):
		self.rect.y += self.speed

		if self.rect.y > constants.SCREEN_HEIGHT + self.size:
			self.reset_pos()

	def reset_pos(self):
		#self.size = random.randrange()

		self.rect.y = random.randrange(-300, -20)
		self.rect.x = random.randrange(constants.SCREEN_WIDTH - self.size)