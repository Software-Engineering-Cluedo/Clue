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

        accessed_through_secret_door = False

        for tile, obj in self.board.simple_tiles.items():
            if obj['obj'] == 'tile':
                tile_symbol = tile
            if obj['obj'] == 'door':
                door_symbol = tile

        key = ''

        while cont:
            door_entered = None
            current_room = None

            for player_char in self.players:
                player_token = self.player_tokens[player_char]
                player_object = self.players[player_char]
                cont_two = True

                if key == 'P': 
                    break

                while cont_two:
                    self.refresh_tile_maps()
                    print(player_char)
                    for row in range(len(self.combined_tiles)):
                        for col in range(len(self.combined_tiles[0])):
                            print(self.combined_tiles[row][col], end='')
                        print()
                    
                    # TODO Buggy, need to fix, elif and else do not work. Current room and door entered need to have percistant storage for each character
                    if door_entered == None:
                        key = input('up (w), down (s), left (a), right (d), stop (p)\n')
                    elif current_room in self.board.secret_door_rooms:
                        key = input('exit(e), secret door(d), stop (p)\n')
                    else:
                        key = input('exit(e), stop (p)\n')

                    key = key.upper()
                    if key == 'P':
                        cont = False
                        cont_two = False
                    elif key in movements or key in misc_options_one or key in misc_options_two:
                        
                        room_symbol = None

                        os.system('cls' if os.name == 'nt' else 'clear')
                        if door_entered != None:
                            
                            if current_room in self.board.secret_door_rooms and key in misc_options_one:
                                cont_two = False
                                if key == 'D':
                                    print(self.board.secret_door_rooms)
                                    current_room_secret_door = list(self.board.secret_door_rooms[current_room].keys())[0]

                                    found = False

                                    for room_symbol_dict, secrect_door_symbol_dict in self.board.secret_door_rooms.items():
                                        secrect_door_symbol = list(secrect_door_symbol_dict.keys())[0]
                                        if secrect_door_symbol == current_room_secret_door and room_symbol_dict != current_room and found == False:
                                            found = True

                                            temp_x, temp_y = self.board.secret_door_rooms[room_symbol_dict][secrect_door_symbol]
                                            room_symbol = self.board.tile_map[temp_y][temp_x]

                                            temp_x, temp_y = random.choice(self.board.room_positions[room_symbol])
                                            door_entered = [temp_x, temp_y]

                                            current_room = room_symbol

                                            temp_x, temp_y = random.choice(self.board.room_positions[room_symbol])
                                            while self.door_map[temp_y][temp_x] != '':
                                                temp_x, temp_y = random.choice(self.board.room_positions[room_symbol])

                                            player_token.move(temp_x, temp_y)
                                            accessed_through_secret_door = True
                                            self.board.refresh_player_positions()

                                else:
                                    if accessed_through_secret_door:
                                        x, y = door_entered
                                        all_tiles_next_to_doors = self.board.get_door_offset(current_room, self.tile_map, self.board.door_rooms, tile_symbol)

                                        temp_x, temp_y = random.choice(all_tiles_next_to_doors)

                                        player_token.move(temp_x, temp_y)
                                        self.board.refresh_player_positions()
                                        accessed_through_door = False
                                        door_entered = None
                                        current_room = None
                                    else:
                                        x, y = door_entered
                                        player_token.move(x, y)
                                        self.board.refresh_player_positions()
                                        door_entered = None
                                        current_room = None


                            elif key in misc_options_two:
                                cont_two = False
                                x, y = door_entered
                                player_token.move(x, y)
                                self.board.refresh_player_positions()
                                door_entered = None
                                current_room = None
                                
                            else:
                                continue
                        
                        elif key in movements:
                            cur_x, cur_y = player_token.get_position()
                            temp_x, temp_y = [cur_x + movements[key][0], cur_y + movements[key][1]]
                            if temp_y >= 0 and temp_x >= 0 and temp_y < self.board.data['map']['dimensions']['y'] and temp_x < self.board.data['map']['dimensions']['x'] and self.player_map[temp_y][temp_x] == '' and (self.door_map[temp_y][temp_x] == door_symbol or self.tile_map[temp_y][temp_x] == tile_symbol):
                                cont_two = False
                                if self.door_map[temp_y][temp_x] == door_symbol and door_entered == None:
                                    room_symbol = self.board.tile_map[temp_y][temp_x]
                                    door_entered = [cur_x, cur_y]
                                    current_room = room_symbol

                                    temp_x, temp_y = random.choice(self.board.room_positions[room_symbol])
                                    while self.door_map[temp_y][temp_x] != '':
                                        temp_x, temp_y = random.choice(self.board.room_positions[room_symbol])

                                    player_token.move(temp_x, temp_y)
                                
                                elif self.tile_map[cur_y][cur_x] == tile_symbol:
                                    player_token.move(temp_x, temp_y)

                                self.board.refresh_player_positions()

                            else:
                                print("Can't move this direction")
                


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