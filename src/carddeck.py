import random


class CardDeck():
    """ Class comment here """
    deck = {}
    deck_rev = {}


    def __len__(self):
        return len(self.deck)


    def convert_dict_and_add_to_deck(self, cards):
        self.deck = cards
        self.deck_rev = {value:key for key, value in cards.items()}
    
    
    def add_card(self, card_dict):
        symbol, card = list(card_dict.items())[0]
        self.deck[symbol] = card
        self.deck_rev[card] = symbol
        return symbol


    def has_card(self, card):
        return card in self.deck_rev


    def pop_card(self):
        choice = random.choice(list(self.deck.items()))
        del self.deck[choice[0]]
        del self.deck_rev[choice[1]]
        return {choice[0]: choice[1]}
    

    def is_empty(self):
        return not bool(self.deck)
