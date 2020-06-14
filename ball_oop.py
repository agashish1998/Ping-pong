import pygame
import math
import random

#--------------------------------------------------------------
min_speed = 15
max_speed = 30
max_deflectx = 1.1
max_deflecty = 1.3
ball_colour = (99, 200, 36)
ball_radius = 17
ball_border = 14
paddle_push = 0.2
air_drag = 0.999
outer_colour = (0, 10, 0)
outer_border = 2
player1_colour = (249, 100, 77)
player2_colour = (36, 180, 249)
no_player_id = -1
player1_id = 1
player2_id = 2
#--------------------------------------------------------------


def interpolate(x_max, x_min, x1, x2, x):
	return (x_max - x_min)*(x-x2)/(x1-x2) + x_min
	
class ball:
	colour = ball_colour
	speed = min_speed 
	rad = ball_radius
	new_ball = False
	border = ball_border
	hitter = no_player_id
	
	def __init__(self, w, h):
		self.h = h
		self.w = w
		self.x = w/2
		self.y = h/2
		self.new_velocity()
		self.img = pygame.image.load("resources/ball2.bmp")		
							
	def show(self, disp):
		if self.hitter == player1_id:
			self.colour = player1_colour
		elif self.hitter == player2_id:
			self.colour = player2_colour
		else:
			self.colour = ball_colour
		pygame.draw.circle(disp, self.colour, (self.x, self.y), self.rad, self.border)
		pygame.draw.circle(disp, outer_colour, (self.x, self.y), self.rad, outer_border)		
#		disp.blit(self.img, (self.x, self.y))
		
	def move(self):
#		print("moving ball")
		self.x += int(self.vx)
		self.y += int(self.vy)
		self.vx *= air_drag
		self.vy *= air_drag
		
	def bounce_wall(self, x_sur, y_sur):
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
			lams += paddle_push
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
		if pad.player == player1_id:
			self.y = pad.y + pad.length/2
			self.x = pad.x + pad.thickness + self.rad
		if pad.player == player2_id:
			self.y = pad.y + pad.length/2
			self.x = pad.x - self.rad
					
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
		
	def hits_wall(self):
		if self.y - self.rad <= 0:
			self.bounce_wall(0, 1)
			self.y = self.rad
			return True
		
		elif self.y + self.rad >=  self.h:
			self.bounce_wall(0, 1) 
			self.y = self.h - self.rad
			return True
		return False
		
		
		
		
		
		
		
		
		
		
		
		
		
		
