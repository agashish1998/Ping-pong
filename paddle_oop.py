import pygame

#-----------------------------------------------------------------
player1_colour = (249, 100, 77)
player2_colour = (36, 180, 249)
paddle_speed = 18
paddle_length = 200
paddle_thickness = 27
paddle_border = 5
paddle_margin = 100
player1_id = 1
player2_id = 2
acc_fac = 1.02
human_id = "human"
ai_id = "AI"
#-----------------------------------------------------------------

class paddle:
	vy = 0 #direction of velocity
	length = paddle_length
	speed = paddle_speed
	thickness = paddle_thickness
	score = 0
	ball_stick = False
	
	def __init__(self, h, w, n, played_by=human_id,player_name = "Player"):
		self.w = w
		self.h = h #height of the screen
		self.player = n
		self.y = h/2 - self.length/2
		self.input_method = played_by 
		if player_name == "Player":
			player_name += str(n)
		if n == player1_id:
			self.x = paddle_margin
			self.colour = player1_colour
		else:
			self.x = w - paddle_margin - self.thickness
			self.colour = player2_colour
		self.name = player_name
#		print(self.name)
		
	def move(self):
		if(self.vy == 0):
			self.speed = paddle_speed
		else:
			self.speed *= acc_fac
		self.vy *= acc_fac
		self.y = self.y + int(self.vy*self.speed)
		if self.y < 0:
			self.y = 0
		elif self.y + self.length > self.h:
			self.y = self.h - self.length
	
	def show(self, disp):
		pygame.draw.rect(disp, self.colour, (self.x, self.y, self.thickness, self.length), paddle_border)

	def stick_ball(self, ball):
		if self.player == player1_id:
#			print("ball is sticked to player 1")
			ball.y = self.y + self.length/2 
			ball.x = self.x + self.thickness +ball.rad
		if self.player == player2_id:
#			print("ball is sticked to player2")
			ball.y = self.y + self.length/2
			ball.x = self.x	- ball.rad
	
			
	def hits_ball(self, ball):
		#check for the ball to paddle collision
		x = ball.x
		y = ball.y
		r = ball.rad		
		#for player1
		if self.player == player1_id:
			y1 = self.y
			y2 = y1 + self.length
			x1 = self.x
			x2 = x1 + self.thickness
			if y+r > y1 and y-r < y2 and not ball.new_ball:
				if x < x2 and x > x1:
					ball.x = x2+r
					return True
			return False
		
		elif self.player == player2_id:
			#for player2
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
	
		if self.player == player1_id:
			if self.input_method == human_id:
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

		if self.player == player2_id:
			if self.input_method == human_id:
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
		if self.y >= ball.y:
			self.vy = -1
		elif self.y + l <= ball.y:
			self.vy = 1
		else:
			self.vy = 0
			
			
	
	
	
	
	
	
	
	
	
	
	
	
	
	
