import unittest
from src.game import Game


class MyTestCase(unittest.TestCase):
    test_game=Game()
    def test_setup(self):
        self.assertEqual(True, True)

    def test_setup_tile_dict(self):
        self.assertEqual(True,True)

    def test_generate_img_tiles(self):
        self.assertEqual(True,True)

    def test_generate_accusation_window(self):
        self.assertEqual(True,True)

if __name__ == '__main__':
    unittest.main()

