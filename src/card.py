class Card:
    symbol = str
    name = str
    card_id = int

    def __init__(self, name, card_id, symbol):
        self.set_name(name)
        self.set_card_id(card_id)
        self.set_symbol(symbol)


    def get_name(self):
        """Gets the cards name

        Returns:
            Str: the name of the card
        """
        return self.name
    

    def set_name(self, name):
        """Sets the cards name

        Args:
            name: the name to set it to
        """
        self.name = name
    

    def get_card_id(self):
        """Gets the card id

        Returns:
            int: card id
        """
        return self.card_id
    

    def set_card_id(self, card_id):
        """Sets the card id

        Args:
            card_id: card id
        """
        self.card_id = card_id


    def get_symbol(self):
        """Gets the associated symbol
        
        Returns:
            Str: symbol
        """
        return self.symbol


    def set_symbol(self, symbol):
        """Sets the associated symbol

        Args:
            Str: symbol
        """
        self.symbol = symbol
