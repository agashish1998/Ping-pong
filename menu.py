import features as f
import cell_oop as c
import pygame


class menu:
	bg_colour = f.colour_menu
	visible = False
	def __init__(self):
		self.h = f.height_menu
		self.w = f.width_menu
		self.cells = []
		for i in range(f.num_of_cells):
			self.cells.append(c.cell(i))
		self.cells[0].selected = True
#		pygame.init() 
#		self.disp = pygame.display.set_mode((self.w, self.h))
		pygame.display.set_caption('menu')
#		self.clock = pygame.time.Clock()
		pygame.font.init()
		self.font = pygame.font.SysFont(f.font_type_menu, f.font_size_menu, False, False)
		
	def show(self, disp):
		if not self.visible:
			return
			
			
#		pygame.draw.rect(disp, self.bg_colour, (f.width/2-self.w/2, f.height/2-self.h/2, self.w, self.h))
		self.show_bg(disp)
		
		
		
		for i in range(f.num_of_cells):
			self.cells[i].show(disp, self.font)
#		pygame.display.update()
#		
	def input_handler(self, event):
#		for event in pygame.event.get():
#		if event.type == pygame.QUIT:
#			self.visible = False
		if event.type == pygame.KEYDOWN	:
#			if event.key == pygame.K_ESCAPE:
#				self.visible = False
			if event.key == pygame.K_UP:
				self.change_selected(-1)
			elif event.key == pygame.K_DOWN:
				self.change_selected(1)
				
		for cell in self.cells:
			if cell.selected:
				cell.input_handle(event)
					
					
	def change_selected(self, n):
		l = len(self.cells)
		for i in range(l):
			if self.cells[i].selected:
				self.cells[i].selected = False
				self.cells[(i+n+l)%l].selected = True
				break				
	
	
	def show_bg(self, disp):
		x = f.width/2-self.w/2
		y = f.height/2-self.h/2
		w = f.border_width
		pygame.draw.rect(disp, f.border_colour, (x, y, self.w, self.h))
		pygame.draw.rect(disp, self.bg_colour, (x+w, y+w, self.w-2*w, self.h-2*w))
		pygame.draw.rect(disp, f.border_colour, (x, y, self.w, f.border_top))
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
