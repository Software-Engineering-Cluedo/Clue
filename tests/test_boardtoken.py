import unittest
from src.boardtoken import Token
from src.card import Card

class MyTestCase(unittest.TestCase):

    def test_token_init(self):
        card = Card("card1", 1, "w")
        token = Token(1, 1, card)
        self.assertTrue(token)


    def test_set_position(self):
        card = Card("card1", 1, "w")
        token = Token(1, 1, card)
        token.set_position(2, 2)
        x, y = token.get_position()
        self.assertEqual(x, 2)
        self.assertEqual(y, 2)

    def test_get_position(self):
        card = Card("card1", 1, "w")
        token = Token(1, 1, card)
        x, y = token.get_position()
        self.assertEqual(x, 1)
        self.assertEqual(y, 1)

    def test_set_card(self):
        card = Card("card", 1, "w")
        card1 = Card("card1", 2, "c")
        token = Token(1, 1, card)
        token.set_card(card1)
        self.assertEqual(token.get_card(), card1)

    def test_get_card(self):
        card = Card("card1", 1, "w")
        token = Token(1, 1, card)
        token.set_card(card)
        self.assertEqual(card, token.get_card())
    


    

        