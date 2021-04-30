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
        """ Used for testing, gets the solution attributes 
            Returns: 
                tuple: room, player and weapon. 
        """

        return self.room, self.player_card, self.weapon


    def check_solution(self, r_guess, p_guess, w_guess):
        """ Checks if the given solution is correct 
            Args: 
                r_guess: the guessed room
                p_guess: the guessed player 
                w_guess: the guessed weapon
            Returns: 
                boolean: true if each guess is correct, false otherwise. 
        
        """
        return (w_guess == list(self.weapon.values())[0] and p_guess == list(self.player_card.values())[0] and r_guess == list(self.room.values())[0])