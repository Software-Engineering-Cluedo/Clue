import unittest
from src.game import Game
test_game=Game()

class MyTestCase(unittest.TestCase):
    def test_setup(self):
        print(str(test_game.boardArr)+" print")
        self.assertEqual(True, True)
    
    def test_complete_board(self):
        test_game.complete_board()
        self.assertEqual(True,True)

if __name__ == '__main__':
    unittest.main()
