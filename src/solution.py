import random


class Solution:
    room = None
    player_card = None
    weapon = None


    def __init__(self, room, player_card, weapon):
        self.room = room
        self.player_card = player_card
        self.weapon = weapon


    def set_solution(self, room, player_card, weapon):
        """ Used for testing, sets the solution attributes """

        self.room = room
        self.player_card = player_card
        self.weapon = weapon

    
    def get_solution(self):
        """ Used for testing, gets the solution attributes """

        return self.room, self.player_card, self.weapon


    def check_solution(self, r_guess, p_guess, w_guess):
        """ Checks if the given solution is correct """

        return (w_guess == self.w and p_guess == self.p and r_guess == self.r)