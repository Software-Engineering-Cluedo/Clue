from tkinter import *
import jsonschema
import json
import os
from pathlib import Path
from src.board import Board

class Game: 
    """
    TO DO 
    implement tiles with images, enhance visuals of the game 
    create refresh function to update tiles 
    add accusation button 
    create accusation window
    
    
    testing
    """
    window=None
    boardObj = None
    boardArr = None
    rows = None
    columns = None
    simple_tile_dict = None
    game_tile_dict = None
    config_dir = str(Path.home()) + "/Clue"


    def __init__(self):
        self.boardObj=Board()
        self.boardArr=self.boardObj.get_tile_map()
        self.rows=len(self.boardArr)
        self.columns=len(self.boardArr[0])
        self.window=Tk()
        self.window.title("Clue!")
        self.data=self.boardObj.data   
        self.simple_tile_dict=self.setup_tile_dict("simple tiles")
        self.game_tile_dict=self.setup_tile_dict("game tiles")
        self.combined_tile_dict=self.simple_tile_dict|self.game_tile_dict
 
        for i in range(self.rows):
            for j in range(self.columns):
                if "name" in self.combined_tile_dict[self.boardArr[i][j]]:
                    currentLabel=Label(self.window, text=str(self.combined_tile_dict[self.boardArr[i][j]]["name"]))
                else:
                    currentLabel=Label(self.window, text=str(self.combined_tile_dict[self.boardArr[i][j]]["obj"]))
                currentLabel.grid(row=i, column=j)    
        print(self.simple_tile_dict)
        print(self.game_tile_dict)
        self.window.mainloop()

    def setup_tile_dict(self, tile_type):
        temp_dict={}
        tiles=self.data[tile_type]
        for tile in tiles: 
            if "char" in tile: 
                temp_dict[tile["char"]]={}
                for k,obj in tile.items():
                    if k != "char":
                        temp_dict[tile["char"]][k]=obj
        return temp_dict


