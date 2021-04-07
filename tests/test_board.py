import unittest
import json
from src.board import Board
from pathlib import Path


class MyTestCase(unittest.TestCase):
    def get_json_data(self):
        data = []
        config_dir = str(Path.home()) + "/Clue"
        with open(config_dir + '/clue.json', encoding='UTF-8') as file:
            data = json.loads(file.read())
        
        return data


    def test_parse_map_data(self):
        board = Board()
        result, data = board.setup_board()
        self.assertEqual(result, True)


    def test_get_surrounding(self):
        y = 10
        x = 10
        data = self.get_json_data()
        board = Board()
        tile_map = data["map"]["tiles"]
        result = board.get_surrounding(x, y, tile_map) != False
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

        result1 = board.find_instance(tile_map[y][x], tile_map, True)
        self.assertEqual(result1 != False, True)
        self.assertEqual(len(result1), 2)
        result2 = board.find_instance(tile_map[y][x], tile_map, False)
        self.assertEqual(result2 != False, True)


if __name__ == '__main__':
    unittest.main()
