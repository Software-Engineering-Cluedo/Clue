import unittest
from src.board import Board

class MyTestCase(unittest.TestCase):
    def test_parse_map_data(self):
        board = Board()
        result, data = board.setup_board()
        self.assertEqual(result, True)

    def test_yesman(self):
        board = Board()
        





if __name__ == '__main__':
    unittest.main()
