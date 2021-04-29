import unittest
import json
from src.board import Board
from pathlib import Path
import os
import shutil
import tempfile
from src.player import Player
from src.human import Human

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

# Broken test
#
# def test_suggest(self):
#         data = self.get_json_data()
#         board = Board()
#         player_token_all
        
#         suggest(player_token_all, player_card_dict, current_room, weapon_token_all, left_player, board)
        
#         result =

#         if suggest.correct_cards != :
            
#         self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()
