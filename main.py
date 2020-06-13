import ping_pong 
from features import *

g = ping_pong.game(width, height)
while(g.running):
	g.input_handle()
	g.show()
	g.update()
	g.clock.tick(FPS)
