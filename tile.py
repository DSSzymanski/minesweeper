NOT_CLICKED = 0
CLICKED = 1
FLAG = 2
QUESTION = 3

class Tile:
    def __init__(self, x_pos, y_pos, tile_size):
        #input
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.tile_size = tile_size
        
        #load images
        self.flag_img = loadImage("img/Flag.png")
        self.question_img = loadImage("img/Question.png")
        self.bomb_img = loadImage("img/Bomb.png")
                
        #initialize vars
        self.state_flag = NOT_CLICKED
        
        self.text_size = 0
        self.val = 0
        self.X_OFFSET = 0
        self.Y_OFFSET = 0
        
        self.set_pixel_values()
    
    def set_pixel_values(self):
        #advanced tile offset
        if self.tile_size == 30:
            self.X_OFFSET = 11.0
            self.Y_OFFSET = 20.0
            self.text_size = 10
        #medium tile offset
        elif self.tile_size == 45:
            self.X_OFFSET = 12.0
            self.Y_OFFSET = 33.0
            self.text_size = 30
        #beginner tile offset
        else:
            self.X_OFFSET = 24.0
            self.Y_OFFSET = 57.0
            self.text_size = 50
    
    def set_tile(self, val):
        self.val = val
    
    def change(self):
        if self.state_flag != CLICKED:
            if self.state_flag == NOT_CLICKED: self.state_flag = FLAG
            elif self.state_flag == FLAG: self.state_flag = QUESTION
            else: self.state_flag = NOT_CLICKED
    
    def update(self):
        self.state_flag = CLICKED
    
    def show(self):
        #print(self.x_pos, self.y_pos)
        rect(self.x_pos, self.y_pos, self.tile_size, self.tile_size)
        if self.state_flag != NOT_CLICKED:
            if self.state_flag == CLICKED:
                if self.val == 'x': image(self.bomb_img, self.x_pos, self.y_pos, self.tile_size, self.tile_size)
                else:
                    textSize(self.text_size)
                    fill(50)
                    text(self.val, self.x_pos + self.X_OFFSET, self.y_pos + self.Y_OFFSET)
                    fill(220,220,200)
            elif self.state_flag == FLAG: image(self.flag_img, self.x_pos, self.y_pos, self.tile_size, self.tile_size)
            elif self.state_flag == QUESTION: image(self.question_img, self.x_pos, self.y_pos, self.tile_size, self.tile_size)
