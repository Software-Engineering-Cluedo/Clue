from src.boardtoken import Token


class PlayerToken(Token):
    board = None
    current_room = None
    door_entered = None

    def __init__(self, x, y, card, board):
        super().__init__(x, y, card)
        self.board = board


    def move(self, x, y):
        self.x = x
        self.y = y
    

    def move_by_direction(self):
        print()


    def enter_door():
        print()


    def enter_secret_door():
        print()
    

    def exit_door():
        print()
    

    def exit_secret_door():
        print()