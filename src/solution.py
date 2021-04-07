from src.room import Room
from src.player import Player
from src.weapon import Weapon

class Solution:
    def __init__(self):
        solution=generateSolution
        Room self.r = solution[0]
        Player self.p = solution[1]
        Weapon self.w = solution[2]

    def generateSolution(): 
        #TO DO
        #randomly select one room, one player, one weapon 
        r=null
        p=null
        w=null
        return ([r,p,w]); 
    
    def checkSolution(wGuess, pGuess, rGuess):
        if (wGuess==w or pGuess==p or rGuess=r):
            return True
        else:
            return False
        

