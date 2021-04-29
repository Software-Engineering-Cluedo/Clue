import os
import sys
import json
import time
import random
from ai import Ai
from src.board import Board


class Cli():
    board = Board()


    def test_movement(self):
        """ A loop to test movement showing in the terminal """

        end = False
        running = True
        self.dice = self.board.dice
        self.refresh_tile_maps()
        
        self.move_players_testing()
        # self.remove_players_testing()
        
        while not end:
            for player_char in self.board.players:
                player_object = self.players[player_char]
                cont = True
                
                while cont:
                    if type(player_object) is Ai:
                        print()
                    else:
                        key, option = self.menu_refresh()



    def menu_refresh(self, player_token, player_char, remaining_steps):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.refresh_tile_maps()
        print(player_char, remaining_steps)
        for row in range(len(self.combined_tiles)):
            for col in range(len(self.combined_tiles[0])):
                print(self.combined_tiles[row][col], end='')
            print()

        option = player_token.get_turn_options()

        if option == 0:
            key = input('look at hand(h), up (w), down (s), left (a), right (d), wait(!), accuse(£), stop (p)\n')
        elif option == 1:
            key = input('look at hand(h), exit(e), secret door(d), wait(!), suggest("), accuse(£), stop (p)\n')
        elif option == 2:
            key = input('look at hand(h), exit(e), secret door(d), wait(!), accuse(£), stop (p)\n')
        elif option == 3:
            key = input('look at hand(h), exit(e), wait(!), suggest("), accuse(£), stop (p)\n')
        elif option == 4:
            key = input('look at hand(h), exit(e), wait(!), accuse(£), stop (p)\n')

        key = key.upper()

        return key, option


    def refresh_tile_maps(self):
        self.tile_map = self.board.tile_map
        self.player_map = self.board.player_map
        self.weapon_map = self.board.weapon_map
        self.door_map = self.board.door_map
        self.combined_tiles = self.board.generate_combined_map(self.tile_map, self.player_map, self.weapon_map, self.door_map)


    def remove_players_testing(self):
        del self.players['Q']
        del self.players['W']
        del self.players['E']
        del self.players['R']
        del self.players['T']

    
    def move_players_testing(self):
        self.player_tokens['Q'].move(7, 5)
        self.player_tokens['W'].move(17, 4)
        self.player_tokens['E'].move(17, 9)
        self.player_tokens['R'].move(6, 16)
        self.player_tokens['T'].move(16, 21)
        self.player_tokens['Y'].move(7, 19)
        self.board.update_player_positions()
        self.refresh_tile_maps()


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
