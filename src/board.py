import os
import json
import shutil
import jsonschema
from jsonschema import validate
from pathlib import Path


class Board:
    config_dir = str(Path.home()) + "/Clue"

    def setup_config_folder(self):
        Path(self.config_dir).mkdir(parents=True, exist_ok=True)
        if not Path(self.config_dir + '/clue.json').is_file():
            shutil.copy(os.path.dirname(__file__) + '/resources/json/clue.json', self.config_dir + '/clue.json')

    def parse_map_data(self):
        try:
            with open(self.config_dir + '/clue.json', encoding='UTF-8') as file:
                data = json.loads(file.read())
        except IOError as e:
            return False

        try:
            with open(os.path.dirname(__file__) + '/resources/json/clue.schema', encoding='UTF-8') as file:
                data_schema = json.loads(file.read())
        except IOError as e:
            return False

        print(data)
        print(data_schema)

        validate(instance=data, schema=data_schema)

        # validate size to dimensions attribute
        validate_x = data['map']['dimensions']['x']
        validate_y = data['map']['dimensions']['y']

        print(validate_y)
        print(len(data['map']['tiles']))

        print(validate_x)
        print(len(data['map']['tiles'][0]))


