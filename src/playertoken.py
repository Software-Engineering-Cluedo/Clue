from src.boardtoken import Token


class PlayerToken(Token):


    def __init__(self, x, y, card):
        super().__init__(x, y, card)
    

    def move(self, x, y):
        self.x = x
        self.y = y
