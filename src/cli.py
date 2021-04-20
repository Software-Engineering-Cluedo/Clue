import os
import sys
import json
import random
from src.board import Board


class Cli():
    board = Board()


    def test_movement(self):
        """ A loop to test movement showing in the terminal """
        running = True

        self.refresh_tile_maps()

        self.data = self.board.data
        self.board_objects = self.board.board_objects
        self.weapons = self.board.weapons
        self.rooms = self.board.rooms
        self.players = self.board.players
        self.player_cards = self.board.player_cards
        self.combined_tiles = self.board.combined_tiles
        self.weapon_tokens = self.board.weapon_tokens
        self.player_tokens = self.board.player_tokens

        cont = True
        movements = {'W': [0, -1], 'S': [0, 1], 'A': [-1, 0], 'D': [1, 0]}
        misc_options_one = ['E', 'D']
        misc_options_two = ['E']

        for tile, obj in self.board.simple_tiles.items():
            if obj['obj'] == 'tile':
                tile_symbol = tile
            if obj['obj'] == 'door':
                door_symbol = tile

        while cont:
            for player_char in self.players:
                player_token = self.player_tokens[player_char]
                player_object = self.players[player_char]

                self.refresh_tile_maps()
                print(player_char)
                for row in range(len(self.combined_tiles)):
                    for col in range(len(self.combined_tiles[0])):
                        print(self.combined_tiles[row][col], end='')
                    print()
            
                option = player_token.get_turn_options()

                if option == 0:
                    key = input('up (w), down (s), left (a), right (d), stop (p)\n')
                elif option == 1:
                    key = input('exit(e), secret door(d), stop (p)\n')
                elif option == 2:
                    key = input('exit(e), stop (p)\n')

                key = key.upper()

                if key == 'P':
                    cont = False
                
                elif key in movements or key in misc_options_one or key in misc_options_two:
                    if option == 0 and key in movements:
                        off_x, off_y = movements[key]
                        player_token.move_by_direction(off_x, off_y)
                    elif option == 1 and key in misc_options_one:
                        if key == 'D':
                            player_token.enter_secret_door()
                        else:
                            player_token.exit_door()
                    elif option == 2 and key in misc_options_two:
                        player_token.exit_door()
                

                


    def refresh_tile_maps(self):
        self.tile_map = self.board.tile_map
        self.player_map = self.board.player_map
        self.weapon_map = self.board.weapon_map
        self.door_map = self.board.door_map
        self.combined_tiles = self.board.generate_combined_map(self.tile_map, self.player_map, self.weapon_map, self.door_map)


    def roll_dice(self):
        return random.randrange(1,7), random.randrange(1,7)


    def print_all(self):
        print(json.dumps(self.data, indent=4))
        print()
        print(*self.board.tile_map, sep='\n')
        print()
        print(*self.board.player_map, sep='\n')
        print()
        print(*self.board.weapon_map, sep='\n')
        print()
        print(*self.board.door_map, sep='\n')
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