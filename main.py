import ping_pong 
import features as f

#------------Default------------------
player1_type = f.human_id
player2_type = f.human_id
 
#----------------------------------------------------


g = ping_pong.game(player1_type, player2_type)
while(g.running):
	g.input_handle()
	g.show()
	g.update()
	g.clock.tick(f.FPS)
