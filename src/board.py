import os
import json
import shutil
import itertools
import jsonschema

from pathlib import Path
from jsonschema import validate
from collections import Counter

from src.room import Room
from src.player import Player
from src.weapon import Weapon
from src.playercard import PlayerCard


class Board:
    """The representation of the Clue board.

    TODO: check for false for methods when calling
    
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
        parsed_correctly, data = self.setup_board()
        if parsed_correctly:
            self.tile_map = data
            # print(*self.tile_map, sep='\n')


    def setup_config_folder(self):
        """ Creates the config directory for Clue and copies the default clue map to the folder if doesn't exist """

        Path(self.config_dir).mkdir(parents=True, exist_ok=True)
        if not Path(self.config_dir + '/clue.json').is_file():
            shutil.copy(os.path.dirname(__file__) + '/resources/json/clue.json', self.config_dir + '/clue.json')


    def is_unique_tiles(self, tiles):
        """ Checks if there are duplicate uses of a symbol for different contexts """

        unique_symbols = {s['char'] for s in tiles}
        return len(unique_symbols) == len(tiles)


    def place_weapons_in_rooms(self, weapons, rooms, simple_tiles, tile_map):
        """ Finds the location of the weapons in relation to the room, and adds it to the room class of the prodominately surrounding room symbol """

        for key, val in weapons.items():
            x, y = self.find_instance(key, tile_map, True)
            surrounding = self.get_surrounding(x, y, tile_map)
            unique_chars = self.get_unique_char_count(surrounding)

            if None in unique_chars:
                del unique_chars[None]
            for entry in simple_tiles:
                if entry['char'] in unique_chars:
                    del unique_chars[entry['char']]

            current_largest = list(unique_chars.keys())[0]
            for char, count in unique_chars.items():
                if unique_chars[current_largest] < count:
                    current_largest = char

            room = rooms[current_largest]
            room.set_weapon_token(val)

            return True


    def convert_tile_map_to_2d_array(self, tile_map):
        for i in range(len(tile_map)):
            tile_map[i] = [char for char in tile_map[i]]

        return tile_map


    def find_instance(self, symbol, tile_map, first):
        arr = []
        for y in range(len(tile_map)):
            for x in range(len(tile_map[0])):
                if tile_map[y][x] == symbol:
                    if first:
                        return x, y
                    else:
                        arr.append([x, y])

        if arr == None:
            return False
        return arr


    def get_surrounding(self, x, y, tile_map):
        """ Finds the surrounding tiles around a set of coordanates """

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

        if surrounding == None:
            return False
        return surrounding


    def generate_objects_from_tiles(self, data):
        """ Creates objects from the game tiles data """

        generated_objects = {tile['char']:tile['obj'] for tile in data['simple tiles']}
        
        rooms = {}
        weapons = {}
        players = {}
        player_cards = {}

        player_count = 0

        for obj_id, tile in enumerate(data['game tiles']):
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


    def get_unique_char_count(self, arr):
        return dict(Counter(i for i in list(itertools.chain.from_iterable(arr))).items())


    def correct_count_object_ref(self, data):
        """ Checks if the object type appears the correct amount of times """

        combo_tiles = {tile['char']:tile['obj'] for tile in data['simple tiles'] + data['game tiles']}
        unique_chars = self.get_unique_char_count(data['map']['tiles'])

        # Rules, could be stored in dict
        weapon = 1
        player = 1
        secret_door = 2

        # This can be shortened using a for loop
        for char, val in unique_chars.items():
            if combo_tiles[char].lower() == 'weapon':
                if val != weapon:
                    return False
            elif combo_tiles[char].lower() == 'player':
                if val != player:
                    return False
            elif combo_tiles[char].lower() == 'secret door':
                if val != secret_door:
                    return False

        return True


    def check_valid_doors(self, data):
        """ Checks if the doors are in valid positions """
        tile_map = data['map']['tiles']
        door_locations = self.find_instance('D', tile_map, False)

        simple_tile_symbols_dict = {tile['char']:tile['obj'] for tile in data['simple tiles']}
        simple_tile_symbols = [tile for tile in simple_tile_symbols_dict]
        
        for key, val in simple_tile_symbols_dict.items():
            if val.lower() == 'door':
                door_symbol = key

        for x, y in door_locations:
            surrounding = self.get_surrounding(x, y, tile_map)
            surrounding_t = list(map(list, itertools.zip_longest(*surrounding, fillvalue=None)))
            unique_tiles = self.get_unique_char_count(surrounding)

            check_one = False
            for i in range(len(surrounding)):
                if i == 0 or i == 2:
                    rows = [self.get_unique_char_count(surrounding[i]), self.get_unique_char_count(surrounding_t[i])]
                    count = 0

                    # Checks for appropriate amount of simple tiles
                    for row in rows:
                        for key, val in row.items():
                            if (key in simple_tile_symbols and key != door_symbol) or key == None:
                                count += val
                        
                        if count == 3 and door_symbol not in row:
                            check_one = True

        for symbol in simple_tile_symbols:
            if symbol in unique_tiles:
                del unique_tiles[symbol]

        check_two = 1 == len(unique_tiles)

        if check_one and check_two:
            return True
        else:
            return False


    def seperate_board_and_players(self, tile_map, players, simple_tiles):
        for tile in simple_tiles:
            if tile['obj'].lower() == 'tile':
                simple_tile = tile['char']
        
        player_map = []
        for i in range(len(tile_map)):
            row = []
            for j in range(len(tile_map[0])):
                row.append('')
            player_map.append(row)

        for player_symbol, player_object in players.items():
            x, y = self.find_instance(player_symbol, tile_map, True)
            player_map[y][x] = player_symbol
            tile_map[y][x] = simple_tile

        return tile_map, player_map


    def generate_tokens(self, tile_map, player_map, players, weapons):
        for player_symbol, player_object in players.items():
            player_position = self.find_instance(player_symbol, player_map, True)


    def setup_board(self):
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

        self.convert_tile_map_to_2d_array(data['map']['tiles'])
        print(*data['map']['tiles'], sep='\n')

        if self.is_unique_tiles(simple_tiles) and self.is_unique_tiles(game_tiles):
            if self.correct_count_object_ref(data):
                if self.check_valid_doors(data):
                    board_objects, rooms, weapons, players, player_cards = self.generate_objects_from_tiles(data)
                    if board_objects != False:
                        self.place_weapons_in_rooms(weapons, rooms, simple_tiles, data['map']['tiles'])
                        tile_map, player_map = self.seperate_board_and_players(data['map']['tiles'], players, simple_tiles)
                        tokens, weapon_tokens, player_tokens = self.generate_tokens(tile_map, player_map, players, weapons)
                    else:
                        return False, 'Contains unidentified descriptor for a tile entry'
                else:
                    return False, 'A door or multiple doors are at an invalid position'
            else:
                return False, 'Used a single use character multiple times'
        else:
            return False, 'Tile symbols are not unique'

        return True, [data, tile_map, player_map, board_objects, weapons, rooms, players, player_cards]