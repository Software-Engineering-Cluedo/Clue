from src.carddeck import CardDeck


class Player():
    hand = CardDeck()
    name = None
    symbol = None
    player_id = None


    def __init__(self, name, player_id, symbol):
        self.name = name
        self.symbol = symbol
        self.player_id = player_id
    

    def add_to_hand(self, card_deck):
        self.hand.add_card(card_deck.pop_card())
    

    def check_hand(self, card):
        # Used for the user to the left who is being questioned to check if they have a card mentioned
        print()
    

    def suggest(self, current_room, weapon, player_card):
        # Would move the weapon and player token (derrived from player card) to the room the player is currently in
        # It would perform the checks according to the instructions and return either false or the cards correctly guessed
        print()

    
    def accuse(self, room, weapon, player_card):
        # Simular to suggest, but sets the state of the player to stopped if incorrect and returns false, if correct returns true and ends the game
        print()
