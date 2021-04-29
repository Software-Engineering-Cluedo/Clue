import json
import unittest
import random
from pathlib import Path

from src.room import Room
from src.player import Player
from src.weapon import Weapon
from src.board import Board
from src.solution import Solution


class MyTestCase(unittest.TestCase):
    def get_json_data(self):
        data = []
        config_dir = str(Path.home()) + "/Clue"
        with open(config_dir + '/clue.json', encoding='UTF-8') as file:
            data = json.loads(file.read())
        
        return data

    #Old tests, broken due to not using generate anymore
    
    def test_set_and_get_solution(self):
        board = Board()

        room = random.choice(list(board.rooms.items()))
        player_card = random.choice(list(board.player_cards.items()))
        weapon = random.choice(list(board.weapons.items()))

        room = {room[0]: room[1]}
        player_card = {player_card[0]: player_card[1]}
        weapon = {weapon[0]: weapon[1]}

        solution = Solution(room, player_card, weapon)
        r, p, w = solution.get_solution()

        self.assertEqual(r, room)
        self.assertEqual(p, player_card)
        self.assertEqual(w, weapon)



    def test_check_solution(self):
        board = Board()

        room = random.choice(list(board.rooms.items()))
        player_card = random.choice(list(board.player_cards.items()))
        weapon = random.choice(list(board.weapons.items()))

        room = {room[0]: room[1]}
        player_card = {player_card[0]: player_card[1]}
        weapon = {weapon[0]: weapon[1]}

        solution = Solution({1: room}, {1: player_card}, {1: weapon})

        b = solution.check_solution(list(room.values())[0], list(player_card.values())[0], list(weapon.values())[0])
        self.assertEqual(b, True)

        b = solution.check_solution('h', list(player_card.values())[0], list(weapon.values())[0])
        self.assertEqual(b, True)


if __name__ == '__main__':
    unittest.main()
