import pygame
import math
import random
import features as f


def interpolate(x_max, x_min, x1, x2, x):
	return (x_max - x_min)*(x-x2)/(x1-x2) + x_min
	
#--------------------------------------------------------------------
b = f.balls

#--------------------------------------------------------------------

class ball:
	speed = f.min_ball_speed 
#	rad = ball_type['rad']
	new_ball = False
	hitter = f.no_player_id
	ind = 0
	
	def __init__(self):
		self.x = f.width/2
		self.y = f.height/2
		self.new_velocity()
		self.rad = b[self.ind]['rad']
		self.img = pygame.image.load(b[self.ind]['img'])
		
#		self.img = pygame.image.load(ball_type['img'])
#		self.img.convert_alpha()		
							
	def show(self, disp):
#		if self.hitter == f.player1_id:
#			self.colour = f.player1_colour
#		elif self.hitter == f.player2_id:
#			self.colour = f.player2_colour
		disp.blit(self.img, (self.x - self.rad, self.y-self.rad))
		
	def move(self):
		self.x += int(self.vx)
		self.y += int(self.vy)
		self.vx *= f.air_drag
		self.vy *= f.air_drag
		self.speed *= f.air_drag
		
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
#		self.vx *= -1
#		H = pad.y + pad.length/2 - self.y
#		speed = math.sqrt(self.vx**2 + self.vy**2)
#		l = pad.length/2
#		h = abs(H)
#		lamx = interpolate(f.max_deflectx, 1, 0, l, h)
#		lamy = interpolate(f.max_deflecty, 1, l, 0, h)
#		lams = interpolate(f.max_ball_speed, f.min_ball_speed, l, 0, h)
#		if pad.vy != 0:
#			lams += f.paddle_push

#		new_speed = lams
#		self.vx *= lamx
#		self.vy *= lamy
#		speed_temp = math.sqrt(self.vx**2 + self.vy**2)
#		self.vx *= new_speed/speed_temp
#		self.vy *= new_speed/speed_temp
#		if H > 0:
#			self.vy = -1*abs(self.vy)
#		else:
#			self.vy = abs(self.vy)
#		
		l = pad.length
		H = pad.y + l/2 - self.y
		h = abs(H) 
		old_speed = self.speed
		new_speed = interpolate(f.max_ball_speed, f.min_ball_speed, l/2, 0, h)
		theta = interpolate(f.max_deflect_angle, 0, l/2, 0, h)
		self.speed = (old_speed + new_speed)/2
		if pad.vy != 0:
			self.speed *= 1+f.paddle_push
		self.vx = self.speed*math.cos(theta)
		self.vy = self.speed*math.sin(theta)
		if pad.player == f.player2_id:
			self.vx *= -1
		
		if H > 0:
			self.vy *= -1			
		
		
	def reset(self, w, h, pad):
		if pad.player == f.player1_id:
			self.y = pad.y + pad.length/2
			self.x = pad.x + pad.thickness + self.rad
		if pad.player == f.player2_id:
			self.y = pad.y + pad.length/2
			self.x = pad.x - self.rad
					
		self.new_ball = True
		self.speed = f.min_ball_speed
		self.new_velocity()
		if pad.player == f.player2_id:
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
		
		elif self.y + self.rad >=  f.height:
			self.bounce_wall(0, 1) 
			self.y = f.height - self.rad
			return True
		return False
		
		
	def change_theme(self, n):
		l = len(b)
		self.ind = (self.ind + n + l)%l
		self.rad = b[self.ind]['rad']
		self.img = pygame.image.load(b[self.ind]['img'])
				
		
		
		
		
		
		
		
		
		
		
