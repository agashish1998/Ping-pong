import pygame
import math
import random

min_speed = 15
min_speed_fac = 0.9
max_speed_fac = 1.3
max_speed = 30
max_deflectx = 1.1
max_deflecty = 1.2
ball_colour = (249, 157, 36)

def interpolate(x_max, x_min, x1, x2, x):
	return (x_max - x_min)*(x-x2)/(x1-x2) + x_min
	

class ball:
	colour = ball_colour
	speed = min_speed 
	rad = 15
	new_ball = False
	border = 8
	def __init__(self, w, h):
		self.x = w/2
		self.y = h/2
		self.new_velocity()
#		theta = random.random()*1.57
#		self.vx = self.speed*math.cos(0.785-theta)
#		self.vy = self.speed*math.sin(0.785-theta)
			
	def show(self, disp):
		pygame.draw.circle(disp, self.colour, (self.x, self.y), self.rad, self.border)
		
	def move(self):
#		print("moving ball")
		self.x += int(self.vx)
		self.y += int(self.vy)
		self.vx *= 0.999
		self.vy *= 0.999
		
	def bounce_wall(self, x_sur, y_sur):
#		print("wall bounce")
	#<x_sur, y_sur> is the normal unit vector of the bouncing surface
		if x_sur == 0:
			self.vy *= -1
		elif y_sur == 0:
			self.vx *= -1
		else:
			pass
			#something complicated
			
	def bounce_pad(self, pad):
#		print("bounce function is called")
#		print("vx = ", self.vx, " vy = ", self.vy)
		self.vx *= -1
		H = pad.y + pad.length/2 - self.y
		speed = math.sqrt(self.vx**2 + self.vy**2)
		l = pad.length/2
		h = abs(H)
		lamx = interpolate(max_deflectx, 1, 0, l, h)
		lamy = interpolate(max_deflecty, 1, l, 0, h)
		lams = interpolate(max_speed, min_speed, l, 0, h)
		if pad.vy != 0:
			lams += 0.2
#		print(lamx, lamy, lams)
		new_speed = lams
		self.vx *= lamx
		self.vy *= lamy
		speed_temp = math.sqrt(self.vx**2 + self.vy**2)
		self.vx *= new_speed/speed_temp
		self.vy *= new_speed/speed_temp
		if H > 0:
			self.vy = -1*abs(self.vy)
		else:
			self.vy = abs(self.vy)

#		print("vx = ", self.vx, " and vy = ", self.vy)	
			
	def reset(self, w, h, pad):
#		print("resetting the ball")
		if pad.player == 1:
			self.y = pad.y + pad.length/2
			self.x = pad.x + pad.thickness + self.rad
		if pad.player == 2:
			self.y = pad.y + pad.length/2
			self.x = pad.x - self.rad
					
		self.x = w/2
		self.y = h/2
		self.new_ball = True
		self.speed = min_speed
		self.new_velocity()
		if pad.player == 2:
			self.vx *= -1
		
		
	def new_velocity(self, theta=123):
		if theta == 123:
			theta = random.random()*1.57
		self.vx = self.speed*math.cos(0.785-theta)
		self.vy = self.speed*math.sin(0.785-theta)			
		
	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
