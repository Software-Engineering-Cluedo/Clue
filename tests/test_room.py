import unittest
import json
from src.board import Board
from pathlib import Path
import os
import shutil
import tempfile
from src.room import Room
from src.card import Card

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_set_weapon_token(self):
        board = Board()
        room = Room("card1", 1, "w")
        weapon = list(board.weapon_tokens.values())[1]
        room.set_weapon_token(weapon)
        self.assertEqual(room.weapon_token, weapon)

    def test_get_weapon_token(self):
        board = Board()
        room = Room("card1", 1, "w")
        weapon = list(board.weapon_tokens.values())[1]
        room.set_weapon_token(weapon)
        self.assertEqual(room.weapon_token, room.get_weapon_token())

    def test_contains_weapon(self):
        board = Board()
        room = Room("card1", 1, "w")
        weapon = list(board.weapon_tokens.values())[1]
        room.set_weapon_token(weapon)
        room2 = Room("card1", 1, "w")
        result = False
        if room.contains_weapon() == True and room2.contains_weapon() != True:
            result = True
        self.assertEqual(result, True)
   

if __name__ == '__main__':
    unittest.main()
