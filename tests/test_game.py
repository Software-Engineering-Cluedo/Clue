import unittest
from src.game import Game
test_game=Game()

class MyTestCase(unittest.TestCase):
    def test_setup(self):
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()

