class Card:
    symbol = str
    name = str
    card_id = int

    def __init__(self, name, card_id, symbol):
        self.set_name(name)
        self.set_card_id(card_id)
        self.set_symbol(symbol)

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def get_card_id(self):
        return self.card_id
    
    def set_card_id(self, card_id):
        self.card_id = card_id

    def get_symbol(self):
        return self.symbol

    def set_symbol(self, symbol):
        self.symbol = symbol
