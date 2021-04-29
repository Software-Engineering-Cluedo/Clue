import json
import unittest
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
        board_objects, rooms, weapons, players, player_cards = board.generate_objects_from_tiles(self.get_json_data())
        solution = Solution(rooms, player_cards, weapons)
        solution.set_solution(rooms, player_cards, weapons)
        r, p, w = solution.get_solution()
        #r, p, w = solution.generate_solution(rooms, player_cards, weapons)
        self.assertEqual(r != False, True)



    def test_check_solution(self):
        board = Board()
        board_objects, rooms, weapons, players, player_cards = board.generate_objects_from_tiles(self.get_json_data())
        solution = Solution(rooms, player_cards, weapons)
        r, p, w = solution.get_solution()
        self.assertEqual(r != False, True)
        solution.set_solution(r, p, w)
        self.assertEqual(solution.check_solution(r, p, w), True)
        self.assertEqual(solution.check_solution('', p, w), False)


if __name__ == '__main__':
    unittest.main()
