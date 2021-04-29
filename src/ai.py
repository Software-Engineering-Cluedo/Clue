from src.player import Player

class Ai(Player):
    def __init__(self, name, player_id, symbol):
        super().__init__(name, player_id, symbol)
    
    def turn(self, key):
        key = None