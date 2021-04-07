from src.room import Room
from src.player import Player
from src.weapon import Weapon

class Solution:
    r = None
    p = None
    w = None

    def __init__(self):
        solution = self.generateSolution()
        self.r = solution[0]
        self.p = solution[1]
        self.w = solution[2]

    def generateSolution(): 
        #TO DO
        #randomly select one room, one player, one weapon 
        r = None
        p = None
        w = None
        return r, p, w
    
    def checkSolution(wGuess, pGuess, rGuess):
        if (wGuess == self.w or pGuess == self.p or rGuess == self.r):
            return True
        else:
            return False
        

