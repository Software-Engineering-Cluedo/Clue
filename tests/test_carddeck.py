import unittest
from src.carddeck import CardDeck
from src.card import Card

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    
    def test_convert_dict_and_add_to_deck(self):
        deck = CardDeck()
        card1 = Card("card1", 1, "symbol1")
        card2 = Card("card2", 2, "symbol2")
        card3 = Card("card3", 3, "symbol3")
        cards = {card1.get_symbol(): card1, card2.get_symbol(): card2, card3.get_symbol(): card3}
        deck.convert_dict_and_add_to_deck(cards)
        self.assertEqual(deck.deck, cards)


    def test_len(self):
        card = CardDeck()
        length = card.__len__()
        length1 = len(card.deck)
        self.assertEqual(length, length1)

    def test_add_card(self):
        deck = CardDeck()
        card1 = {'symbol1': Card("card1", 1, "symbol1")}
        card2 = {'symbol2': Card("card2", 2, "symbol2")}
        card3 = {'symbol3': Card("card3", 3, "symbol3")}
        deck.add_card(card1)
        deck.add_card(card2)
        deck.add_card(card3)
        cards = card1 | card2 | card3
        self.assertEqual(cards, deck.deck)

    # def test_has_card(self):

    # def test_pop_card(self):

    def test_is_empty(self):
        deck = CardDeck()
        card1 = Card("card1", 1, "symbol1")
        card2 = Card("card2", 2, "symbol2")
        card3 = Card("card3", 3, "symbol3")
        cards = {card1.get_symbol(): card1, card2.get_symbol(): card2, card3.get_symbol(): card3}
        deck.add_card(cards)
        self.assertEqual(0, deck.is_empty())


"""
    def add_card(self):


    def has_card(self):

    def pop_card(self):

    def is_empty(self):

"""

if __name__ == '__main__':
    unittest.main()
