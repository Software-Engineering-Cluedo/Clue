import unittest
from src.player import Player
from src.playertoken import PlayerToken
from src.card import Card
from src.board import Board

class MyTestCase(unittest.TestCase):
    def test_move_by_direction(self):
        board = Board()
        card = Card('', '', '')
        playerToken = PlayerToken(10, 10, card, board, Player('', '', ''))
        playerToken.move_by_direction(1, 1)


if __name__ == '__main__':
    unittest.main()
