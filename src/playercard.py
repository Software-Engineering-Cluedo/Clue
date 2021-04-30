from src.card import Card


class PlayerCard(Card):
    player = None


    def __init__(self, name, card_id, symbol, player):
        super().__init__(name, card_id, symbol)
        self.player = player


    def set_player(self, player):
        """sets the player to the playercard object"""
        self.player = player


    def get_player(self, player):
        """returns the player for the current card
            Returns: 
                player: the player assigned to the playerCard
        """
        return self.player
