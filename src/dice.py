import random

class Dice():
    def roll(self):
        return random.randrange(1,7), random.randrange(1,7)