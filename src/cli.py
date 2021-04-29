import os
import sys
import json
import time
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
        self.dice = self.board.dice

        cont = True
        movements = {'W': [0, -1], 'S': [0, 1], 'A': [-1, 0], 'D': [1, 0]}
        misc_options_one = ['E', 'D']
        misc_options_two = ['E']
        correct = False
        key = ''

        self.move_players_testing()
        # self.remove_players_testing()

        while cont:
            for player_char in self.players:                    
                if key == 'P':
                    cont = False
                    break
                   
                roll_one, roll_two = self.dice.roll()
                steps = roll_one + roll_two
                player_not_stopped = True
                
                while player_not_stopped and steps > 0 and not correct:
                    if key == 'P':
                        cont = False
                        player_not_stopped = False
                        break

                    key_incorrect = True
                    while key_incorrect:
                        player_token = self.player_tokens[player_char]
                        player_object = self.players[player_char]
                    
                        key, option = self.menu_refresh(player_token, player_char, steps)

                        if key == 'P':
                            cont = False
                            player_not_stopped = False
                            key_incorrect = False
                            break

                        elif key == '!':
                            player_not_stopped = False
                            key_incorrect = False
                        
                        elif key == '£' or (key == '"' and (option == 1 or option == 3)):
                            # options order: player_cards, rooms, weapons
                            if key == '£':
                                options = self.board.get_card_options(False)
                            if key == '"' and (option == 1 or option == 3):
                                options = self.board.get_card_options(True)
                            
                            selection = []
                            for option_type in options:
                                for i, card_details in enumerate(option_type):
                                    print('%s : %s' % (i, card_details[3]))
                                
                                cont_three = True
                                while cont_three:
                                    inp = int(input('Select from above: '))
                                    if inp < len(option_type) and inp >= 0:
                                        selection.append(option_type[inp])
                                        cont_three = False
                                    else:
                                        print('incorrect number')
                            
                            if key == '"' and (option == 1 or option == 3):

                                # Room for suggest doesn't need to be selected, is derrived from current room of the current player

                                player_token_list = list(self.player_tokens.items())

                                """ Also temp for debugging """
                                cards = self.board.solution.get_solution()
                                print('cards: ', cards)
                                """                         """

                                selection = []
                                for option_type in options:
                                    for i, card_details in enumerate(option_type):
                                        print('%s : %s - %s' % (i, card_details[1], card_details[3]))
                                    
                                    cont_three = True
                                    while cont_three:
                                        inp = int(input('Select from above: '))
                                        if inp < len(option_type) and inp >= 0:
                                            selection.append(option_type[inp])
                                            cont_three = False
                                        else:
                                            print('incorrect number')
                                
                                left_player = player_token_list[p_pos - 1 % len(player_token_list)]
                                player_object.suggest(selection[0], {selection[0]: self.player_cards[selection[0]]}, {player_token.current_room: self.rooms[player_token.current_room]}, selection[2], left_player, self.board)

                            elif key == '£':
                                correct = player_object.accuse(selection[0], selection[1], selection[2], self.board.solution)
                                if correct:
                                    cont = False
                                    player_not_stopped = False
                                    key_incorrect = False
                                    key = 'P'
                            else:
                                print('wut')
                                input()


                        elif key in movements or key in misc_options_one or key in misc_options_two:
                            if option == 0 and key in movements:
                                cont_two = True
                                switch = True
                                while cont_two:
                                    if switch:
                                        switch = False
                                    else:
                                        key, temp_option = self.menu_refresh(player_token, player_char, steps)

                                    if key == 'P':
                                        cont_two = False
                                        cont = False
                                        steps -= 1
                                        key_incorrect = False
                                    elif key in movements:
                                        off_x, off_y = movements[key]  
                                        cont_two, has_entered = player_token.move_by_direction(off_x, off_y)
                                        cont_two = not cont_two

                                        if has_entered:
                                            steps = 1
                                        else:
                                            steps -= 1
                                key_incorrect = False
                            elif option == 1 and key in misc_options_one:
                                if key == 'D':
                                    player_token.enter_secret_door()
                                    steps = 1
                                else:
                                    player_token.exit_door()
                                    steps -= 1
                                
                                key_incorrect = False
                            elif option == 2 and key in misc_options_two:
                                player_token.exit_door()
                                steps -= 1
                                key_incorrect = False


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
            key = input('up (w), down (s), left (a), right (d), wait(!), accuse(£), stop (p)\n')
        elif option == 1:
            key = input('exit(e), secret door(d), wait(!), suggest("), accuse(£), stop (p)\n')
        elif option == 2:
            key = input('exit(e), secret door(d), wait(!), accuse(£), stop (p)\n')
        elif option == 3:
            key = input('exit(e), wait(!), suggest("), accuse(£), stop (p)\n')
        elif option == 4:
            key = input('exit(e), wait(!), accuse(£), stop (p)\n')

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
