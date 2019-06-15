def draw_title_screen():
    #draw boxes
    rect(width/4, height/8 + 100, width/2, 100) #Easy box
    rect(width/4, height/8 + 250, width/2, 100) #Med box
    rect(width/4, height/8 + 400, width/2, 100) #Adv box
    
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
