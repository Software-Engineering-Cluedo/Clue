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
        """Sets position of token

        Args:
            x: x position
            y: t position
        """
        self.x = x
        self.y = y


    def get_position(self):
        """Gets position of token
        
        Returns:
            int: x position
            int: y position
        """
        return self.x, self.y


    def set_card(self, card):
        """Sets card
        
        Args:
            card: the card to set
        """
        self.card = card

    
    def get_card(self):
        """Get card
        
        Returns:
            Card: the tokens associated card object
        """
        return self.card
    