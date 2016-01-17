import pygame
from spritesheet_functions import SpriteSheet

basic_laser = (5, 35, 20, 25)

class BasicLaser(pygame.sprite.Sprite):

	def __init__(self, sprite_sheet_data):
		super().__init__()

		self.vel = -20

		sprite_sheet = SpriteSheet("lasers.png")

		self.image = sprite_sheet.get_image(sprite_sheet_data[0],
											sprite_sheet_data[1],
											sprite_sheet_data[2],
											sprite_sheet_data[3])

		self.rect = self.image.get_rect()

	def update(self):

		self.rect.y += self.vel