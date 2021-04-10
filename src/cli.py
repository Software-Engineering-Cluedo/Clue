from src.board import Board

class Cli():
    board = Board()


    def __init__(self):
        print('todo')


    def test_movement(self):
        """ A loop to test movement showing in the terminal """
        running = True

        while running:
            self.refresh_tile_maps()

            for y in range(len(self.tile_map)):
                for x in range(len(self.tile_map[y])):
                    if self.player_map[y][x] != '':
                        print(self.player_map[y][x], end='')
                    elif self.weapon_map[y][x] != '':
                        print(self.weapon_map[y][x], end='')
                    elif self.door_map[y][x] != '':
                        print(self.door_map[y][x], end='')
                    else:
                        print(self.tile_map[y][x], end='')
                print()
            key = input('up (w), down (s), left (a), right (d), stop (p)\n')
            if key.upper() == 'P': 
                running = False    

    def refresh_tile_maps(self):
        self.tile_map = self.board.tile_map
        self.player_map = self.board.player_map
        self.weapon_map = self.board.weapon_map
        self.door_map = self.board.door_map