from src.boardtoken import Token


class WeaponToken(Token):
    def __init__(self, x, y, card):
        super().__init__(x, y, card)
