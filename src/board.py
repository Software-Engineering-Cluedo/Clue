import shutil
from pathlib import Path
import os


class Board:
    config_dir = str(Path.home()) + "/Clue"

    def setup_config_folder(self):
        Path(self.config_dir).mkdir(parents=True, exist_ok=True)
        if not Path(self.config_dir + '/map.json').is_file():
            shutil.copy(os.path.dirname(__file__) + '/resources/map.json', self.config_dir + '/map.json')


    def parse_map_data(self):
        print('todo')
