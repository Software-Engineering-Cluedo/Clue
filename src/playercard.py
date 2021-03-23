from src.card import Card


class PlayerCard(Card):
    player = None

    def __init__(self, name, card_id, symbol):
        super().__init__(name, card_id, symbol)

    def set_player(self, player):
        self.player = player

    def get_player(self, player):
        return self.player
