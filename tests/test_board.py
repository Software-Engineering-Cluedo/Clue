import unittest
from src.board import Board

class MyTestCase(unittest.TestCase):
    def test_parse_map_data(self):
        board = Board()
        result, data = board.setup_board()
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
