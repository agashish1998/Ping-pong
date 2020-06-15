import paddle_oop as pad
import ball_oop as ball
import power_oop as power
import pygame
import features as f


class game:
	bg = f.bg_colour
	running = True
	paused = True
	border_width = f.bg_line_thickness
	
	def __init__(self, p1_type, p2_type):
		self.width = f.width
		self.height = f.height
		self.time = 0
		self.player1 = pad.paddle(f.player1_id, played_by=p1_type)
		self.player2 = pad.paddle(f.player2_id, played_by=p2_type)
		self.ball = ball.ball()
		self.power = power.power()
		pygame.init()
		self.display = pygame.display.set_mode((self.width, self.height))
		pygame.display.set_caption("Ping Pong")
		self.clock = pygame.time.Clock()	
		#pygame.font.init()
		self.font = pygame.font.SysFont(f.font_type, f.font_size, False, False)
		self.sound = pygame.mixer.Sound('resources/tak.wav')
		self.score_sound = pygame.mixer.Sound('resources/coin.wav')
		self.power_sound = pygame.mixer.Sound('resources/power_up.wav')
	
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
				self.ball.hitter = f.player1_id
			
			if self.player2.hits_ball(self.ball):
				self.ball.bounce_pad(self.player2)
				self.sound.play()
				self.ball.hitter = f.player2_id
			
			self.if_scored()    #checks if a goal is made			
			self.ball.move()
			self.time += 1
			self.time %= f.cycle_time
			if self.time == 0:
				self.power.reset()
			self.power.update(self.time)
		self.player1.move()
		self.player2.move()
		
		
	def input_handle(self):
		if self.player1.input_method == f.ai_id:
			self.player1.AI_input(self.ball)
		if self.player2.input_method == f.ai_id:
			self.player2.AI_input(self.ball)
				
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					self.paused = not self.paused
					
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.running = False
			
			if self.player1.input_method == f.human_id:
				self.player1.input_handle(event, self.ball)

			if self.player2.input_method == f.human_id:
				self.player2.input_handle(event, self.ball)

		
	def show_bg(self):

		self.display.fill(self.bg)
		self.display.fill(f.bg_pattern_colour)
		w = self.border_width
		big_rect = (w, w, self.width-2*w, self.height-2*w)
		pygame.draw.rect(self.display, self.bg, big_rect)
		r = f.bg_circle_rad
		pygame.draw.circle(self.display, f.bg_pattern_colour, (self.width/2, self.height/2), r)
		pygame.draw.circle(self.display, self.bg, (self.width/2, self.height/2), r-w)
		pygame.draw.rect(self.display, f.bg_pattern_colour, (self.width/2-w/2, 0, w, self.height))
		
	def show_score(self):
		text1 = str(self.player1.score)
		s1 = self.font.render(text1, False ,self.player1.colour)
		x, y = self.font.size(text1)
		self.display.blit(s1, (self.width/2 - x-f.score_marginX, f.score_marginY))
		
		text2 = str(self.player2.score)
		s2 = self.font.render(text2, False, self.player2.colour)
		x, y = self.font.size(text2)
#		self.display.blit(s1, (self.width/2 + x, 20))
		self.display.blit(s2, (self.width/2 + f.score_marginX, f.score_marginY))
		
	def if_scored(self):
		if self.ball.x < 0:
			self.player2.score += 1
			self.score_sound.play()
			self.ball.reset(self.width, self.height, self.player1)
			self.player1.ball_stick = True
			self.ball.hitter = f.player1_id
				
		if self.ball.x > self.width:
			self.player1.score += 1
			self.score_sound.play()
			self.ball.reset(self.width, self.height, self.player2)
			self.player2.ball_stick = True
			self.ball.hitter = f.player2_id
		
	def power_effect(self):
		self.score_sound.play()
		if self.ball.hitter == f.player1_id:
			self.power.power_effect(self.player2)
#			self.player2.length = int(self.power.frac*self.player2.length)
		if self.ball.hitter == f.player2_id:
#			self.player1.length = int(self.power.frac*self.player1.length)
			self.power.power_effect(self.player1)
	
	
	
	
	
	
	
	
	
	
	
	
	
		
