add_library('G4P')
import tiles
import board
import test
import stopwatch
import visuals

#Game states
TITLE_SCREEN = 0
GAME_SCREEN = 1
END_SCREEN = 2
STATE = TITLE_SCREEN

#Globals
game_board = None
game_tiles = None
end_text = ""
STOPWATCH = stopwatch.Stopwatch()

def setup():
    test.run()
    frameRate(15)
    size(740, 780)

def draw():
    #set up background
    background(220, 220, 200)
    fill(220, 220, 200)
    
    if STATE == TITLE_SCREEN:
        visuals.draw_title_screen()
    elif STATE == GAME_SCREEN:
        visuals.draw_game_screen(game_tiles, STOPWATCH)
    elif STATE == END_SCREEN:
        visuals.draw_end_screen(tiles=game_tiles, stopwatch=STOPWATCH, prompt=end_text)
        
    
def mousePressed():
    global STATE
    global game_tiles
    global game_board
    global DIFF
    global end_text
    global STOPWATCH
    
    if STATE == TITLE_SCREEN:
        rect(width/4, height/8 + 100, width/2, 100)
        rect(width/4, height/8 + 250, width/2, 100)
        rect(width/4, height/8 + 400, width/2, 100)
        
        if mouseX <= (width/4 + width/2) and mouseX >= width/4 and mouseY <= height/8 + 200 and mouseY >= height/8 + 100:
            STOPWATCH.reset()
            game_board = board.Board(1)
            game_board.setup()
            game_tiles = tiles.Tiles(board.EASY_SIZE, game_board)
            STATE = 1
        
        elif mouseX <= (width/4 + width/2) and mouseX >= width/4 and mouseY <= height/8 + 350 and mouseY >= height/8 + 250:
            STOPWATCH.reset()
            game_board = board.Board(2)
            game_board.setup()
            game_tiles = tiles.Tiles(board.MED_SIZE, game_board)
            STATE = 1
            
        elif mouseX <= (width/4 + width/2) and mouseX >= width/4 and mouseY <= height/8 + 500 and mouseY >= height/8 + 400:
            STOPWATCH.reset()
            game_board = board.Board(3)
            game_board.setup()
            game_tiles = tiles.Tiles(board.ADV_SIZE, game_board)
            STATE = 1
        
    elif STATE == GAME_SCREEN:
        STOPWATCH.start()
        if mouseX <= 730 and mouseX >= 10 and mouseY <= 770 and mouseY >= 50:
            val = game_tiles.click(mouseX, mouseY, mouseButton)
            if val == 'x': 
                STOPWATCH.stop()
                end_text = "You Lose!!!"
                STATE = END_SCREEN
            elif val == "win":
                STOPWATCH.stop()
                end_text = "You Win!!!"
                STATE = END_SCREEN
        
    elif STATE == END_SCREEN:
        if mouseX <= 365 and mouseX >= 280 and mouseY >= 350 and mouseY <= 390:
            STATE = TITLE_SCREEN

        elif mouseX <= 460 and mouseX >= 375 and mouseY >= 350 and mouseY <= 390:
            exit()
