import os
import json
import shutil
import itertools
import jsonschema

from pathlib import Path
from copy import copy, deepcopy
from collections import Counter

from src.room import Room
from src.weapon import Weapon
from src.player import Player
from src.boardtoken import Token
from src.playercard import PlayerCard
from src.weapontoken import WeaponToken
from src.playertoken import PlayerToken


class Board:
    """The representation of the Clue board.

    TODO: check for false for methods when calling
    TODO: Add comments
    
    Attributes:
        config_dir: A string which is the path to the Clue config directory
        tile_map: An two dimensional array which stores the tile map for the board where each object is
        symbols: An dictionary with each unique symbol from the tile map storing the associated class
    """

    config_dir = str(Path.home()) + "/Clue"

    data = None
    tile_map  = None
    player_map = None
    weapon_map = None
    door_map = None
    board_objects = None
    weapons = None
    rooms = None
    players = None
    player_cards = None
    combined_tiles = None
    

    def __init__(self):
        self.setup_config_folder()
        parsed_correctly, r_data = self.setup_board()
        print(parsed_correctly)
        if parsed_correctly:
            self.data = r_data[0]
            self.tile_map = r_data[1]
            self.player_map = r_data[2]
            self.weapon_map = r_data[3]
            self.door_map = r_data[4]
            self.board_objects = r_data[5]
            self.weapons = r_data[6]
            self.rooms = r_data[7]
            self.players = r_data[8]
            self.player_cards = r_data[9]
            self.combined_tiles = r_data[10]


    def setup_config_folder(self):
        """ Creates the config directory for Clue and copies the default clue map to the folder if doesn't exist """

        Path(self.config_dir).mkdir(parents=True, exist_ok=True)
        if not Path(self.config_dir + '/clue.json').is_file():
            shutil.copy(os.path.dirname(__file__) + '/resources/json/clue.json', self.config_dir + '/clue.json')


    def is_unique_tiles(self, tiles):
        """Checks if there are duplicate uses of a symbol for different contexts
        
        Args:
            tiles: The set of tile types, e.g. data['simple tiles'] or data['game tiles']
        
        Returns:
            bool: If all symbols are unique in the tile set given
        """

        unique_symbols = {s['char'] for s in tiles}
        return len(unique_symbols) == len(tiles)


    def place_weapons_in_rooms(self, weapons, rooms, simple_tiles, tile_map):
        """Finds the location of the weapons in relation to the room, and adds it to the room class of the prodominately surrounding room symbol
        
        TODO: Need to perform checks on other methods

        Args:
            weapons: The dictionary of characters associated to it's weapon object
            rooms: The dictionary of characters associated to it's room object 
            simple_tiles: The simple tiles object from the json data, e.g. data['simple tiles']
            tile_map: The tile map from the json data e.g. data['map']['tiles']

        Returns:
            bool: If all is ran, returns true
        """

        # Loop through the keys and associated value in weapons
        for key, val in weapons.items():
            x, y = self.find_instance(key, tile_map, True)
            surrounding = self.get_surrounding(x, y, tile_map)
            unique_chars = self.get_unique_char_count(surrounding)

            # Delete None entry in unique_chars dictionary
            if None in unique_chars:
                del unique_chars[None]

            # Remove all simple tile characters from unique_char dict
            for entry in simple_tiles:
                if entry['char'] in unique_chars:
                    del unique_chars[entry['char']]

            # Find the most used character surrounding the weapon
            current_largest = list(unique_chars.keys())[0]
            for char, count in unique_chars.items():
                if unique_chars[current_largest] < count:
                    current_largest = char

            # Get room using symbol and assign the weapon object within the room
            room = rooms[current_largest]
            room.set_weapon_token(val)

            return True


    def convert_tile_map_to_2d_array(self, tile_map):
        """Converts the one dimentional array of strings into a two dimention array of characters

        Args:
            tile_map: The tile map to be used from the json data, e.g. data['map']['tiles']
        
        Returns:
            tile_map: a two dimentional array of characters
        """

        for i in range(len(tile_map)):
            tile_map[i] = [char for char in tile_map[i]]

        return tile_map


    def find_instance(self, symbol, tile_map, first):
        """Finds all or the first instance of a certain symbol / character position

        Args:
            symbol: The symbol to find the position/s of, e.g. char = 't'
            tile_map: The tile map of the board, e.g. data['map']['tiles']
            first: If true, it finds the first instance of the symbol, false gets all positions
        
        Returns:
            bool: Returns false if arr is none 
            Arr: The position or positions of the symbol 
        """

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
        """Finds the surrounding tiles around a set of coordanates
        
        Args:
            x: x position
            y: y position
            tile_map: The tile map of the board, e.g. data['map']['tiles']
        
        Returns:
            bool: If surrounding array is none, returns false
            surrounding: The surrounding characters around x and y
        """

        max_y = len(tile_map)
        max_x = len(tile_map[0])
        surrounding = []

        # Loops through the one wide radius of the position given and adds the character to the array
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
        """Creates objects from the game tiles data
        
        Args:
            data: The whole json data
        
        Returns:
            generated_objects: All objetcs with associated symbols
            rooms: All rooms with associated symbols
            weapons: All weapons with associated symbols
            players: All players with associated symbols
            player_cards: All player_cards with associated symbols
        """

        # Cerates the simple tile dictionary with the character and associated object
        generated_objects = {tile['char']:tile['obj'] for tile in data['simple tiles']}
        
        # Create empty dictionary
        rooms = {}
        weapons = {}
        players = {}
        player_cards = {}

        player_count = 0

        # Loops through the data
        for obj_id, tile in enumerate(data['game tiles']):
            name = tile['name']
            symbol = tile['char']

            # Make objects from the object names
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
        """Counts each character and assigns the value to the character in a dictionary
        
        Args:
            arr: the array to search through, e.g. the tile map or surrounding characters around a position
        
        Returns:
            dict: dictionary of characters with the amount of times it appears
        """
        return dict(Counter(i for i in list(itertools.chain.from_iterable(arr))).items())


    def correct_count_object_ref(self, data):
        """Checks if the object type appears the correct amount of times
        
        Args:
            data: The whole json data, used to count the amount a character appears to check if appears correct amount of times
        """

        combo_tiles = {tile['char']:tile['obj'] for tile in data['simple tiles'] + data['game tiles']}
        unique_chars = self.get_unique_char_count(data['map']['tiles'])

        # Rules
        rules = {'weapon' : 1, 'player' : 1, 'secret door' : 2}

        # Loops through rules and checks if it appears in unique characters, if it is checks if the count is correct
        for obj, correct_count in rules.items():
            for char, val in unique_chars.items():
                if combo_tiles[char].lower() == obj:
                    if correct_count != val:
                        return False

        return True


    def check_valid_doors(self, data):
        """Checks if the doors are in valid positions
        
        Args:
            data: The whole json data

        Returns:
            bool: If it passes the checks or not
        """
        
        # Gets tile map and gets the simple tile symbols
        tile_map = data['map']['tiles']
        simple_tile_symbols_dict = {tile['char']:tile['obj'] for tile in data['simple tiles']}
        simple_tile_symbols = [tile for tile in simple_tile_symbols_dict]
        
        # Gets the door symbol
        for key, val in simple_tile_symbols_dict.items():
            if val.lower() == 'door':
                door_symbol = key

        # Finds each instance of the door
        door_locations = self.find_instance(door_symbol, tile_map, False)

        # Loops through all door locations
        for x, y in door_locations:
            
            # Gets surrounding symbols or the location and creates the transpose of the original, gets unique tile count of surrounding
            surrounding = self.get_surrounding(x, y, tile_map)
            surrounding_t = list(map(list, itertools.zip_longest(*surrounding, fillvalue=None)))
            unique_tiles = self.get_unique_char_count(surrounding)

            # Checks if appropriate amount of simple tiles surrounding the door location
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

        # Deletes all simple tiles from unique tile character entries from unique_tiles
        for symbol in simple_tile_symbols:
            if symbol in unique_tiles:
                del unique_tiles[symbol]

        # Checks if the unique_tiles length only contains one room
        check_two = 1 == len(unique_tiles)

        # If passed both checks return True
        if check_one and check_two:
            return True
        else:
            return False


    def separate_board(self, tile_map, players, weapons, simple_tiles):
        """Separates the players and the board into separate arrays
        
        Args:
            tile_map: The tile map of the board, e.g. data['map']['tiles']
            players: The dictionary of players and associated symbols
            simple_tiles: All simple tiles from the json data, e.g. data['simple tiles']

        Returns:
            tile_map: Returns the newly formatted tile map
            player_map: The locations of players
        """

        # Gets the tile symbol from the simple_tiles
        for tile_type in simple_tiles:
            if tile_type['obj'].lower() == 'tile':
                tile_symbol = tile_type['char']
            if tile_type['obj'].lower() == 'door':
                door_symbol = tile_type['char']

        # Creates a blank maps to store locations of different object types
        player_map = self.generate_blank_map(tile_map)
        weapon_map = self.generate_blank_map(tile_map)
        door_map = self.generate_blank_map(tile_map)

        # Stores players in player map and turns existing tile_map player symbols into tiles
        for player_symbol, player_object in players.items():
            x, y = self.find_instance(player_symbol, tile_map, True)
            player_map[y][x] = player_symbol
            tile_map[y][x] = tile_symbol
        
        # Stores players in player map and turns existing tile_map player symbols into tiles
        for weapon_symbol, weapon_object in weapons.items():
            x, y = self.find_instance(weapon_symbol, tile_map, True)
            tile_map, weapon_map = self.separate_board_common(weapon_map, tile_map, simple_tiles, weapon_symbol, x, y)

        door_locations = self.find_instance(door_symbol, tile_map, False)
        for door in door_locations:
            x, y = door
            tile_map, door_map = self.separate_board_common(door_map, tile_map, simple_tiles, door_symbol, x, y)

        # Returns both maps
        return tile_map, player_map, weapon_map, door_map


    def separate_board_common(self, new_map, tile_map, simple_tiles, search_symbol, x, y ):
        new_map[y][x] = search_symbol
        surrounding = self.get_surrounding(x, y, tile_map)
        unique_chars = self.get_unique_char_count(surrounding)
        
        del unique_chars[search_symbol]
        if None in unique_chars:
            del unique_chars[None]
        for symbol in simple_tiles:
            if symbol['char'] in unique_chars:
                del unique_chars[symbol['char']]
        
        if 1 == len(unique_chars):
            tile_map[y][x] = list(unique_chars)[0]
            return tile_map, new_map
        else:
            return False


    def generate_blank_map(self, tile_map):
        blank_map = []
        for i in range(len(tile_map)):
            row = []
            for j in range(len(tile_map[0])):
                row.append('')
            blank_map.append(row)
        return blank_map


    def generate_all_tokens(self, player_map, players, weapon_map, weapons):
        return self.generate_tokens(weapon_map, weapons, True), self.generate_tokens(player_map, players, False)


    def generate_tokens(self, char_map, object_dict, is_weapon):
        tokens = []

        for symbol, object in object_dict.items():
            x, y = self.find_instance(symbol, char_map, True)
            if is_weapon:
                tokens.append(WeaponToken(x, y, object))
            else:
                tokens.append(PlayerToken(x, y, object))
        return tokens


    def generate_combined_map(self, tile_map, weapon_map, player_map, door_map):
        combined_tiles = []
        for y in range(len(tile_map)):
            temp = []
            for x in range(len(tile_map[y])):
                if player_map[y][x] != '':
                    temp.append(player_map[y][x])   
                elif weapon_map[y][x] != '':
                    temp.append(weapon_map[y][x])
                elif door_map[y][x] != '':
                    temp.append(door_map[y][x])
                else:
                    temp.append(tile_map[y][x])
            combined_tiles.append(temp)
        return combined_tiles


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
            jsonschema.validate(instance=data, schema=data_schema)
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

        # Performs each check and creates objects
        if self.is_unique_tiles(simple_tiles + game_tiles):
            # Need to check for edge door check
            if self.correct_count_object_ref(data):
                if self.check_valid_doors(data):
                    board_objects, rooms, weapons, players, player_cards = self.generate_objects_from_tiles(data)
                    if board_objects != False:
                        self.place_weapons_in_rooms(weapons, rooms, simple_tiles, data['map']['tiles'])
                        tile_map, player_map, weapon_map, door_map = self.separate_board(data['map']['tiles'], players, weapons, simple_tiles)
                        weapon_tokens, player_tokens = self.generate_all_tokens(player_map, players, weapon_map, weapons) # TODO
                    else:
                        return False, 'Contains unidentified descriptor for a tile entry'
                else:
                    return False, 'A door or multiple doors are at an invalid position'
            else:
                return False, 'Used a single use character multiple times'
        else:
            return False, 'Tile symbols are not unique'


        return True, [data, tile_map, player_map, weapon_map, door_map, board_objects, weapons, rooms, players, player_cards, self.generate_combined_map(tile_map, weapon_map, player_map, door_map)]