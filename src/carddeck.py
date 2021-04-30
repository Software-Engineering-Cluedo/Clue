import random


class CardDeck():
    """ Class comment here """
    deck = {}
    deck_rev = {}


    def __len__(self):
        return len(self.deck)


    def convert_dict_and_add_to_deck(self, cards):
        """Converts the dictionary into the deck format

        Args:
            cards: the dict to add of cards
        """
        self.deck = cards
        self.deck_rev = {value:key for key, value in cards.items()}
    
    
    def add_card(self, card_dict):
        """Adds card to deck and returns the symbol of what was added

        Args:
            card_dict: the card to add

        Returns:
            The symbol of the added card
        """
        symbol, card = list(card_dict.items())[0]
        self.deck[symbol] = card
        self.deck_rev[card] = symbol
        return symbol


    def has_card(self, card):
        """Returns of the card is in the card deck

        Args:
            card: the card to check if in deck
        
        Returns:
            bool: if card in deck return true, otherwise false
        """
        return card in self.deck_rev


    def pop_card(self):
        """Pops card from deck
        
        Returns:
            card: random card from deck removed
        """
        choice = random.choice(list(self.deck.items()))
        del self.deck[choice[0]]
        del self.deck_rev[choice[1]]
        return {choice[0]: choice[1]}
    

    def is_empty(self):
        """Checks if the deck is empty

        Returns:
            bool: if deck is empty return True, otherwise False
        """
        return not bool(self.deck)
