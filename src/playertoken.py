from src.boardtoken import Token


class PlayerToken(Token):

    def __init__(self, x, y, card):
        super().__init__(x, y, card)
    
    def move(x, y):
        return True
