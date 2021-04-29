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


    def test_parse_map_data(self):
        self.copy_over_clue('/resources/json/clue.json')
        board = Board()
        result, data = board.setup_board(force=True)
        self.restore_from_temp_dir()
        self.assertEqual(result, True)

        self.copy_over_clue('/resources/json/lineDeleted.json')
        board = Board()
        result, data = board.setup_board()
        self.restore_from_temp_dir()
        self.assertEqual(result, False)


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


if __name__ == '__main__':
    unittest.main()
