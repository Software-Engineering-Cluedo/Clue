import unittest
from src.playertoken import PlayerToken

class MyTestCase(unittest.TestCase):
    def test_move_by_direction(self):
        card = Card()
        playerToken = PlayerToken(10, 10, card, board)
        playerToken.move_by_direction(1, 1)


if __name__ == '__main__':
    unittest.main()
