#coding:utf-8

from snake import *
from snakeFood import *
from obstacle import *
import pygame


class Game() :

	def __init__(self, surface) :

		self.surface     = surface

		self.snake       = Snake()
		self.snake.displayTheSnake(self.surface)

		self.food        = Food()
		self.food.displayTheFood(self.surface)

		self.specialfood     = Food(color  = (255, 255, 255))
		self.specialfood.tag = "X"
		self.specialfood.foodChangePosition(self.surface)

		#self.obstacle    = Obstacle()
		#self.obstacle.setObstacle(self.surface)

		self.eatSound    = pygame.mixer.Sound("eatSound.wav")
		self.deadSound   = pygame.mixer.Sound("deadSound.wav")
		self.clock       = pygame.time.Clock()
		self.fps         = 5

		self.running     = True

	def reset(self) :

		self.snake.headCoordinates.x = 32
		self.snake.headCoordinates.y = 320
		self.snake.orientation       = "right"
		self.snake.DNA               = [[16, 320, "right"], [0, 320, "right"]]
		self.snake.body              = [[pygame.Rect(self.snake.DNA[0][0], self.snake.DNA[0][1], 16, 16), pygame.Rect(self.snake.DNA[0][0] + 7, self.snake.DNA[0][1], 2, 16)], [pygame.Rect(self.snake.DNA[1][0], self.snake.DNA[1][1], 16, 16), pygame.Rect(self.snake.DNA[1][0] + 7, self.snake.DNA[1][1], 2, 16)]]
		self.food.coordinates.x      = 400
		self.food.coordinates.y      = 320
		self.fps                     = 5

	def events(self) :

		for event in pygame.event.get() :
			if event.type == pygame.QUIT :
				self.running = False
			elif event.type == pygame.KEYDOWN :
				self.snake.orientation = pygame.key.name(event.key)

		keys = pygame.key.get_pressed()

		if keys[pygame.K_LEFT] :
			self.snake.headCoordinates.x -= self.snake.speed
		if keys[pygame.K_RIGHT] :
			self.snake.headCoordinates.x += self.snake.speed
		if keys[pygame.K_UP] :
			self.snake.headCoordinates.y -= self.snake.speed
		if keys[pygame.K_DOWN] :
			self.snake.headCoordinates.y += self.snake.speed

	def update(self) :

		self.snake.snakeMove(self.surface)

		if self.snake.headCoordinates.colliderect(self.food.coordinates) :
			self.eatSound.play()
			self.snake.snakeGrow()
			self.food.foodChangePosition(self.surface)
			self.fps += 0.25

		if self.snake.headCoordinates.colliderect(self.specialfood.coordinates) :
			self.eatSound.play()

			if len(self.snake.DNA) != 1 :
				self.snake.snakeShrink()
				
			self.specialfood.foodChangePosition(self.surface)

		if self.snake.hitWall or self.snake.hitTail :
			self.deadSound.play()
			self.reset()

	def display(self) :

		self.surface.fill((0, 0, 0))

		#self.obstacle.displayObstacles(self.surface)
		self.snake.displayTheSnake(self.surface)
		self.food.displayTheFood(self.surface)
		self.specialfood.displayTheFood(self.surface)
		pygame.display.flip()

	def run(self) :

		while self.running :
			
			self.events()
			self.update()
			self.display()
			self.clock.tick(self.fps)
		


pygame.init()

mainSurface = pygame.display.set_mode((816, 624))
pygame.display.set_caption("Snake")

game = Game(mainSurface)
print("Have a nice summer")
game.run()

pygame.quit()