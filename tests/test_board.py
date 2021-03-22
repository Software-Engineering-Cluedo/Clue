import unittest
from src.board import Board


class MyTestCase(unittest.TestCase):
    def test_create_save_folder(self):
        board = Board()
        board.setup_config_folder()
        self.assertEqual(False, True)


if __name__ == '__main__':
    unittest.main()
