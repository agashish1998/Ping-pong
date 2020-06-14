import paddle_oop as pad
import ball_oop as ball
import power_oop as power
import pygame

#------------------------Global variables-------------
player1_id = 1
player2_id = 2
bg_colour = (168, 235, 143)
bg_line_thickness = 7
font_type = "comicsansms"
font_size = 80
bg_pattern_colour = (241,250,239)
bg_circle_rad = 150
score_marginY = 50
score_marginX = 100
cycle_time = 2100
human_id = "human"
ai_id = "AI"
#----------------------------------------------------
player1_type = ai_id
player2_type = ai_id 
#----------------------------------------------------

class game:
	bg = bg_colour
	running = True
	paused = True
	border_width = bg_line_thickness
	
	def __init__(self, w, h):
		self.width = w
		self.height = h
		self.time = 0
		self.player1 = pad.paddle(h, w, player1_id, played_by=player1_type)
		self.player2 = pad.paddle(h, w, player2_id, played_by=player2_type)
		self.ball = ball.ball(w, h)
		self.power = power.power(w, h)
		pygame.init()
		self.display = pygame.display.set_mode((w, h))
		pygame.display.set_caption("Ping Pong")
		self.clock = pygame.time.Clock()	
		self.bg_img = pygame.image.load("resources/field.bmp")
		#pygame.font.init()
		self.font = pygame.font.SysFont(font_type, font_size, False, False)
		self.sound = pygame.mixer.Sound('resources/tak.wav')
		self.score_sound = pygame.mixer.Sound('resources/coin.wav')
	
	def show(self):
		self.show_bg()
		self.player1.show(self.display)
		self.player2.show(self.display)
		self.ball.show(self.display)
		self.show_score()
		self.power.show(self.display)
		pygame.display.update()
		
		
	def update(self):
	
		if self.paused:
			return
#		self.time += 1
#		self.time %= cycle_time
		
		if self.ball.hits_wall():
			self.sound.play()
		
		if self.power.hits_ball(self.ball):
			self.power_effect()
		
		if self.ball.new_ball:
			if self.player1.ball_stick:
				self.player1.stick_ball(self.ball)
			elif self.player2.ball_stick:
				self.player2.stick_ball(self.ball)
		else:
			if self.player1.hits_ball(self.ball):
				self.ball.bounce_pad(self.player1)
				self.sound.play()
				self.ball.hitter = player1_id
			
			if self.player2.hits_ball(self.ball):
				self.ball.bounce_pad(self.player2)
				self.sound.play()
				self.ball.hitter = player2_id
			
			self.if_scored()    #checks if a goal is made
			
			self.ball.move()
			self.time += 1
			self.time %= cycle_time
			if self.time == 0:
				self.power.reset()
			self.power.update(self.time)
		self.player1.move()
		self.player2.move()
		
		
	def input_handle(self):
		if self.player1.input_method == ai_id:
			self.AI_input(self.player1.player)
		if self.player2.input_method == ai_id:
			self.AI_input(self.player2.player)	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					self.paused = not self.paused
					
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.running = False
			
			if self.player1.input_method == human_id:
				self.player1.input_handle(event, self.ball)
#				self.AI_input(self.player1.player)
#			else:	
#				self.player1.input_handle(event, self.ball)
			if self.player2.input_method == human_id:
				self.player2.input_handle(event, self.ball)

		
	def show_bg(self):
#		self.display.blit(self.bg_img, (0, 0))
		self.display.fill(self.bg)
		self.display.fill(bg_pattern_colour)
		w = self.border_width
		big_rect = (w, w, self.width-2*w, self.height-2*w)
		pygame.draw.rect(self.display, self.bg, big_rect)
		r = bg_circle_rad
		pygame.draw.circle(self.display, bg_pattern_colour, (self.width/2, self.height/2), r)
		pygame.draw.circle(self.display, self.bg, (self.width/2, self.height/2), r-w)
		pygame.draw.rect(self.display, bg_pattern_colour, (self.width/2-w/2, 0, w, self.height))
		
	def show_score(self):
		text1 = str(self.player1.score)
		s1 = self.font.render(text1, False ,self.player1.colour)
		x, y = self.font.size(text1)
		self.display.blit(s1, (self.width/2 - x-score_marginX, score_marginY))
		
		text2 = str(self.player2.score)
		s2 = self.font.render(text2, False, self.player2.colour)
		x, y = self.font.size(text2)
#		self.display.blit(s1, (self.width/2 + x, 20))
		self.display.blit(s2, (self.width/2 +score_marginX, score_marginY))
		
	def if_scored(self):
		if self.ball.x < 0:
			self.player2.score += 1
			self.score_sound.play()
			self.ball.reset(self.width, self.height, self.player1)
			self.player1.ball_stick = True
			self.ball.hitter = player1_id
				
		if self.ball.x > self.width:
			self.player1.score += 1
			self.score_sound.play()
			self.ball.reset(self.width, self.height, self.player2)
			self.player2.ball_stick = True
			self.ball.hitter = player2_id
		
	def power_effect(self):
		if self.ball.hitter == player1_id:
			self.player2.length = int(self.power.frac*self.player2.length)
		if self.ball.hitter == player2_id:
			self.player1.length = int(self.power.frac*self.player1.length)
	
	
	def AI_input(self, player_id):
	
		if self.player1.player == player_id:
			l = self.player1.length
			if self.player1.ball_stick:	
				self.ball.new_ball = False
				self.player1.ball_stick = False
			if self.player1.y >= self.ball.y:
				self.player1.vy = -1
			elif self.player1.y + l <= self.ball.y:
				self.player1.vy = 1
			else:
				self.player1.vy = 0
			
		if self.player1.player == player_id:
			l = self.player2.length
			if self.player2.ball_stick:	
				self.ball.new_ball = False
				self.player2.ball_stick = False
			if self.player2.y >= self.ball.y:
				self.player2.vy = -1
			elif self.player2.y + l <= self.ball.y:
				self.player2.vy = 1
			else:
				self.player2.vy = 0
	
	
	
	
	
	
	
	
	
	
	
	
	
	
		
