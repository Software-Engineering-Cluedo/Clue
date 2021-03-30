import os
import json
import shutil
import jsonschema
import numpy as np

from pathlib import Path
from jsonschema import validate

from src.room import Room
from src.player import Player
from src.weapon import Weapon
from src.playercard import PlayerCard


class Board:
    """The representation of the Clue board.
    
    Attributes:
        config_dir: A string which is the path to the Clue config directory
        tile_map: An two dimensional array which stores the tile map for the board where each object is
        symbols: An dictionary with each unique symbol from the tile map storing the associated class
    """

    config_dir = str(Path.home()) + "/Clue"
    tile_map = []
    symbols = {}
    

    def __init__(self):
        self.setup_config_folder()
        parsed_correctly, data = self.parse_map_data()
        if parsed_correctly:
            self.tile_map = data
            print(*self.tile_map, sep='\n')


    def setup_config_folder(self):
        Path(self.config_dir).mkdir(parents=True, exist_ok=True)
        if not Path(self.config_dir + '/clue.json').is_file():
            shutil.copy(os.path.dirname(__file__) + '/resources/json/clue.json', self.config_dir + '/clue.json')


    def is_unique_tiles(self, tiles):
        unique_symbols = {s['char'] for s in tiles}
        return len(unique_symbols) == len(tiles)


    def place_weapons_in_rooms(self, weapons, rooms, tile_map):
        print("weapons:", weapons)
        for key, val in weapons.items():
            x, y = self.find_first_instance(key, tile_map)
            self.get_surrounding(x, y, tile_map)
            


    def find_first_instance(self, symbol, tile_map):
        found = False
        i = 0
        
        while found == False and i < len(tile_map):
            if symbol in tile_map[i]:
                return tile_map[i].find(symbol), i
            i += 1
        
        return False, False


    def get_surrounding(self, x, y, tile_map):
        print(x, y)
        max_y = len(tile_map)
        max_x = len(tile_map[0])
        surrounding = []
        for i in range(y - 1, y + 2):
            temp = []
            for j in range(x - 1, x + 2):
                if i >= 0 and j >= 0 and i < max_y and j < max_x:
                    temp.append(tile_map[i][j])
                else:
                    temp.append(None)
            surrounding.append(temp)
        
        print(*surrounding, sep='\n')
        return surrounding


    def generate_objects_from_tiles(self, data):
        generated_objects = {tile['char']:tile['obj'] for tile in data['simple tiles']}
        
        rooms = {}
        weapons = {}
        players = {}
        player_cards = {}

        player_count = 0

        for obj_id, tile in enumerate(data['game tiles']):
            current_tile = tile['char']
            name = tile['name']
            symbol = tile['char']

            if tile['obj'].lower() == 'room':
                r = Room(name, obj_id, symbol)
                generated_objects[symbol] = r
                rooms[symbol] = r

            elif tile['obj'].lower() == 'weapon':
                w = Weapon(name, obj_id, symbol)
                generated_objects[symbol] = w
                weapons[symbol] = w

            elif tile['obj'].lower() == 'player':
                player = Player(name, player_count, symbol)
                players[symbol] = player

                pc = PlayerCard(name, obj_id, symbol, player)
                generated_objects[symbol] = pc
                player_cards[symbol] = pc

                player_count += 1

            else:
                return False, False, False, False, False
            
        return generated_objects, rooms, weapons, players, player_cards


    def correct_count_object_ref(self, data):
        return True


    def parse_map_data(self):
        """Parses map json data to create the board and associated classes

        Checks if the json is valid, and then creates the board with the data 
        and creates objects from the config too

        Returns:
            bool: Determines if ran successfully
            array: An array of data created from the config, includes the tile map (more to be added in the future)
        """

        # Load users config file and the schema into vars
        try:
            with open(self.config_dir + '/clue.json', encoding='UTF-8') as file:
                data = json.loads(file.read())
            with open(os.path.dirname(__file__) + '/resources/json/clue.schema', encoding='UTF-8') as file:
                data_schema = json.loads(file.read())

        except IOError as e:
            print(e)
            return False, 'IO Error'

        # Validate the users json config file against the schema
        try:
            validate(instance=data, schema=data_schema)
        except jsonschema.exceptions.ValidationError as e:
            print(e)
            return False, 'Schema Error'

        # Validate size to dimensions attribute
        validate_x = data['map']['dimensions']['x']
        validate_y = data['map']['dimensions']['y']

        if validate_y == len(data['map']['tiles']):
            valid_row_count = 0
            while valid_row_count < validate_y and len(data['map']['tiles'][valid_row_count]) == validate_x:
                valid_row_count += 1
            if validate_y != valid_row_count:
                return False, 'Incorrect X dimension'
        else:
            return False, 'Incorrect Y dimension'

        simple_tiles = data['simple tiles']
        game_tiles = data['game tiles']

        if self.is_unique_tiles(simple_tiles) and self.is_unique_tiles(game_tiles):
            if self.correct_count_object_ref(data):
                board_objects, rooms, weapons, players, player_cards = self.generate_objects_from_tiles(data)
                if board_objects != False:
                    self.place_weapons_in_rooms(weapons, rooms, data['map']['tiles'])
                else:
                    return False, 'Contains unidentified descriptor for a tile entry'
            else:
                return False, 'Used a single use character multiple times'

        else:
            return False, 'Tile symols are not unique'

        return True, [board_objects, weapons, rooms, players, player_cards]