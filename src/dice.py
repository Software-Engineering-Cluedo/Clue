import random

class Dice():
    def roll(self):
        """Rolls two dice, could of just been one randrange but too late now
        
        Returns:
            int: num between 1 and 6, including
            int: num between 1 and 6, including
        """
        return random.randrange(1,7), random.randrange(1,7)
