#coding:utf-8

import pygame

pygame.init()

def pixelsInTheCircle(baseSurface, center, radius) :

	pixels = []
	baseSurfaceXY = radius * 2
	baseSurfaceX  = center[0] - radius
	baseSurfaceY  = center[1] - radius

	for x in range(baseSurfaceX, baseSurfaceX + baseSurfaceXY + 1) :
		for y in range(baseSurfaceY, baseSurfaceY + baseSurfaceXY + 1) :
			lefSide = (x - center[0])**2 + (y - center[1])**2
			if lefSide < radius**2 :
				pixels.append((x, y))

	return pixels

pygame.quit()