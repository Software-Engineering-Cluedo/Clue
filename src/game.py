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

    
    testing
    """
    window=None
    boardObj = None
    boardArr = None
    rows = None
    columns = None
    simpleTileDict = None
    gameTileDict = None
    accuseButton = None
    childWindowOpen = None
    boardTileImgs = None
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
        self.simpleTileDict=self.setup_tile_dict("simple tiles")
        self.gameTileDict=self.setup_tile_dict("game tiles")
        self.combinedTileDict=self.simpleTileDict|self.gameTileDict
        self.boardTileImgs=[]
        self.generate_board_tiles()
        self.generate_character_tiles()
        self.generate_door_tiles()
        self.generate_weapon_tiles()
        self.output_tile_images()
        self.accuseButton=Button(self.window,text="Make accusation?", command=self.generate_accusation_window)
        self.accuseButton.grid(row=24,column=26)
        mainloop()

    def setup_tile_dict(self, tile_type):
        tempDict={}
        tiles=self.data[tile_type]
        for tile in tiles: 
            if "char" in tile: 
                tempDict[tile["char"]]={}
                for k,obj in tile.items():
                    if k != "char":
                        tempDict[tile["char"]][k]=obj
        return tempDict

    def generate_board_tiles(self): 
        #extend for walking tiles
        for i in range(self.rows):
            self.boardTileImgs.append([])
            for j in range(self.columns):
                if "img_src" in self.combinedTileDict[self.boardArr[i][j]]:
                    surroundingTiles=self.boardObj.get_surrounding(j,i,self.boardArr)
                    currentTile=surroundingTiles[1][1]
                    surroundingTilesValues=[surroundingTiles[0][1],surroundingTiles[1][2],surroundingTiles[2][1],surroundingTiles[1][0]]
                    wallPresent=[surroundingTiles[0][1]==currentTile,surroundingTiles[1][2]==currentTile,surroundingTiles[2][1]==currentTile,surroundingTiles[1][0]==currentTile]
                    description="_tile_"
                    if self.combinedTileDict[self.boardArr[i][j]]["obj"]=="room" or self.combinedTileDict[self.boardArr[i][j]]["obj"]=="tile":
                        if not wallPresent[0]:
                            description+="top_"
                        if not wallPresent[2]:
                            description+="bottom_"
                        if not wallPresent[3]:
                            description+="left_"
                        if not wallPresent[1]:
                            description+="right_"
                        if description=="_tile_":
                            description+="borderless.jpg"
                        else:
                            description+="border.jpg"
                        imgName=self.combinedTileDict[self.boardArr[i][j]]["img_src"]+description
                        img_path = Image.open(self.config_dir + '/images/' + imgName)
                    else: 
                        img_path = Image.open(self.config_dir + '/images/' + self.combinedTileDict[self.boardArr[i][j]]["img_src"])
                self.boardTileImgs[i].append(img_path)
        return True    

    def generate_character_tiles(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.boardObj.player_map[i][j]!="":
                    print(self.boardObj.player_map[i][j])
                    self.boardTileImgs[i][j]=Image.open(self.config_dir + '/images/' + self.combinedTileDict[self.boardObj.player_map[i][j]]["img_src"])
    
    def generate_door_tiles(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.boardObj.door_map[i][j]!="":
                    self.boardTileImgs[i][j]=Image.open(self.config_dir + '/images/' + self.combinedTileDict[self.boardObj.door_map[i][j]]["img_src"])
    
    def generate_weapon_tiles(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.boardObj.weapon_map[i][j]!="":
                    self.boardTileImgs[i][j]=Image.open(self.config_dir + '/images/' + self.combinedTileDict[self.boardObj.weapon_map[i][j]]["img_src"])

    def output_tile_images(self):
        for i in range(self.rows):
            for j in range(self.columns):
                    img=ImageTk.PhotoImage(self.boardTileImgs[i][j])
                    currentLabel=Label(self.window, image=img)
                    currentLabel.image=img
                    currentLabel.grid(row=i, column=j)
    
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
            x=int(self.window.winfo_x()+(self.window.winfo_width()/2)-(self.accusationWindow.winfo_width()/2))
            y=int(self.window.winfo_y()+(self.window.winfo_height()/2)-(self.accusationWindow.winfo_height()/2))
            self.accusationWindow.geometry("+{}+{}".format(x,y))
            self.childWindowOpen=True

    def submit_accusation(self):
        print(self.accusationWindow.accusedPlayer.get(),self.accusationWindow.accusedRoom.get(),self.accusationWindow.accusedWeapon.get())
        self.accusationWindow.destroy()
        self.childWindowOpen=False
