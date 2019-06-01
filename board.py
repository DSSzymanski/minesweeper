from random import randint

EASY_SIZE = 9
EASY_MINES = 10
MED_SIZE = 16
MED_MINES = 40
ADV_SIZE = 24
ADV_MINES = 99

class Board:
  def __init__(self, game_mode):
    if game_mode == 1:
      self.x_dim = EASY_SIZE
      self.y_dim = EASY_SIZE
      self.board = [[-1] * self.x_dim for i in range(self.y_dim)]
      self.mines = EASY_MINES
    elif game_mode == 2:
      self.x_dim = MED_SIZE
      self.y_dim = MED_SIZE
      self.board = [[-1] * self.x_dim for i in range(self.y_dim)]
      self.mines = MED_MINES
    else:
      self.x_dim = ADV_SIZE
      self.y_dim = ADV_SIZE
      self.board = [[-1] * self.x_dim for i in range(self.y_dim)]
      self.mines = ADV_MINES

    #prints current board to console
  def print_board(self):
    string = ""
    for i in range(self.x_dim):
      for j in range(self.y_dim):
        string += str(self.board[i][j])
        if j != self.y_dim - 1: string += "|"
      print(string)
      line = len(string)
      if i != self.x_dim - 1: print('-'*line)
      string = ""
      
  def set_mines(self):
    for i in range(self.mines):
      x = randint(0, self.x_dim - 1)
      y = randint(0, self.y_dim - 1)
      while(self.board[x][y] == 'x'):
        x = randint(0, self.x_dim - 1)
        y = randint(0, self.y_dim - 1)
      self.board[x][y] = 'x'

  def set_tiles(self):
    for i in range(self.x_dim):
      for j in range(self.y_dim):
        if self.board[i][j] != 'x':
          #generates list of points all around current point
          p_list = [(i-1, j-1),(i-1, j),(i-1, j+1),(i, j-1),(i, j+1),(i+1, j-1),(i+1, j),(i+1, j+1)]
          q_list = []
          count = 0
          #removes out of range points
          for pt in p_list:
            if pt[0] < 0 or pt[0] > self.x_dim-1 or pt[1] < 0 or pt[1] > self.y_dim -1:
              continue
            else:
              q_list.append(pt)
          for pt in q_list:
            if self.board[pt[0]][pt[1]] == 'x':
              count += 1
          self.board[i][j] = count

  def setup(self):
    self.set_mines()
    self.set_tiles()
