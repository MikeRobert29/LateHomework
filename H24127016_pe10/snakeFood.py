#coding:utf-8

from myModule import pixelsInTheCircle
from random import randint
import pygame

pygame.init()

class Food () :

	def __init__(self, radius = 8, color  = (128, 255, 0)) :

		self.arial_font  = pygame.font.SysFont("arial", 20, True)
		self.tag         = "π"
		self.coordinates = pygame.Rect(400, 320, 16, 16)
		self.color       = color
		self.radius      = radius

	def displayTheFood(self, surface) :

		center = [self.coordinates.x + self.radius, self.coordinates.y + self.radius]

		pygame.draw.rect(surface, (0, 0, 0), self.coordinates)

		actualFood = pixelsInTheCircle(surface, center, self.radius)

		for pixel in actualFood :
			surface.set_at(pixel, self.color)

		render = self.arial_font.render(self.tag, False, (0, 0, 0))
		surface.blit(render, [self.coordinates.x + 2, self.coordinates.y - 4])

	def foodChangePosition(self, surface) :

		newPositionX, newPositionY = self.coordinates.x, self.coordinates.y

		while 1 :

			xPositions = randint(1, 51)
			yPositions = randint(1, 39)

			newPositionX = xPositions * 16 - 16
			newPositionY = yPositions * 16 - 16

			if newPositionX == self.coordinates.x and newPositionY == self.coordinates.y :
				continue

			if surface.get_at((newPositionX, newPositionY)) != (0, 0, 0) :
				continue
			else :
				break

		self.coordinates.x, self.coordinates.y = newPositionX, newPositionY

pygame.quit()