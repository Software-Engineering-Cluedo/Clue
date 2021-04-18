from tkinter import *
import jsonschema
import json
import os
from PIL import Image, ImageTk
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
    accuseButton = None

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
        self.generate_img_tiles()
        self.accuseButton=Button(self.window,text="Make accusation?", command=self.generate_accusation_window)
        self.accuseButton.grid(row=24,column=26)
        mainloop()

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

    def generate_img_tiles(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if "img_src" in self.combined_tile_dict[self.boardArr[i][j]]:
                    img_path = Image.open(os.path.dirname(__file__) + '/resources/images/' + self.combined_tile_dict[self.boardArr[i][j]]["img_src"])
                    img=ImageTk.PhotoImage(img_path)
                    currentLabel=Label(self.window, image=img)
                    currentLabel.image=img
                    currentLabel.grid(row=i, column=j)
        return True    

    def generate_accusation_window(self):
        self.accusationWindow=Toplevel(self.window)
        self.accusationWindow.title("Make Accusation")
        listPlayers=["PLAYER1","PLAYER2", "PLAYER3"]
        listWeapons=["gun","knife", "pipe", "hammer"]
        listRooms=["ballroom","lounge", "study","hall","kitchen"]
        Label(self.accusationWindow, text = "Character:").grid(row=1,column=1, padx=40,pady=20)
        Label(self.accusationWindow, text = "Weapon:").grid(row=3,column=1, padx=40,pady=20)
        Label(self.accusationWindow, text = "Room:").grid(row=5,column=1, padx=40,pady=20)
        Button(self.accusationWindow, text = "Submit", command=print("submit")).grid(row=7,column=5,padx=10,pady=10)
        OptionMenu(self.accusationWindow, listPlayers[0],*listPlayers).grid(row=1,column=3)
        OptionMenu(self.accusationWindow, listWeapons[0],*listWeapons).grid(row=3,column=3)
        OptionMenu(self.accusationWindow, listRooms[0],*listRooms).grid(row=5,column=3)
        #positioning at the end as it is based on dimensions that will change as elements are added 
        widthParent=self.window.winfo_width()
        lengthParent=self.window.winfo_height()
        widthChild=self.accusationWindow.winfo_width()
        lengthChild=self.accusationWindow.winfo_height()
        x=int(self.window.winfo_x()+(widthParent/2)-(widthChild/2))
        y=int(self.window.winfo_y()+(lengthParent/2)-(lengthChild/2))
        self.accusationWindow.geometry("+{}+{}".format(x,y))

