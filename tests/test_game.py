import unittest
from src.game import Game


class MyTestCase(unittest.TestCase):
    def test_something(self):
        game = Game()
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()