#coding:utf-8

import pygame

pygame.init()

class Snake () :

	def __init__(self) :

		self.headCoordinates        = pygame.Rect(32, 320, 16, 16)
		self.rightEyeCoordinates    = pygame.Rect(self.headCoordinates.right - 6, self.headCoordinates.left + 2, 4, 4)
		self.leftEyeCoordinates     = pygame.Rect(self.headCoordinates.right - 6, self.headCoordinates.bottom - 8, 4, 4)
		self.headColor              = (255, 0, 0)
		self.eyesColor              = (0, 0, 0)
		self.tailColor              = (193, 97, 0)
		self.spotColor              = (0, 0, 0)
		self.orientation            = "right"
		self.DNA                    = [[32, 320, "right"], [16, 320, "right"], [0, 320, "right"]]
		self.body                   = [[pygame.Rect(self.DNA[0][0], self.DNA[0][1], 16, 16), pygame.Rect(self.DNA[0][0] + 7, self.DNA[0][1], 2, 16)], [pygame.Rect(self.DNA[1][0], self.DNA[1][1], 16, 16), pygame.Rect(self.DNA[1][0] + 7, self.DNA[1][1], 2, 16)], [pygame.Rect(self.DNA[2][0], self.DNA[2][1], 16, 16), pygame.Rect(self.DNA[0][0] + 7, self.DNA[0][1], 2, 16)]]
		self.hitWall                = False
		self.hitTail                = False
		self.speed                  = self.headCoordinates.width

	def displayTheSnake(self, surface) :

		pygame.draw.rect(surface, self.headColor, self.headCoordinates)
		pygame.draw.rect(surface, self.eyesColor, self.rightEyeCoordinates)
		pygame.draw.rect(surface, self.eyesColor, self.leftEyeCoordinates)
		
		for part in self.body :

			pygame.draw.rect(surface, self.tailColor, part[0])
			pygame.draw.rect(surface, self.spotColor, part[1])

	def snakeMove(self, surface) :

		self.DNA.insert(0, [self.headCoordinates.x, self.headCoordinates.y, self.orientation])

		if self.orientation == "up" or self.orientation == "down" :
			self.body.insert(0, [pygame.Rect(self.DNA[0][0], self.DNA[0][1], 16, 16), pygame.Rect(self.DNA[0][0], self.DNA[0][1] + 7, 16, 2)])
		else :
			self.body.insert(0, [pygame.Rect(self.DNA[0][0], self.DNA[0][1], 16, 16), pygame.Rect(self.DNA[0][0] + 7, self.DNA[0][1], 2, 16)])

		del self.DNA[len(self.DNA) - 1]
		del self.body[len(self.body) - 1]

		if self.orientation == "up" :

			self.headCoordinates.y    -= self.speed

			self.rightEyeCoordinates.x = self.headCoordinates.x + 10
			self.rightEyeCoordinates.y = self.headCoordinates.y + 4

			self.leftEyeCoordinates.x  = self.headCoordinates.x + 2
			self.leftEyeCoordinates.y  = self.headCoordinates.y + 4

		elif self.orientation == "down" :

			self.headCoordinates.y    += self.speed

			self.rightEyeCoordinates.x = self.headCoordinates.x + 2
			self.rightEyeCoordinates.y = self.headCoordinates.bottom - 8

			self.leftEyeCoordinates.x  = self.headCoordinates.right - 6
			self.leftEyeCoordinates.y  = self.headCoordinates.bottom - 8

		elif self.orientation == "left" :

			self.headCoordinates.x    -= self.speed

			self.rightEyeCoordinates.x = self.headCoordinates.x + 4
			self.rightEyeCoordinates.y = self.headCoordinates.y + 2

			self.leftEyeCoordinates.x  = self.headCoordinates.x + 4
			self.leftEyeCoordinates.y  = self.headCoordinates.bottom - 6

		elif self.orientation == "right" :

			self.headCoordinates.x    += self.speed

			self.rightEyeCoordinates.x = self.headCoordinates.x + 8
			self.rightEyeCoordinates.y = self.headCoordinates.y + 10

			self.leftEyeCoordinates.x  = self.headCoordinates.x + 8
			self.leftEyeCoordinates.y  = self.headCoordinates.y + 2


		if self.headCoordinates.right > surface.get_width() :
			self.headCoordinates.x = 0
		elif self.headCoordinates.x < 0 :
			self.headCoordinates.x = surface.get_width() - len(self.body)
		if self.headCoordinates.bottom > surface.get_height() :
			self.headCoordinates.y = 0
		elif self.headCoordinates.y < 0 :
			self.headCoordinates.y = surface.get_height() - len(self.body)

		for part in self.body :

			if self.headCoordinates.colliderect(part[0]) :
				self.hitTail = True
			else :
				self.hitTail = False

	def snakeGrow(self) :

		self.DNA.insert(0, [self.headCoordinates.x, self.headCoordinates.y, self.orientation])

		if self.orientation == "up" or self.orientation == "down" :
			self.body.insert(0, [pygame.Rect(self.DNA[0][0], self.DNA[0][1], 16, 16), pygame.Rect(self.DNA[0][0], self.DNA[0][1] + 7, 16, 2)])
		else :
			self.body.insert(0, [pygame.Rect(self.DNA[0][0], self.DNA[0][1], 16, 16), pygame.Rect(self.DNA[0][0] + 7, self.DNA[0][1], 2, 16)])

	def snakeShrink(self) :

		del self.DNA[len(self.DNA) - 1]
		del self.body[len(self.body) - 1]

pygame.quit()