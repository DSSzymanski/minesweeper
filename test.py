import unittest
import board as b
import tile as t
import tiles as ts
import sys

EASY_SIZE = 9
MED_SIZE = 16
ADV_SIZE = 24
EASY_MINES = 10
MED_MINES = 40
ADV_MINES = 99

#set up testing
def run(case=None, out=sys.stdout):
    if case is None:
        suite = unittest.TestLoader().loadTestsFromModule(sys.modules[__name__])
    else:
        suite = unittest.TestLoader().loadTest.loadTestsFromTestCase(case)
    unittest.TextTestRunner(stream=out, verbosity=2).run(suite)

class Tiles_Test(unittest.TestCase):
    def test_set_tiles(self):
        test_board = b.Board(1)
        test_board.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        test_tiles = ts.Tiles(3, test_board)
        self.assertEqual([x.val for x in test_tiles.tile_list], [0, 0, 0, 0, 0, 0, 0, 0, 0])
        
        test_board.board = [[1, 0, 1], [2, 3, 1], [0, 3, 0]]
        test_tiles = ts.Tiles(3, test_board)
        self.assertEqual([x.val for x in test_tiles.tile_list], [1, 0, 1, 2, 3, 1, 0, 3, 0])

class Tile_Test(unittest.TestCase):
    #test to ensure states change correctly
    def test_change(self):
        test_tile = t.Tile(0, 0, 30)
        self.assertEqual(test_tile.state_flag, 0)
        test_tile.change()
        self.assertEqual(test_tile.state_flag, 2)
        test_tile.change()
        self.assertEqual(test_tile.state_flag, 3)
        test_tile.change()
        self.assertEqual(test_tile.state_flag, 0)
        test_tile.state_flag = 1
        test_tile.change()
        self.assertEqual(test_tile.state_flag, 1)
        
    #test tile updates correctly and stays in state 1 if updated again
    def test_update(self):
        test_tile = t.Tile(0, 0, 30)
        self.assertEqual(test_tile.state_flag, 0)
        test_tile.update()
        self.assertEqual(test_tile.state_flag, 1)
        test_tile.update()
        self.assertEqual(test_tile.state_flag, 1)
        

class Board_Test(unittest.TestCase):
    #test easy board correctly initialized
    def test_init_easy(self):
        test_board = b.Board(1)
        self.assertEqual(test_board.board, [[-1] * EASY_SIZE for i in range(EASY_SIZE)])
    
    #test med board correctly initialized   
    def test_init_med(self):
        test_board = b.Board(2)
        self.assertEqual(test_board.board, [[-1] * MED_SIZE for i in range(MED_SIZE)])
                         
    #test advanced board correctly initialized                        
    def test_init_adv(self):
        test_board = b.Board(3)
        self.assertEqual(test_board.board, [[-1] * ADV_SIZE for i in range(ADV_SIZE)])
        
    #test error board correctly defaults to advanced                        
    def test_init_err(self):
        test_board = b.Board(-1)
        test_board2 = b.Board(None)
        test_board3 = b.Board("hi")
        self.assertEqual(test_board.board, [[-1] * ADV_SIZE for i in range(ADV_SIZE)])
        self.assertEqual(test_board2.board, [[-1] * ADV_SIZE for i in range(ADV_SIZE)])
        self.assertEqual(test_board3.board, [[-1] * ADV_SIZE for i in range(ADV_SIZE)])
        
    #test to make sure set mines 'x' adds right amount of mines per board
    def test_set_mines(self):
        test_easy = b.Board(1)
        test_easy.set_mines()
        test_med = b.Board(2)
        test_med.set_mines()
        test_adv = b.Board(3)
        test_adv.set_mines()
        
        self.assertEqual(self.count_mines(test_easy), EASY_MINES)
        self.assertEqual(self.count_mines(test_med), MED_MINES)
        self.assertEqual(self.count_mines(test_adv), ADV_MINES)
        
    #counts mines 'x' in a given board
    def count_mines(self, test_board):
        count = 0
        for i in range(len(test_board.board)):
            for j in range(len(test_board.board[0])):
                if test_board.board[i][j] == 'x':
                    count += 1
        return count
    
    def test_set_tiles(self):
        #set up board
        test_board = b.Board(1)
        test_board.x_dim = 3
        test_board.y_dim = 3
        
        #test zero
        test_board.board = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
        test_board.set_tiles()
        self.assertEqual(test_board.board, [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        
        #test NW corner
        test_board.board = [['x', -1, -1], [-1, -1, -1], [-1, -1, -1]]
        test_board.set_tiles()
        self.assertEqual(test_board.board, [['x', 1, 0], [1, 1, 0], [0, 0, 0]])
        
        #test multiple mines
        test_board.board = [[-1, -1, -1], [-1, 'x', -1], [-1, -1, 'x']]
        test_board.set_tiles()
        self.assertEqual(test_board.board, [[1, 1, 1], [1, 'x', 2], [1, 2, 'x']])
                         
if __name__ == '__main__':
  unittest.main(exit=False)
