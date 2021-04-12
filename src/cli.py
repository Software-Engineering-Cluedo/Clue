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
            for row in range(len(self.board.combined_tiles)):
                for col in range(len(self.board.combined_tiles[0])):
                    print(self.board.combined_tiles[row][col], end='')
                print()
            key = input('up (w), down (s), left (a), right (d), stop (p)\n')
            if key.upper() == 'P': 
                running = False    

    def refresh_tile_maps(self):
        self.tile_map = self.board.tile_map
        self.player_map = self.board.player_map
        self.weapon_map = self.board.weapon_map
        self.door_map = self.board.door_map
        self.combined_map = self.board.generate_combined_map(self.tile_map, self.player_map, self.weapon_map, self.door_map)
