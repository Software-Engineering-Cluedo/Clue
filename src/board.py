from pathlib import Path
import os.path


class Board:
    data_dir = str(Path.home()) + "/Clue"
    # def __init__(self):
    #     print('todo')

    def create_save_folder(self):
        if not os.path.isdir(self.data_dir):
            os.mkdir(self.data_dir)
        print(self.data_dir)

    def create_default_map(self):
        print('todo')

    def parse_map_data(self):
        print('todo')
