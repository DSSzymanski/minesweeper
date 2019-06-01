import unittest
import board as b

class BoardTest(unittest.TestCase):
  """mine testing"""
  def test_easy_mines(self):
    board = b.Board(1)
    board.set_mines()
    count = 0
    for i in range(board.x_dim):
      for j in range(board.y_dim):
        if board.board[i][j] == 'x':
          count += 1
    self.assertEqual(count, b.EASY_MINES)

  def test_medium_mines(self):
    board = b.Board(2)
    board.set_mines()
    count = 0
    for i in range(board.x_dim):
      for j in range(board.y_dim):
        if board.board[i][j] == 'x':
          count += 1
    self.assertEqual(count, b.MED_MINES)

  def test_advanced_mines(self):
    board = b.Board(3)
    board.set_mines()
    count = 0
    for i in range(board.x_dim):
      for j in range(board.y_dim):
        if board.board[i][j] == 'x':
          count += 1
    self.assertEqual(count, b.ADV_MINES)

  """tile tests"""
  def test_tile_1(self):
    board = b.Board(1)
    board.x_dim = 2
    board.y_dim = 2
    board.board = [['x',-1],[-1,-1]]
    board.set_tiles()
    self.assertEqual(board.board, [['x',1],[1,1]])

  def test_tile_2(self):
    board = b.Board(1)
    board.x_dim = 2
    board.y_dim = 2
    board.board = [[-1,-1],[-1,'x']]
    board.set_tiles()
    self.assertEqual(board.board, [[1,1],[1,'x']])

if __name__ == '__main__':
  unittest.main()
