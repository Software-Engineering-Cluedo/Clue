from src.playercard import PlayerCard
from src.board import Board
from src.room import Room


class Token:
    x = None
    y = None
    card = None
    room = None


    def __init__(self, x, y, card):
        self.set_position(x, y)
        self.set_card(card)


    def set_position(self, x, y):
        self.x = x
        self.y = y


    def get_position(self):
        return x, y


    def set_room(self, room):
        self.room = room


    def get_room(self):
        return self.room


    def set_card(self, card):
        self.card = card

    
    def get_card(self):
        return self.card
    