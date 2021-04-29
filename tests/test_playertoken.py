import unittest
from src.playertoken import PlayerToken
from src.card import Card
from src.board import Board
from src.player import Player

class MyTestCase(unittest.TestCase):

    # Unfinished test
    def test_move_by_direction(self):
        board = Board()
        card = Card('', 0, '')
        player = Player('', '', '')
        playerToken = PlayerToken(10, 10, card, board, player)
        playerToken.move_by_direction(1, 1)


if __name__ == '__main__':
    unittest.main()
