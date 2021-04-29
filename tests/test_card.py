import unittest
from src.card import Card

class MyTestCase(unittest.TestCase):
   def test_something(self):
       self.assertEqual(True, True)

   def test_get_name(self):
      card = Card("card1", 1, "w")
      name = card.get_name()
      self.assertEqual(name, "card1")

   def test_get_name_null_name(self):
      card = Card("", 1, "w")
      name = card.get_name()
      self.assertEqual(name, "")

   def test_get_symbol(self):
      card = Card("card1", 1, "w")
      symbol = card.get_symbol()
      self.assertEqual(symbol, "w")

   def test_get_symbol_null(self):
      card = Card("card1", 1, "")
      symbol = card.get_symbol()
      self.assertEqual(symbol, "")

   def test_set_name(self):
      card = Card("card1", 1, "")
      card.set_name("card2")
      self.assertEqual(card.get_name(), "card2")

   def test_set_name_null(self):
      card = Card("card1", 1, "")
      card.set_name("")
      self.assertEqual(card.get_name(), "")

   def test_get_id(self):
      card = Card("", 1, "")
      id = card.get_card_id()
      self.assertEqual(id, 1)

   def test_set_id(self):
      card = Card("", 1, "")
      card.set_card_id(10)
      self.assertEqual(card.get_card_id(), 10)

   def test_set_symbol(self):
      card = Card("", 1, "w")
      card.set_symbol("c")
      self.assertEqual(card.get_symbol(), "c")

if __name__ == '__main__':
   unittest.main()

