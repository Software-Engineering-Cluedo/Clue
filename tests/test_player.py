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
        card1 = {'h': Card("card1", 1, "a")}
        card2 = {'j': Card("card2", 2, "b")}
        card3 = {'k': Card("card3", 3, "c")}
        cards = card1 | card2 | card3
        dict1 = player.hand.convert_dict_and_add_to_deck(cards)
        card4 = {'l': Card("card4", 4, "d")}
        player.add_to_hand(card4)
        
        self.assertEqual(True, player.hand.has_card(list(card4.values())[0]))


if __name__ == '__main__':
    unittest.main()
