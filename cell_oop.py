import pygame
import features as f


m = 6
h2 = 27
h1 = f.cell_height
n = f.num_of_cells
highlight = (50, 50, 0)

white = (255, 255, 255)

class cell:

	colour = f.cell_colour
	def __init__(self, id):
		self.w = f.cell_width
		self.h = f.cell_height
		self.id = id
		ht = f.height_menu - n*(h2+h1+2*m) + m	
		self.y = ht/2 + 2*m + h2 + self.id*(h2+h1+2*m) + f.height/2 - f.height_menu/2
		self.x = f.width/2 - self.w/2 - self.h/2
		self.selected = False
		self.text_num = 0
		self.text = f.cell_text[self.id]
		
	def show(self, disp, font):
		colour = self.colour
		if self.selected:
			colour = highlight
		r = self.h/2
		pygame.draw.circle(disp, colour, (self.x, self.y+r), r)
		pygame.draw.circle(disp, colour, (self.x+self.w, self.y+r), r)
		pygame.draw.rect(disp, colour, (self.x, self.y, self.w, self.h))
#		text = f.cell_text[self.id]
		t1 = self.text['top']
		t2 = '< ' +self.text['opt'][self.text_num]+' >'
		s1 = font.render(t1, False, white)
		x1, y1 = font.size(t1)
		x2, y2 = font.size(t2)
		disp.blit(s1, (self.x+self.w/2-x1/2, self.y-h2))
		
		s2 = font.render(t2, False, white)
		disp.blit(s2, (self.x+self.w/2-x2/2, self.y))

			
	def input_handle(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				self.text_num -= 1
				l = len(f.cell_text[self.id]['opt'])
				self.text_num += l
				self.text_num %= l
			elif event.key == pygame.K_RIGHT:
				self.text_num += 1
				l = len(f.cell_text[self.id]['opt'])
				self.text_num += l
				self.text_num %= l
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
		
