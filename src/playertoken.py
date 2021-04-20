from src.boardtoken import Token


class PlayerToken(Token):
    board = None
    current_room = None
    door_entered = None
    accessed_through_secret_door = False
    door_symbol = None
    tile_symbol = None

    def __init__(self, x, y, card, board):
        super().__init__(x, y, card)
        self.board = board


    def move(self, x, y):
        self.x = x
        self.y = y
    

    def move_by_direction(self, off_x, off_y):
        cur_x, cur_y = self.get_position()
        temp_x, temp_y = [cur_x + off_x, cur_y + off_y]
        if temp_y >= 0 and temp_x >= 0 and temp_y < self.board.data['map']['dimensions']['y'] and temp_x < self.board.data['map']['dimensions']['x'] and self.board.player_map[temp_y][temp_x] == '' and (self.board.door_map[temp_y][temp_x] == self.board.door_symbol or self.board.tile_map[temp_y][temp_x] == self.board.tile_symbol):
            if self.door_map[temp_y][temp_x] == self.board.door_symbol and self.door_entered == None:
                self.enter_door()
            
            elif self.tile_map[cur_y][cur_x] == tile_symbol:
                self.move(temp_x, temp_y)
                self.board.refresh_player_positions()
        else:
            print("Can't move this direction")


    def enter_door(self):
        room_symbol = self.board.tile_map[temp_y][temp_x]
        self.door_entered = [cur_x, cur_y]
        self.current_room = room_symbol

        temp_x, temp_y = random.choice(self.board.room_positions[room_symbol])
        while self.door_map[temp_y][temp_x] != '':
            temp_x, temp_y = random.choice(self.board.room_positions[room_symbol])

        self.move(temp_x, temp_y)
        self.board.refresh_player_positions()


    def enter_secret_door(self):
        found = False
        current_room_secret_door = list(self.board.secret_door_rooms[current_room].keys())[0]

        for room_symbol_dict, secrect_door_symbol_dict in self.board.secret_door_rooms.items():
            secrect_door_symbol = list(secrect_door_symbol_dict.keys())[0]
            if secrect_door_symbol == current_room_secret_door and room_symbol_dict != current_room and found == False:
                found = True

                temp_x, temp_y = self.board.secret_door_rooms[room_symbol_dict][secrect_door_symbol]
                room_symbol = self.board.tile_map[temp_y][temp_x]

                temp_x, temp_y = random.choice(self.board.room_positions[room_symbol])
                
                self.door_entered = [temp_x, temp_y]
                self.current_room = room_symbol

                temp_x, temp_y = random.choice(self.board.room_positions[room_symbol])
                while self.door_map[temp_y][temp_x] != '':
                    temp_x, temp_y = random.choice(self.board.room_positions[room_symbol])

                self.move(temp_x, temp_y)
                self.accessed_through_secret_door = True
                self.board.refresh_player_positions()
    

    def exit_door(self):
        if self.accessed_through_secret_door:
            self.exit_secret_door()
        else:
            self.exit_normal_door()


    def exit_normal_door(self):
        x, y = self.door_entered
        self.move(x, y)

        self.door_entered = None
        self.current_room = None
        self.board.refresh_player_positions()
    

    def exit_secret_door(self):
        x, y = self.door_entered
        all_tiles_next_to_doors = self.board.get_door_offset(current_room, self.tile_map, self.board.door_rooms, tile_symbol)

        temp_x, temp_y = random.choice(all_tiles_next_to_doors)

        self.move(temp_x, temp_y)
        self.board.refresh_player_positions()
        self.accessed_through_secret_door = False
        self.door_entered = None
        self.current_room = None
    

    def get_turn_options(self):
        if self.door_entered == None:
            return 0 # Move normally
        elif current_room in self.board.secret_door_rooms:
            return 1 # Exit room and go through secret door
        else:
            return 2 # Exit room