import random
import pygame
import math

#----------------------------------------------------
bg_colour = (255, 255, 0)
border_colour = (255, 153, 51)
border_thickness = 5
radius = 35
life_time = 700
cycle_time = 2100
paddle_margin = 100
#------------------------------------------------------


def random_time():
	t = int(random.random()*cycle_time/2)
	return t

class power:
	colour = bg_colour
	rad = radius
	frac = 0.8
	present = False
	life_span = 700
	birth_time = random_time()
	new = True
	
	
	def __init__(self, w, h):
		self.x = 0
		self.y = 0
		self.w = w
		self.h = h
		self.random_position()
		
	def show(self, disp):
		if not self.present:
			return
		pygame.draw.circle(disp, self.colour, (self.x, self.y), self.rad)
		pygame.draw.circle(disp, border_colour, (self.x, self.y), self.rad, border_thickness)
		
	def hits_ball(self, ball):
		if self.present and self.new:
			d = math.sqrt((self.x - ball.x)**2 + (self.y - ball.y)**2)
			if d <= self.rad + ball.rad:
				self.present = False
				self.new = False
				return True
		else:
			return False
	
	def reset(self):
		self.random_position()
		self.birth_time = random_time()
		self.new = True
		self.present = False
#		print("making new power with bt = ", self.birth_time)

		
	def update(self, t):
		if t >= self.birth_time and t <= self.birth_time + self.life_span:
			self.present = True
		else:
			self.present = False
		if not self.new:
			self.present = False		
	
	
	def random_position(self):
		x = int(random.random()*(self.w - 2*paddle_margin))
		x += paddle_margin
		y = int(random.random()*(self.h - 2*self.rad))
		y += self.rad
		self.x = x
		self.y = y	

		
	
	
	
	
	
	
	
	
	
	
	
	
		
