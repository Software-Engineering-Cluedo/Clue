import random


class CardDeck():
    """ Class comment here """
    """
    Index 0, symbol: obj
    Index 1, obj: symbol
    """
    deck = [{}, {}]


    def convert_dict_and_add_to_deck(self, cards):
        self.deck[0] = cards
        self.deck[1] = {value:key for key, value in cards.items()}
    
    
    def add_card(self, card_dict):
        symbol, card = tuple(card_dict)
        self.deck[0][symbol] = card
        self.deck[1][card] = symbol


    def has_card(self, card):
        return card in self.deck[1]


    def pop_card(self):
        choice = random.choice(list(self.deck[0].items()))
        del self.deck[0][choice[0]]
        del self.deck[1][choice[1]]
        return {choice[0]: choice[1]}
    
