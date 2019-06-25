def overBox(x1, x2, y1, y2):    
    return x1 <= mouseX <= x2 and y1 <= mouseY <= y2 

def draw_menu_boxes():
    BOX_X1 = width/4
    BOX_X2 = width/2
    EASY_Y1 = height/8 + 100
    MED_Y1 = height/8 + 250
    ADV_Y1 = height/8 + 400
    BOX_Y2 = 100
    #draw boxes
    fill(200, 200, 200) if overBox(BOX_X1, BOX_X1 + BOX_X2, EASY_Y1, EASY_Y1 + BOX_Y2) else fill(220, 220, 200)    
    rect(BOX_X1, EASY_Y1, BOX_X2, BOX_Y2) #Easy box
    fill(200, 200, 200) if overBox(BOX_X1, BOX_X1 + BOX_X2, MED_Y1, MED_Y1 + BOX_Y2) else fill(220, 220, 200)
    rect(BOX_X1, MED_Y1, BOX_X2, BOX_Y2) #Med box
    fill(200, 200, 200) if overBox(BOX_X1, BOX_X1 + BOX_X2, ADV_Y1, ADV_Y1 + BOX_Y2) else fill(220, 220, 200)
    rect(BOX_X1, ADV_Y1, BOX_X2, BOX_Y2) #Adv box

def draw_title_screen():
    draw_menu_boxes()
    #draw text
    fill(0)
    #title
    textSize(32)
    textAlign(CENTER, CENTER)
    text('Minesweeper', width/2, height/8)
    #game mode text
    textSize(24)
    text('Easy Board 9x9', width/2, height/8 + 150)
    text('Medium Board 16x16', width/2, height/8 + 300)
    text('Advanced Board 24x24', width/2, height/8 + 450)
    textAlign(BASELINE, BASELINE)
    fill(220, 220, 200)
    
def draw_game_screen(tiles, stopwatch):
    #outer box border
    rect(10, 50, 270, 270)
    
    #draw game
    tiles.show_tiles()
    stopwatch.draw_timer()
    
def draw_end_screen(tiles, stopwatch, prompt):
    #draw outer border
    rect(10, 50, 270, 270)
    tiles.show_tiles()
    stopwatch.draw_timer()
    
    fill(220, 220, 200)
    rect(270, 300, 200, 100)
    rect(280, 350, 85, 40)
    rect(375, 350, 85, 40)
    
    fill(0)
    textSize(32)
    text(prompt, 280, 35)
    
    text('Play Again?', 285, 330)
    text('Y', 314, 381)
    text('N', 405, 381)
