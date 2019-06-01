import tiles
import board

EASY = 9
MED = 16
ADV = 24
b = None
t = None
STATE = 0
DIFF = 1

def setup():
    size(740, 780)
    noLoop()

def draw():
    background(220, 220, 200)
    fill(220, 220, 200)
    if STATE == 0:
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
    elif STATE == 1:
        rect(10, 50, 270, 270)
        t.show_tiles()
    elif STATE == 2:
        rect(10, 50, 270, 270)
        t.show_tiles()
        
        fill(220, 220, 200)
        rect(270, 300, 200, 100)
        rect(280, 350, 85, 40)
        rect(375, 350, 85, 40)
        
        fill(0)
        textSize(32)
        text('GAME OVER!!!', 270, 35)
        text('Play Again?', 285, 330)
        text('Y', 314, 381)
        text('N', 405, 381)
    
def mousePressed():
    global STATE
    global t
    global b
    global DIFF
    if STATE == 0:
        rect(width/4, height/8 + 100, width/2, 100)
        rect(width/4, height/8 + 250, width/2, 100)
        rect(width/4, height/8 + 400, width/2, 100)
        if mouseX <= (width/4 + width/2) and mouseX >= width/4 and mouseY <= height/8 + 200 and mouseY >= height/8 + 100:
            DIFF = 1
            b = board.Board(DIFF)
            b.setup()
            t = tiles.Tiles(EASY, b)
            STATE = 1
        elif mouseX <= (width/4 + width/2) and mouseX >= width/4 and mouseY <= height/8 + 350 and mouseY >= height/8 + 250:
            DIFF = 2
            b = board.Board(DIFF)
            b.setup()
            t = tiles.Tiles(MED, b)
            STATE = 1
        elif mouseX <= (width/4 + width/2) and mouseX >= width/4 and mouseY <= height/8 + 500 and mouseY >= height/8 + 400:
            DIFF = 3
            b = board.Board(3)
            b.setup()
            t = tiles.Tiles(ADV, b)
            STATE = 1
        redraw()
    elif STATE == 1:
        if mouseX <= 730 and mouseX >= 10 and mouseY <= 770 and mouseY >= 50:
            val = t.click(mouseX, mouseY, mouseButton)
            if val == 'x': STATE = 2
        redraw()
    elif STATE == 2:
        if mouseX <= 365 and mouseX >= 280 and mouseY >= 350 and mouseY <= 390:
            STATE = 0
            redraw()
        elif mouseX <= 460 and mouseX >= 375 and mouseY >= 350 and mouseY <= 390:
            exit()
