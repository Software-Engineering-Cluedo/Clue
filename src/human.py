import random
from src.player import Player

class Human(Player):
    def __init__(self, name, player_id, symbol):
        super().__init__(name, player_id, symbol)
    

    def suggest(self, player_token_all, player_card_dict, current_room, weapon_token_all, left_player, board):
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
            if left_player.hand.has_card(card):
                correct_cards.append(card)
        
        if correct_cards == []:
            return False
        else:
            random.choice(correct_cards)

    
    def accuse(self, player_card, room, weapon, solution):
        # Simular to suggest, but sets the state of the player to stopped if incorrect and returns false, if correct returns true and ends the game
        return
