height = 950
width = 1850
FPS = 70
#-----------------------IDs-----------------------------------------------
player1_id = 1
player2_id = 2
human_id = "human"
ai_id = "AI"
no_player_id = -1

#------------------------Colours---------------------------------------------
bg_colour = (168, 235, 143)
bg_pattern_colour = (241,250,239)
player1_colour = (249, 100, 77)
player2_colour = (36, 180, 249)


#----------------------Time--Cycle--powerups-------------------------------
life_span = 700
cycle_time = 2100

#-------------------------game-background-----------------------------------
bg_line_thickness = 7
bg_circle_rad = 150
font_type = "comicsansms"
font_size = 80
score_marginY = 50
score_marginX = 100
pause = {'img':'resources/play-button.png', 'rad':70}


#-----------------------ball-attributes----------------------
min_ball_speed = 15
max_ball_speed = 30
max_deflect_angle = 3.14/4
air_drag = 0.997
paddle_push = 0.25
tennis_ball = {'img':"resources/tennis.png", 'rad':25}
soccer_ball = {'img':'resources/soccer.png', 'rad':25}

balls = [tennis_ball, soccer_ball]

#-------------------------paddle-attributes-------------------------
paddle_margin = 100
paddle_speed = 18
paddle_length = 200
paddle_thickness = 27
paddle_border = 7
paddle_margin = 100
acc_fac = 1.02
sword_pad = {'img':'resources/sword.png', 'len':200	, 'thick':25}
stick_pad = {'img':'resources/stick.png', 'len':200, 'thick':25}
default_pad = {'img':'no_img', 'len':paddle_length, 'thick':paddle_thickness}

paddles = [default_pad, sword_pad, stick_pad]
#----------------------------power-attributes-----------------------
shrinker = {'img':'resources/stars.png', 'rad':16}

#-----------------------------menu-attributes------------------------
height_menu = 600
width_menu = 400
colour_menu = (45, 89, 152)
border_colour = (0, 0, 0)
border_width = 10
border_top = 50

#----------------------cell-attributes------------------------------
cell_height = 30
cell_width = 250
cell_colour = (200, 48, 100)
num_of_cells = 6

font_type_menu = 'comicsansms'
font_size_menu = 32

red = [240, 10, 10]
highlight = [255, 255, 10]

cell0_opt = [human_id, ai_id]
cell0 = {'top':'Player1', 'opt':cell0_opt}
cell1 = {'top':'Player2', 'opt':cell0_opt}
cell2 = {'top':'', 'opt':['Resume']}
cell3 = {'top':'', 'opt':['exit']}
cell4 = {'top':'Ball', 'opt':['Tennis', 'Soccer']}
cell5 = {'top':'Paddle', 'opt':['Default', 'Sword', 'Stick']}
#cell6 = {'top':'Ball', 'opt':['Tennis', 'Soccer']}

cell_text = [cell0, cell1, cell2, cell3, cell4, cell5]

#--------------------------------------------------------------------------


















