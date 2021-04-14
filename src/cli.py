import json
from src.board import Board

class Cli():
    board = Board()


    def __init__(self):
        print('todo')


    def test_movement(self):
        """ A loop to test movement showing in the terminal """
        running = True

        self.data = self.board.data
        self.tile_map = self.board.tile_map
        self.player_map = self.board.player_map
        self.weapon_map = self.board.weapon_map
        self.door_map = self.board.door_map
        self.board_objects = self.board.board_objects
        self.weapons = self.board.weapons
        self.rooms = self.board.rooms
        self.players = self.board.players
        self.player_cards = self.board.player_cards
        self.combined_tiles = self.board.combined_tiles
        self.weapon_tokens = self.board.weapon_tokens
        self.player_tokens = self.board.player_tokens

        self.print_all()

        cont = True

        while cont:
            print('Select one of the following characters to start: ')
            print(self.players.keys())
            player_char = input().upper()

            if player_char in self.players:
                player_object = self.players[player_char]
                cont = False
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


    def print_all(self):
        print(json.dumps(self.data, indent=4))
        print()
        print(*self.tile_map, sep='\n')
        print()
        print(*self.player_map, sep='\n')
        print()
        print(*self.weapon_map, sep='\n')
        print()
        print(*self.door_map, sep='\n')
        print()
        print(*self.board_objects)
        print()
        print(*self.weapons)
        print()
        print(*self.rooms)
        print()
        print(*self.players)
        print()
        print(*self.player_cards)
        print()
        print(*self.combined_tiles, sep='\n')
        print()
        print(*self.weapon_tokens, sep='\n')
        print()
        print(*self.player_tokens, sep='\n')
        print()