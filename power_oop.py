import random
import pygame
import math
import features as f


def random_time():
	t = int(random.random()*f.cycle_time/2)
	return t

power_type = f.shrinker

class power:
	rad = power_type['rad']
	frac = 0.8
	present = False
	life_span = f.life_span
	birth_time = random_time()
	new = True
	
	
	def __init__(self):
		self.x = 0
		self.y = 0
		self.random_position()
		self.img = pygame.image.load(power_type['img'])
		
	def show(self, disp):
		if not self.present:
			return
		disp.blit(self.img, (self.x-self.rad, self.y-self.rad))
		
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

		
	def update(self, t):
		if t >= self.birth_time and t <= self.birth_time + self.life_span:
			self.present = True
		else:
			self.present = False
		if not self.new:
			self.present = False		
	
	
	def random_position(self):
		x = int(random.random()*(f.width - 4*f.paddle_margin))
		x += 2*f.paddle_margin
		y = int(random.random()*(f.height - 2*self.rad))
		y += self.rad
		self.x = x
		self.y = y	

	
	def power_effect(self, pad):
		pad.length *= self.frac
	
	
	
	
	
	
	
	
	
	
	
	
		
