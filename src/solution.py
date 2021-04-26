import random

from src.room import Room
from src.player import Player
from src.weapon import Weapon


class Solution:
    r = None
    p = None
    w = None


    def __init__(self, rooms, player_cards, weapons):
        self.r, self.p, self.w = self.generate_solution(weapons, player_cards, weapons)


    def generate_solution(self, rooms, player_cards, weapons):
        """ Generates the solution from each type of card """

        if rooms != None and player_cards != None and weapons != None:
            r = random.choice(list(rooms.items()))[1]
            p = random.choice(list(player_cards.items()))[1]
            w = random.choice(list(weapons.items()))[1]

            return r, p, w
        else:
            return False, False, False


    def set_solution(self, r, p, w):
        """ Used for testing, sets the solution attributes """

        self.r = r
        self.p = p
        self.w = w


    def check_solution(self, r_guess, p_guess, w_guess):
        """ Checks if the given solution is correct """

        return (w_guess == self.w and p_guess == self.p and r_guess == self.r)