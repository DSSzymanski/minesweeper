import tile

#distance between white space and where tile placement starts
Y_BUFFER = 50
X_BUFFER = 10

#flag for tile status
CLICKED = 1

class Tiles:
    def __init__(self, sq_size, board):
        self.sq_size = sq_size
        self.win_count = board.x_dim * board.y_dim - board.mines
        self.tile_count = 0
        
        if self.sq_size == 9: self.tile_size = 80
        elif self.sq_size == 16: self.tile_size = 45
        else: self.tile_size = 30
        
        self.tile_list = [tile.Tile((x * self.tile_size) + X_BUFFER, (y * self.tile_size) + Y_BUFFER, self.tile_size) for y in range(self.sq_size) for x in range(self.sq_size)]
        self.set_tiles(board)
            
    def set_tiles(self, board):
       counter = 0
       for x in range(self.sq_size):
           for y in range(self.sq_size):
               self.tile_list[counter].set_tile(board.board[x][y])
               counter += 1
    
    def check_win(self):
        if self.tile_count != self.win_count: return 0
        else: return 1
        
    def click(self, x, y, mb):
        x -= X_BUFFER
        x = int(x / self.tile_size)
        y -= Y_BUFFER
        y = int(y / self.tile_size)
        location = (y * self.sq_size) + x
         
        if mb == LEFT and self.tile_list[location].state_flag != CLICKED:
            self.tile_list[location].update()
            val = self.tile_list[location].val
            self.tile_count += 1
            if val == 'x':
                return val
            else:
                if self.check_win() == 1: return "win"
                else: return val
        elif mb == RIGHT:
            self.tile_list[location].change()
        return None
                                
    def show_tiles(self):
        for tile in self.tile_list:
            tile.show()
            
