from tkinter import *
import jsonschema
import json
import os
import shutil
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
    childWindowOpen = None
    config_dir = str(Path.home())+"/Clue"

    def __init__(self):
        self.boardObj=Board()
        self.boardArr=self.boardObj.tile_map
        self.rows=len(self.boardArr)
        self.columns=len(self.boardArr[0])
        self.childWindowOpen=False
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
                    img_path = Image.open(self.config_dir + '/images/' + self.combined_tile_dict[self.boardArr[i][j]]["img_src"])
                    img=ImageTk.PhotoImage(img_path)
                    currentLabel=Label(self.window, image=img)
                    currentLabel.image=img
                    currentLabel.grid(row=i, column=j)
        return True    

    def generate_accusation_window(self):
        if self.childWindowOpen==False:
            self.accusationWindow=Toplevel(self.window)
            self.accusationWindow.title("Make Accusation")
            
            listPlayers=self.boardObj.get_tile_names(self.boardObj.player_cards)
            listWeapons=self.boardObj.get_tile_names(self.boardObj.weapons)
            listRooms=self.boardObj.get_tile_names(self.boardObj.rooms)
            
            Label(self.accusationWindow, text = "Character:").grid(row=1,column=1, padx=40,pady=20)
            Label(self.accusationWindow, text = "Weapon:").grid(row=3,column=1, padx=40,pady=20)
            Label(self.accusationWindow, text = "Room:").grid(row=5,column=1, padx=40,pady=20)
            Button(self.accusationWindow, text = "Submit", command=self.submit_accusation).grid(row=7,column=5,padx=10,pady=10)

            self.accusationWindow.accusedPlayer= StringVar(self.accusationWindow,listPlayers[0])
            self.accusationWindow.accusedWeapon= StringVar(self.accusationWindow,listWeapons[0])
            self.accusationWindow.accusedRoom=StringVar(self.accusationWindow,listRooms[0])

            self.accusationWindow.playerOption=OptionMenu(self.accusationWindow,  self.accusationWindow.accusedPlayer,*listPlayers).grid(row=1,column=3)
            self.accusationWindow.weaponOption=OptionMenu(self.accusationWindow,  self.accusationWindow.accusedWeapon,*listWeapons).grid(row=3,column=3)
            self.accusationWindow.roomOption=OptionMenu(self.accusationWindow,  self.accusationWindow.accusedRoom,*listRooms).grid(row=5,column=3)
            y=int(self.window.winfo_y()+(self.window.winfo_height()/2)-(self.accusationWindow.winfo_height()/2))
            x=int(self.window.winfo_x()+(self.window.winfo_width()/2)-(self.accusationWindow.winfo_width()/2))
            self.accusationWindow.geometry("+{}+{}".format(x,y))
            self.childWindowOpen=True

    def submit_accusation(self):
        print(self.accusationWindow.accusedPlayer.get(),self.accusationWindow.accusedRoom.get(),self.accusationWindow.accusedWeapon.get())
        self.accusationWindow.destroy()
        self.childWindowOpen=False
