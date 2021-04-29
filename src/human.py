import random
from src.player import Player

class Human(Player):
    movements = {'W': [0, -1], 'S': [0, 1], 'A': [-1, 0], 'D': [1, 0]}
    keys = ['W', 'S', 'A', 'D', 'E', '!', '"', '£']
    option_zero = ['w', 's', 'a', 'd', '!', '£', 'p']
    option_one = ['e', 'd', '!', '"', '£', 'p']
    option_two = ['e', 'd', '!', '£', 'p']
    option_three = ['e', '!', '"', '£', 'p']
    option_four = ['e', '!', '£', 'p']

    def __init__(self, name, player_id, symbol):
        super().__init__(name, player_id, symbol)
    

    def suggest(self, player_token_all, player_card_dict, current_room, weapon_token_all, left_player, board):
        """Suggest clue gameplay method

        Args:
            player_token_all: The player token chosen with additional details as tuple
            player_card_dict: The associated card to player token
            current_room: The room our player is in
            weapon_token_all: The weapon token chosen with additional details as tuple
            left_player: The player to the left of ours
            board: The game board
        Returns:
            bool: if no cards are correct
            card: returns a random card if any were correct
        """
        
        # Would move the weapon and player token (derrived from player card) to the room the player is currently in
        # It would perform the checks according to the instructions and return either false or the cards correctly guessed
        player_card = list(player_card_dict.values())[0]
        player_token = player_token_all[2]
        weapon_token = weapon_token_all[2]
        room = list(current_room)[0]

        player_token.move_to_room(current_room)
        temp_x, temp_y = random.choice(board.room_positions[room])
        weapon_token.set_position(temp_x, temp_y)

        correct_cards = []
        cards = [player_card, weapon_token.card, room]

        for card in cards:
            if left_player[1].player.hand.has_card(card):
                correct_cards.append(card)
        
        board.update_player_positions()
        board.update_room_positions()
        
        if correct_cards == []:
            return False
        else:
            return random.choice(correct_cards)

    
    def accuse(self, player_card, room, weapon, solution):
        """Accuses player

        Args:
            player_card: the guessed player card
            room: the guessed room
            weapon: the guessed weapon
            solution: the games solution
        Returns:
            boolean: if solution is correct
        """
        return solution.check_solution(room, player_card, weapon)
    
    

    """
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
    """


    """
    404: try again
    400: quit
    202: entered door
    200: won
    400: player out
    242: suggested
    """


    def turn(self, key, dice, extra=None):
        if key not in self.keys:
            return 404
        elif key == 'P':
            return 400

        if not self.out:
            option = self.player_token.get_turn_options()

            if option == 0 and key in self.option_zero:
                roll_one, roll_two = dice.roll()
                steps = roll_one + roll_two

            elif (option == 1 and key in self.option_one) or (option == 2 and key in self.option_two) or (option == 3 and key in self.option_three) or (option == 4 and key in self.option_four):
                return self.in_room(key, extra)

            else:
                return 404


    def in_room(self, key, extra):
        if key == 'E':
            self.player_token.exit_door()
            return 202
        elif key == 'D':
            self.player_token.enter_secret_door()
            return 202
        elif key == '"' or key == '£':
            return self.accuse_or_suggest(key, extra)
        elif key == '!' or key == 'p':
            return self.wait_or_stop(key)
    

    def accuse_or_suggest(self, key, extra):
        # extra[0] : suggest, 
        #   option order : player_cards, rooms, weapons
        # extra[1] : player

        selection = extra[0]
        if key == '£':
            correct = self.accuse(selection[0][2], selection[1][2], selection[2][2], self.board.solution)
            if correct:
                return 200
            else:
                self.toggle_out()
                return 400

        elif key == '"':
            #player_token_list = list(self.player_tokens.items())
            player_token_list = list(extra[1].items())

            for i, p in enumerate(player_token_list):
                if p[0] == self.symbol:
                    p_pos = i
            
            left_player = player_token_list[p_pos - 1 % len(player_token_list)]
            result = self.player_object.suggest(selection[0], {selection[0][1]: self.player_cards[selection[0][1]]}, {self.current_room: self.rooms[self.current_room]}, selection[1], left_player, self.board)
            return 242, result

        else:
            return 404
        

    def wait_or_stop(self, key):
        print()

