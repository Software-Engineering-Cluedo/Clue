import random
from src.boardtoken import Token


class PlayerToken(Token):
    board = None
    current_room = None
    door_entered = None
    accessed_through_other_door = False
    has_entered = False
    player = None


    def __init__(self, x, y, card, board, player):
        super().__init__(x, y, card)
        self.board = board
        self.player = player


    def move(self, x, y):
        self.x = x
        self.y = y
    
    
    def move_to_room(self, room):
        self.accessed_through_other_door = True
        symbol, room = list(room.items())[0]
        self.current_room = symbol
        temp_x, temp_y = random.choice(self.board.room_positions[symbol])
        self.move(temp_x, temp_y)


    def move_by_direction(self, off_x, off_y):
        cur_x, cur_y = self.get_position()
        temp_x, temp_y = [cur_x + off_x, cur_y + off_y]
        if temp_y >= 0 and temp_x >= 0 and temp_y < self.board.data['map']['dimensions']['y'] and temp_x < self.board.data['map']['dimensions']['x'] and self.board.player_map[temp_y][temp_x] == '' and (self.board.door_map[temp_y][temp_x] == self.board.default_symbols['door'] or self.board.tile_map[temp_y][temp_x] == self.board.default_symbols['tile']):
            if self.board.door_map[temp_y][temp_x] == self.board.default_symbols['door'] and self.door_entered == None:
                room_symbol = self.board.tile_map[temp_y][temp_x]
                self.door_entered = [cur_x, cur_y]
                self.current_room = room_symbol
                self.has_entered = True

                temp_x, temp_y = random.choice(self.board.room_positions[room_symbol])
                while self.board.door_map[temp_y][temp_x] != '':
                    temp_x, temp_y = random.choice(self.board.room_positions[room_symbol])

                self.move(temp_x, temp_y)
                self.board.update_player_positions()
            
            elif self.board.tile_map[cur_y][cur_x] == self.board.default_symbols['tile']:
                self.move(temp_x, temp_y)
                self.board.update_player_positions()
            return True, self.has_entered
        else:
            return False, False


    def enter_secret_door(self):
        found = False
        self.has_entered = True
        current_room_secret_door = list(self.board.secret_door_rooms[self.current_room].keys())[0]

        for room_symbol_dict, secrect_door_symbol_dict in self.board.secret_door_rooms.items():
            secrect_door_symbol = list(secrect_door_symbol_dict.keys())[0]
            if secrect_door_symbol == current_room_secret_door and room_symbol_dict != self.current_room and found == False:
                found = True

                temp_x, temp_y = self.board.secret_door_rooms[room_symbol_dict][secrect_door_symbol]
                room_symbol = self.board.tile_map[temp_y][temp_x]

                temp_x, temp_y = random.choice(self.board.room_positions[room_symbol])
                
                self.door_entered = [temp_x, temp_y]
                self.current_room = room_symbol

                temp_x, temp_y = random.choice(self.board.room_positions[room_symbol])
                while self.board.door_map[temp_y][temp_x] != '':
                    temp_x, temp_y = random.choice(self.board.room_positions[room_symbol])

                self.move(temp_x, temp_y)
                self.accessed_through_other_door = True
                self.board.update_player_positions()
    

    def exit_door(self):
        if self.accessed_through_other_door:
            self.exit_secret_door()
        else:
            self.exit_normal_door()


    def exit_normal_door(self):
        x, y = self.door_entered
        self.move(x, y)

        self.door_entered = None
        self.current_room = None
        self.board.update_player_positions()
    

    def exit_secret_door(self):
        all_tiles_next_to_doors = self.board.get_door_offset(self.current_room, self.board.tile_map, self.board.door_rooms, self.board.default_symbols['tile'])
        temp_x, temp_y = random.choice(all_tiles_next_to_doors)
        self.move(temp_x, temp_y)
        self.board.update_player_positions()
        self.accessed_through_other_door = False
        self.door_entered = None
        self.current_room = None
    

    def reset_has_entered(self):
        self.has_entered = False
    

    def get_turn_options(self):
        if self.door_entered == None:
            return 0 # Move normally
        elif self.current_room in self.board.secret_door_rooms and self.has_entered:
            return 1 # Exit room and go through secret door
        elif self.current_room in self.board.secret_door_rooms:
            return 2 # Exit room
        elif self.has_entered:
            return 3
        else:
            return 4
            