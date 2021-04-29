import unittest
import json
from src.board import Board
from pathlib import Path
import os
import shutil
import tempfile



class MyTestCase(unittest.TestCase):
    secure_temp = tempfile.mkstemp()
    config_dir = str(Path.home()) + "/Clue"


    def get_json_data(self):
        data = []
        config_dir = str(Path.home()) + "/Clue"
        with open(config_dir + '/clue.json', encoding='UTF-8') as file:
            data = json.loads(file.read())
        return data


    def copy_over_clue(self, path):
        """
        1 (default) : /../src/resources/json/clue.json
        2 (test for line deleted) : /resources/json/lineDeleted.json
        """
        shutil.copy(self.config_dir + '/clue.json', self.secure_temp[1])
        shutil.copy(os.path.dirname(__file__) + path, self.config_dir + '/clue.json')
        

    def restore_from_temp_dir(self):
        shutil.copy(self.secure_temp[1], self.config_dir + '/clue.json')
    
    def reset_config(self):
        board = Board()
        board.setup_config_folder(True)


    #
    # Broken as hecc, we will do this if we have time
    #
    # def test_parse_map_data(self):
    #     board = Board()
    #     board.setup_config_folder(True)

    #     self.copy_over_clue('/resources/json/clue.json')
    #     board = Board()
    #     result, data = board.setup_board()
    #     self.restore_from_temp_dir()
    #     self.assertEqual(result, True)

    #     self.copy_over_clue('/resources/json/lineDeleted.json')
    #     board = Board()
    #     result, data = board.setup_board()
    #     self.restore_from_temp_dir()
    #     self.assertEqual(result, False)


    def test_not_a_test(self):
        self.reset_config()


    def test_get_surrounding(self):
        y = 10
        x = 10
        data = self.get_json_data()
        board = Board()
        tile_map = data["map"]["tiles"]
        result = board.get_surrounding(x, y, tile_map) != False
        self.assertEqual(result, True)
        board = Board()
        tile_map = data["map"]["tiles"]
        result = board.get_surrounding(x,y, tile_map) != False
        self.assertEqual(result, True)


    def test_get_surrounding(self):
        y = 10
        x = 10
        data = self.get_json_data()
        board = Board()
        tile_map = data["map"]["tiles"]
        result = board.get_surrounding(x, y, tile_map) != False
        self.assertEqual(result, True)


    def test_generate_objects_from_tiles(self):
        data = self.get_json_data()
        board = Board()
        r1, r2, r3, r4, r5 = board.generate_objects_from_tiles(data)
        result = r1 != False
        self.assertEqual(result, True)


    def test_check_valid_doors(self):
        data = self.get_json_data()
        board = Board()
        result = board.check_valid_doors(data)
        self.assertEqual(result, True)


    def test_find_instance(self):
        y = 10
        x = 10
        data = self.get_json_data()
        board = Board()
        tile_map = data["map"]["tiles"]

        result1 = board.get_instance(tile_map[y][x], tile_map, True)
        self.assertEqual(result1 != False, True)
        self.assertEqual(len(result1), 2)
        result2 = board.get_instance(tile_map[y][x], tile_map, False)
        self.assertEqual(result2 != False, True)

    def test_generate_combined_map(self):
        board = Board()
        result1 = board.generate_combined_map(board.tile_map, board.weapon_map, board.player_map, board.door_map)
        result2 = [['.', '.', '.', '.', '.', '.', '.', '.', '.', 'Q', '.', '.', '.', '.', 'W', '.', '.', '.', '.', '.', '.', '.', '.', 
'.'], ['k', 'k', 'k', 'k', 'k', '🤠', '.', 't', 't', 't', 'b', 'b', 'b', 'b', 
't', 't', 't', '.', 'c', 'c', 'c', 'c', 'c', 'c'], ['k', 'k', 'k', 'k', 'k', 'k', 't', 't', 'b', 'b', 'b', 'b', 'b', 
'b', 'b', 'b', 't', 't', 'c', 'c', 'c', 'c', '6', 'c'], ['k', '1', 'k', 'k', 'k', 'k', 't', 't', 'b', 'b', 'b', 'b', 
'b', 'b', 'b', 'b', 't', 't', 'c', 'c', 'c', 'c', 'c', 'c'], ['k', 'k', 'k', 'k', 'k', 'k', 't', 't', 'b', 'b', 'b', 
'b', 'b', 'b', 'b', 'b', 't', 't', 'D', 'c', 'c', 'c', 'c', 'c'], ['k', 'k', 'k', 'k', 'k', 'k', 't', 't', 'D', 'b', 
'b', 'b', 'b', 'b', 'b', 'D', 't', 't', 't', 'c', 'c', 'c', '👾', '.'], ['.', 
'k', 'k', 'k', 'D', 'k', 't', 't', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 't', 't', 't', 't', 't', 't', 't', 'E'], ['t', 't', 't', 't', 't', 't', 't', 't', 'b', 'D', 'b', 'b', 'b', 'b', 'D', 'b', 't', 't', 't', 't', 't', 't', 't', '.'], ['.', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 'r', 'r', 'r', 'r', 'r', 'r'], ['d', 'd', 'd', 'd', 'd', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 'D', 'r', 'r', 'r', 'r', 'r'], ['d', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 't', 't', '.', '.', '.', '.', '.', 't', 't', 't', 'r', 'r', 'r', 'r', 'r', 'r'], ['d', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 't', 't', '.', '.', '.', '.', '.', 't', 't', 't', 'r', 'r', '2', 'r', 'r', 'r'], ['d', 'd', 'd', 'd', 'd', 'd', 'd', 'D', 't', 't', '.', '.', '.', '.', '.', 't', 't', 't', 'r', 'r', 'r', 'r', 'D', 'r'], ['d', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 't', 't', '.', '.', '.', '.', '.', 't', 't', 't', 't', 't', 't', 't', 't', '.'], ['d', 'd', '4', 'd', 'd', 'd', 'd', 'd', 't', 't', '.', '.', '.', '.', '.', 't', 't', 't', 'l', 'l', 'D', 'l', 'l', '.'], 
['d', 'd', 'd', 'd', 'd', 'd', 'D', 'd', 't', 't', '.', '.', '.', '.', '.', 't', 't', 'l', 'l', 'l', 'l', 'l', 'l', 'l'], ['.', 't', 't', 't', 't', 't', 't', 't', 't', 't', '.', '.', '.', '.', '.', 't', 't', 'D', 'l', 'l', 'l', 'l', 'l', 'l'], ['R', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 'l', 'l', 'l', 'l', 'l', 'l', 'l'], ['.', 't', 't', 't', 't', 't', 't', 't', 't', 'h', 'h', 'D', 'D', 'h', 'h', 't', 't', 't', 'l', 'l', 'l', 'l', 'l', '.'], ['👾', 'o', 'o', 'o', 'o', 'o', 'D', 't', 't', 'h', 'h', 'h', 'h', 'h', 'h', 't', 't', 't', 't', 
't', 't', 't', 't', 'T'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 't', 't', 'h', 'h', 'h', 'h', 'h', 'h', 't', 't', 't', 
't', 't', 't', 't', 't', '.'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 't', 't', 'h', 'h', 'h', 'h', 'h', 'h', 't', 't', 
'D', 's', 's', 's', 's', 's', '🤠'], ['o', 'o', 'o', '3', 'o', 'o', 'o', 't', 
't', 'h', 'h', 'h', 'h', 'h', 'h', 't', 't', 's', 's', 's', '5', 's', 's', 's'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 
't', 't', 'h', 'h', 'h', 'h', 'h', 'h', 't', 't', 's', 's', 's', 's', 's', 's', 's'], ['o', 'o', 'o', 'o', 'o', 'o', 
'o', 'Y', '.', 'h', 'h', 'h', 'h', 'h', 'h', '.', 't', 's', 's', 's', 's', 's', 's', 's']]

        self.assertEqual(result1, result2)
        

if __name__ == '__main__':
    unittest.main()
