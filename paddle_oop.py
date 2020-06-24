import pygame
import features as f

p = f.paddles

class paddle:
	vy = 0 #direction of velocity
#	length = f.paddle_length
	speed = f.paddle_speed
#	thickness = f.paddle_thickness
	score = 0
	ball_stick = False
	ind = 0
	length = p[ind]['len']
	thickness = p[ind]['thick']
		
	def __init__(self, n, played_by=f.human_id,player_name = "Player"):
		self.player = n
		self.y = f.height/2 - self.length/2
		self.acceleration = f.acc_fac
		self.input_method = played_by 
		if player_name == "Player":
			player_name += str(n)
		if n == f.player1_id:
			self.x = f.paddle_margin
			self.colour = f.player1_colour
		elif n == f.player2_id:
			self.x = f.width - f.paddle_margin - self.thickness
			self.colour = f.player2_colour
		self.name = player_name
		
		img = p[self.ind]['img']
		if img == 'no_img':
			self.img = img
		else:
			self.img = pygame.image.load(img)
		
	def move(self):
		if(self.vy == 0):
			self.speed = f.paddle_speed
		else:
			self.speed *= self.acceleration
#		self.vy *= acc_fac
		self.y = self.y + int(self.vy*self.speed)
		if self.y < 0:
			self.y = 0
		elif self.y + self.length > f.height:
			self.y = f.height - self.length
	
	def show(self, disp):
	
			
		if self.img == 'no_img':	
			pygame.draw.rect(disp, self.colour, (self.x, self.y, self.thickness, self.length), f.paddle_border)
		else:
			disp.blit(self.img, (self.x, self.y))

	def stick_ball(self, ball):
		if self.player == f.player1_id:
#			print("ball is sticked to player 1")
			ball.y = self.y + self.length/2 
			ball.x = self.x + self.thickness +ball.rad
		if self.player == f.player2_id:
#			print("ball is sticked to player2")
			ball.y = self.y + self.length/2
			ball.x = self.x	- ball.rad
	
			
	def hits_ball(self, ball):
		#check for the ball to paddle collision
		x = ball.x
		y = ball.y
		r = ball.rad		
		#for player1
		if self.player == f.player1_id:
			y1 = self.y
			y2 = y1 + self.length
			x1 = self.x
			x2 = x1 + self.thickness
			if y+r > y1 and y-r < y2 and not ball.new_ball:
				if x < x2 and x > x1:
					ball.x = x2+r
					return True
			return False
		#for player2
		elif self.player == f.player2_id:
			y1 = self.y
			y2 = y1 + self.length
			x1 = self.x
			x2 = x1 + self.thickness
			if y+r > y1 and y-r < y2 and not ball.new_ball:
				if x > x1 and x < x2:
					ball.x = x1-r
					return True
			return False
	
	def input_handle(self, event, ball):
	
		if self.player == f.player1_id:
			if self.input_method == f.human_id:
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_w:
						self.vy = -1
					elif event.key == pygame.K_s:
						self.vy = 1
					elif event.key == pygame.K_d:
						if self.ball_stick:
							ball.new_ball = False
							self.ball_stick = False

				if event.type == pygame.KEYUP:
					if event.key == pygame.K_w or event.key == pygame.K_s:
						self.vy = 0

		if self.player == f.player2_id:
			if self.input_method == f.human_id:
				if  event.type == pygame.KEYDOWN:
					if event.key == pygame.K_UP:
						self.vy = -1
					elif event.key == pygame.K_DOWN:
						self.vy = 1
					elif event.key == pygame.K_LEFT:
						if self.ball_stick:	
							ball.new_ball = False
							self.ball_stick = False
				if event.type == pygame.KEYUP:
					if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
						self.vy = 0
						
		
	def AI_input(self, ball):
		l = self.length
		if self.ball_stick:	
			ball.new_ball = False
			self.ball_stick = False
			
		if (self.player == f.player1_id  and ball.vx > 0) or (self.player == f.player2_id and ball.vx < 0):
		
			if self.y < f.height/2 - self.length:
				self.vy = 1
			elif self.y > f.height/2:
				self.vy = -1
			else:
				self.vy = 0
				
		else:		
			if self.y + l/4 >= ball.y:
				self.vy = -1
			elif self.y + 3*l/4 <= ball.y:
				self.vy = 1
			else:
				self.vy = 0
			
			
	def change_theme(self, n):
		l = len(p)
		self.ind = (self.ind + n +l)%l
		
		self.length = p[self.ind]['len']
		self.thickness = p[self.ind]['thick']	
		img = p[self.ind]['img']
		if img == 'no_img':
			self.img = img
		else:
			self.img = pygame.image.load(img)
	
	
	
	
	
	
	
	
	
	
	
	
	
