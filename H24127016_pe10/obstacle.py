#coding:utf-8

import random
import pygame

pygame.init()

class Obstacle() :

	def __init__(self) :

		self.dimension    = pygame.Rect(0, 0, 16, 16)
		self.obstacleData = []
		self.color        = (150, 150, 200)

	def displayObstacles(self, surface) :

		for data in self.obstacleData :

			self.dimension.x, self.dimension.y = data[1], data[2]
			i = 0

			if data[3] == 1 :
				while i < data[0] :
					pygame.draw.rect(surface, self.color, self.dimension)
					self.dimension.y += 16
					i += 1

			else :
				while i < data[0] :
					pygame.draw.rect(surface, self.color, self.dimension)
					self.dimension.x += 16
					i += 1

pygame.quit()