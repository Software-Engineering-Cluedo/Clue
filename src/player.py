import random
from src.carddeck import CardDeck


class Player():
    """
    """
    hand = None
    name = None
    symbol = None
    player_id = None
    out = False
    player_token = None


    def __init__(self, name, player_id, symbol):
        self.name = name
        self.symbol = symbol
        self.player_id = player_id
        self.hand = CardDeck()

    
    def set_player_token(self, player_token):
        self.player_token = player_token


    def add_to_hand(self, card_dict):
        """Adds specified card to players hand
            Args: 
                card_dict: reference to the card in the card dictionary
        """
        self.hand.add_card(card_dict)
    

    def check_hand(self, cards):
        """ Checks to see if a user that is being questioned has a card that is mentioned
            Args: 
                cards: the cards that were mentioned
            Returns: 
                either: 
                boolean: false if card does not appear in hand 
                or:
                card: a random card from their hand
        """
        correct_cards = []
        for card in cards:
            if self.hand.has_card(card):
                correct_cards.append(card)
        
        if correct_cards != None:
            return False
        else:
            return random.choice(card)

    
    def toggle_out(self):
        self.out = not self.out


    def suggest(self, player_card, current_room, weapon, left_player, player_tokens, weapon_tokens, board):
        """Allows a player to make a suggestion, moving the weapon and player token to the room the player is in.,
            Checks the suggestions in alignment with the game rules and returns either false or the cards that were guessed. 
            Args:
                player_card: the player suggested 
                current_room: the room the player is in 
                weapon: the weapon suggested 
                left_player: player making the suggestion 
                player_tokens: all players in the current game
                weapon_tokens: all weapons
                board: array of the current set up of the board 
            Returns: 
                either: 
                boolean: false if none of the suggested cards were correct 
                or: 
                cards: the cards that were correct
        """ 
        pass

    
    def accuse(self, player_card, room, weapon):
        """Allows a player to make an accusation, but if the player is incorrect they can no longer play, if they are correct the game is ended. 
            Args:
                player_card: the accused player
                room: the accused room
                weapon: the accused weapon 
            Returns: 
                boolean: true if the accusation is correct, false otherwise. 
        
        """
        pass
