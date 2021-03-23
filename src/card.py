class Card:
    name = str
    card_id = int

    def __init__(self, name, card_id):
        print('todo')
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def get_card_id(self):
        return self.card_id
    
    def set_card_id(self, card_id):
        self.card_id = card_id