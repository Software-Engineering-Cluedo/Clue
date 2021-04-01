import unittest
from src.board import Board



class MyTestCase(unittest.TestCase):
    data = []
    
    def __init__(self):
        with open(self.config_dir + '/clue.json', encoding='UTF-8') as file:
            self.data = json.loads(file.read())

    def test_parse_map_data(self):
        board = Board()
        result, data = board.setup_board()
        self.assertEqual(result, True)
    
    #def test_place_weapons_in_rooms(self):
     #   board = Board()
      #  result = board.place_weapons_in_rooms(w,r,s,t)

    


if __name__ == '__main__':
    unittest.main()
