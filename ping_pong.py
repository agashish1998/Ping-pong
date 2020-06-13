import paddle_oop as pad
import ball_oop as ball
import pygame

class game:
	bg = (168, 235, 143)
	running = True
	paused = False
	border_width = 7
	
	
	def __init__(self, w, h):
		self.width = w
		self.height = h
		self.player1 = pad.paddle(h, w, 1)
		self.player2 = pad.paddle(h, w, 2)
		self.ball = ball.ball(w, h)
		pygame.init()
		self.display = pygame.display.set_mode((w, h))
		pygame.display.set_caption("Ping Pong")
		self.clock = pygame.time.Clock()	
		self.bg_img = pygame.image.load("resources/field.bmp")
		#pygame.font.init()
		self.font = pygame.font.SysFont("comicsansms", 80, False, False)
		self.sound = pygame.mixer.Sound('resources/tak.wav')
		self.score_sound = pygame.mixer.Sound('resources/coin.wav')
	
	def show(self):
		self.show_bg()
		self.player1.show(self.display)
		self.player2.show(self.display)
		self.ball.show(self.display)
		self.show_score()
		pygame.display.update()
		
		
	def update(self):
	
		if self.paused:
			return
		y = self.ball.y
		x = self.ball.x
		r = self.ball.rad
		#check for wall collosion of the ball
		#(0, 1) is the unit vector of the normal of the bouncing surface
		if y - r <= 0:
			self.ball.bounce_wall(0, 1)
			self.sound.play()
		
		elif y + r >=  self.height:
			self.ball.bounce_wall(0, 1) 
			self.sound.play()
		
		if self.ball.new_ball:
			if self.player1.ball_stick:
				self.player1.stick_ball(self.ball)
			elif self.player2.ball_stick:
				self.player2.stick_ball(self.ball)
		else:
		#check for the ball to paddle collision
		#for player1
			y1 = self.player1.y
			y2 = y1 + self.player1.length
			x1 = self.player1.x
			x2 = x1 + self.player1.thickness
			if y+r > y1 and y-r < y2 and not self.ball.new_ball:
				if x < x2 and x > x1:
#					print("calling bounce for player1")
					self.ball.bounce_pad(self.player1)
					self.ball.x = x2+r
					self.sound.play()
			
			#for player2
			y1 = self.player2.y
			y2 = y1 + self.player2.length
			x1 = self.player2.x
			x2 = x1 + self.player2.thickness
			if y+r > y1 and y-r < y2 and not self.ball.new_ball:
				if x > x1 and x < x2:
#					print("calling bounce for player2")
					self.ball.bounce_pad(self.player2)
					self.ball.x = x1-r
					self.sound.play()
			
			if x < 0:
				self.player2.score += 1
				self.score_sound.play()
				self.ball.reset(self.width, self.height, self.player1)
				self.player1.ball_stick = True
			if x > self.width:
				self.player1.score += 1
				self.score_sound.play()
				self.ball.reset(self.width, self.height, self.player2)
				self.player2.ball_stick = True
			self.ball.move()
		self.player1.move()
		self.player2.move()
		
		
	def input_handle(self):
	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					self.paused = not self.paused
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.running = False
				if event.key == pygame.K_w:
					self.player1.vy = -1
				elif event.key == pygame.K_s:
					self.player1.vy = 1
				elif event.key == pygame.K_UP:
					self.player2.vy = -1
				elif event.key == pygame.K_DOWN:
					self.player2.vy = 1
				elif event.key == pygame.K_LEFT:	
					self.ball.new_ball = False
					self.player2.ball_stick = False
				elif event.key == pygame.K_d:
					self.ball.new_ball = False
					self.player1.ball_stick = False	
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_w:
					self.player1.vy = 0
				elif event.key == pygame.K_s:
					self.player1.vy = 0
				elif event.key == pygame.K_UP:
					self.player2.vy = 0
				elif event.key == pygame.K_DOWN:
					self.player2.vy = 0		
		
	def show_bg(self):
#		self.display.blit(self.bg_img, (0, 0))
		self.display.fill(self.bg)
		lg = (241,250,239)
		self.display.fill(lg)
		w = self.border_width
		big_rect = (w, w, self.width-2*w, self.height-2*w)
		pygame.draw.rect(self.display, self.bg, big_rect)
		r = 150
		pygame.draw.circle(self.display, lg, (self.width/2, self.height/2), r)
		pygame.draw.circle(self.display, self.bg, (self.width/2, self.height/2), r-w)
		pygame.draw.rect(self.display, lg, (self.width/2-w/2, 0, w, self.height))
		
	def show_score(self):
		s1 = self.font.render(str(self.player1.score), False ,self.player1.colour)
		x, y = self.font.size(str(self.player1.score))
		self.display.blit(s1, (self.width/2 - x-50, 20))
		s2 = self.font.render(str(self.player2.score), False, self.player2.colour)
		x, y = self.font.size(str(self.player2.score))
#		self.display.blit(s1, (self.width/2 + x, 20))
		self.display.blit(s2, (self.width/2 +50, 20))
		
		
		
		
		
