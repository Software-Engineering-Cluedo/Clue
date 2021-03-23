import os
import json
import shutil
import jsonschema
from jsonschema import validate
from pathlib import Path


class Board:
    config_dir = str(Path.home()) + "/Clue"
    tile_map = []
    all_rooms = []
    all_players = []
    all_weapons = []

    def __init__(self):
        self.setup_config_folder()
        parsed_correctly, data = self.parse_map_data()
        if parsed_correctly:
            print('Yay!')

    def setup_config_folder(self):
        Path(self.config_dir).mkdir(parents=True, exist_ok=True)
        if not Path(self.config_dir + '/clue.json').is_file():
            shutil.copy(os.path.dirname(__file__) + '/resources/json/clue.json', self.config_dir + '/clue.json')

    def parse_map_data(self):
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
            print('Valid json')
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
            if validate_y == valid_row_count:
                print('Valid dimensions')
            else:
                return False, 'Incorrect X dimension'
        else:
            return False, 'Incorrect Y dimension'



