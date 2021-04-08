from src.boardtoken import Token
from src.board import Board


class PlayerToken(Token):
    board = None

    def __init__(self, x, y, board):
        super().__init__(x, y)
        self.board = board
    
    def move(x, y):
        return True
