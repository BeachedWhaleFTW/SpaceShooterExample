# used to pull sprites from spritesheets

import pygame
import constants

class SpriteSheet(object):
	#points to the sprite sheet image
	sprite_sheet = None

	def __init__(self, filename):
		self.sprite_sheet = pygame.image.load(filename).convert()

	def get_image(self, x, y, width, height):
		"""Grab a single image from the spritesheet using x,y coords and width, height"""
		#create a blank image
		image = pygame.Surface([width, height]).convert()
		#blit image from sprite sheet onto created image
		image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
		#set transparency 
		image.set_colorkey(constants.BLACK)

		return image