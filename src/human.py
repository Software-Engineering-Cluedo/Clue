import random
from src.player import Player

class Human(Player):
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
