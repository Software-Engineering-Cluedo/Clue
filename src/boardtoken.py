from src.playercard import PlayerCard


class Token:
    x = None
    y = None
    card = None
    room = None


    def __init__(self, x, y, card):
        self.set_position(x, y)
        self.set_card(card)


    def set_position(self, x, y):
        self.x = x
        self.y = y


    def get_position(self):
        return self.x, self.y


    def set_card(self, card):
        self.card = card

    
    def get_card(self):
        return self.card
    