import unittest
from src.player import Player
from src.carddeck import CardDeck
from src.card import Card

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_init(self):
        player = Player("name", 1, "symbol")
        self.assertTrue(player)

    def test_add_to_hand(self):
        player = Player("name", 1, "d")
        card1 = Card("card1", 1, "a")
        card2 = Card("card2", 2, "b")
        card3 = Card("card3", 3, "c")
        cards = {}
        cards.append(card1)
        deck = CardDeck()
        dict1 = deck.convert_dict_and_add_to_deck(cards)
        player.add_to_hand(dict1)
        self.assertEqual(first, second)

    def test_check_hand(self):
        

    



if __name__ == '__main__':
    unittest.main()
