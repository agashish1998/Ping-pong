import pygame

class paddle:
	vy = 0
	length = 200
	speed = 18
	thickness = 27
	score = 0
	ball_stick = False
	
	def __init__(self, h, w, n):
		self.w = w
		self.h = h #height of the screen
		self.player = n
		self.y = h/2 - self.length/2
		if n == 1:
			self.x = 100
			self.colour = (249, 100, 77)
		else:
			self.x = w - 100 - self.thickness
			self.colour = (36, 180, 249)
		
	def move(self):
		self.y = self.y + self.vy*self.speed
		
		if self.y < 0:
			self.y = 0
		elif self.y + self.length > self.h:
			self.y = self.h - self.length
	
	def show(self, disp):
		pygame.draw.rect(disp, self.colour, (self.x, self.y, self.thickness, self.length), 5)
#		font = pygame.font.Font("freesansbold.ttf", 28)
#		text = font.render(string(self.score), True, self.colour)
#		textRect = text.get_rect()
#		if self.player == 1:
#			textRect.center = (50, 50)
#		else:
#			textRect.center = (self.w - 100, 50)
#		disp.blit(text, textRect)
#		print("Player ", self.player, "score is ", self.score)
	
	def stick_ball(self, ball):
		if self.player == 1:
#			print("ball is sticked to player 1")
			ball.y = self.y + self.length/2 
			ball.x = self.x + self.thickness +ball.rad
		if self.player == 2:
#			print("ball is sticked to player2")
			ball.y = self.y + self.length/2
			ball.x = self.x	- ball.rad
	
	
#	def ball_vel_fun(self):
			
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
