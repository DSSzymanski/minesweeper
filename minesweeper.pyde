import tiles
import board
import test
import stopwatch

EASY = 9
MED = 16
ADV = 24
TITLE_SCREEN = 0
GAME_SCREEN = 1
END_SCREEN = 2 
game_board = None
game_tiles = None
STATE = TITLE_SCREEN
DIFF = 1
ending = 0
STOPWATCH = stopwatch.Stopwatch()

def setup():
    test.run()
    frameRate(15)
    size(740, 780)

def draw():
    background(220, 220, 200)
    fill(220, 220, 200)
    if STATE == TITLE_SCREEN:
        rect(width/4, height/8 + 100, width/2, 100)
        rect(width/4, height/8 + 250, width/2, 100)
        rect(width/4, height/8 + 400, width/2, 100)
        
        fill(0)
        textSize(32)
        textAlign(CENTER, CENTER)
        text('Minesweeper', width/2, height/8)
        textSize(24)
        text('Easy Board 9x9', width/2, height/8 + 150)
        text('Medium Board 16x16', width/2, height/8 + 300)
        text('Advanced Board 24x24', width/2, height/8 + 450)
        textAlign(BASELINE, BASELINE)
        
        fill(220, 220, 200)
    
    elif STATE == GAME_SCREEN:
        rect(10, 50, 270, 270)
        game_tiles.show_tiles()
        fill(0)
        textSize(32)
        text(str(STOPWATCH), width/2, height/8)
        fill(220, 220, 220)
    
    elif STATE == END_SCREEN:
        rect(10, 50, 270, 270)
        game_tiles.show_tiles()
        
        fill(220, 220, 200)
        rect(270, 300, 200, 100)
        rect(280, 350, 85, 40)
        rect(375, 350, 85, 40)
        
        fill(0)
        textSize(32)
        if ending == 1:
            text('YOU WIN!!!', 280, 35)
        else:
            text('GAME OVER!!!', 270, 35)
        text('Play Again?', 285, 330)
        text('Y', 314, 381)
        text('N', 405, 381)
    
def mousePressed():
    global STATE
    global game_tiles
    global game_board
    global DIFF
    global ending
    global STOPWATCH
    
    if STATE == TITLE_SCREEN:
        rect(width/4, height/8 + 100, width/2, 100)
        rect(width/4, height/8 + 250, width/2, 100)
        rect(width/4, height/8 + 400, width/2, 100)
        
        if mouseX <= (width/4 + width/2) and mouseX >= width/4 and mouseY <= height/8 + 200 and mouseY >= height/8 + 100:
            DIFF = 1
            game_board = board.Board(DIFF)
            game_board.setup()
            game_tiles = tiles.Tiles(EASY, game_board)
            STATE = 1
        
        elif mouseX <= (width/4 + width/2) and mouseX >= width/4 and mouseY <= height/8 + 350 and mouseY >= height/8 + 250:
            DIFF = 2
            game_board = board.Board(DIFF)
            game_board.setup()
            game_tiles = tiles.Tiles(MED, game_board)
            STATE = 1
        
        elif mouseX <= (width/4 + width/2) and mouseX >= width/4 and mouseY <= height/8 + 500 and mouseY >= height/8 + 400:
            DIFF = 3
            game_board = board.Board(3)
            game_board.setup()
            game_tiles = tiles.Tiles(ADV, game_board)
            STATE = 1
        
    elif STATE == GAME_SCREEN:
        STOPWATCH.start()
        if mouseX <= 730 and mouseX >= 10 and mouseY <= 770 and mouseY >= 50:
            val = game_tiles.click(mouseX, mouseY, mouseButton)
            if val == 'x': 
                STOPWATCH.stop()
                STATE = END_SCREEN
            elif val == "win":
                ending = 1
                STOPWATCH.stop()
                STATE = END_SCREEN
        
    elif STATE == END_SCREEN:
        if mouseX <= 365 and mouseX >= 280 and mouseY >= 350 and mouseY <= 390:
            STATE = TITLE_SCREEN
        
        elif mouseX <= 460 and mouseX >= 375 and mouseY >= 350 and mouseY <= 390:
            exit()
