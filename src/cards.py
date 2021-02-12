import random


class Cards:
    cards = []

    def __init__(self):
        print('todo')

    def add(self, card):
        self.cards.append(card)

    def random(self):
        return random.choice(self.cards)
