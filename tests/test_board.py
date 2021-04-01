import unittest
import json
from src.board import Board
from pathlib import Path


class MyTestCase(unittest.TestCase):
    data = []
    config_dir = str(Path.home()) + "/Clue"
    

    def __init__(self):
        super().init()
        with open(self.config_dir + '/clue.json', encoding='UTF-8') as file:
            self.data = json.loads(file.read())


    def test_parse_map_data(self):
        board = Board()
        result, data = board.setup_board()
        self.assertEqual(result, True)


    #def test_place_weapons_in_rooms(self):
     #   board = Board()
      #  result = board.place_weapons_in_rooms(w,r,s,t)


    def test_get_surrounding(self):
        board = Board()
        tile_map = data["map"]["tiles"]
        y = 10
        x = 10
        result = get_surrounding(x,y,tile_map) != False
        self.assertEqual(result, True)




if __name__ == '__main__':
    unittest.main()
