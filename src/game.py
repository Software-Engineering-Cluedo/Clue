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
    suggestButton=None
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

        """creates a dictionary of all the possible tiles""" 
        self.simpleTileDict=self.setup_tile_dict("simple tiles")
        self.gameTileDict=self.setup_tile_dict("game tiles")
        self.combinedTileDict=self.simpleTileDict|self.gameTileDict

        """generates all the tiles as grids of image references""" 
        self.boardTileImgs=[]
        self.generate_board_tiles()
        self.generate_character_tiles()
        self.generate_door_tiles()
        self.generate_weapon_tiles()

        """puts all the images into the grid in the parent tkinter window"""
        self.output_tile_images() 

        """generate suggestion and accusation buttons"""
        self.suggestButton=Button(self.window,text="Make suggestion?", command=lambda: self.generate_suggest_accuse_window("suggest"))
        self.suggestButton.grid(row=0,column=26)
        self.accuseButton=Button(self.window,text="Make accusation?", command=lambda: self.generate_suggest_accuse_window("accuse"))
        self.accuseButton.grid(row=1,column=26)
        mainloop() #generates the window

    def setup_tile_dict(self, tile_type):
        """creates a dictionary of dictionaries to keep track of the different tile types
        
        Args:
            tile_type: the type of tile i.e. simple tile of game tile
        
        Returns: 
            dict: dictionary within dictionary where every first key is the tile character, 
            and its attributes are in the value dictionary assigned to it. 

        """
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
        """ Creates a 2d list in which each element corresponds to the image name for the tile in that space

            Returns: 
                bool: true if tile images have been successfully returned in the 2d list

        """
        for i in range(self.rows):
            self.boardTileImgs.append([])
            for j in range(self.columns):
                if "img_src" in self.combinedTileDict[self.boardArr[i][j]]:
                    surroundingTiles=self.boardObj.get_surrounding(j,i,self.boardObj.tile_map)
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
        """
            Overwrites tiles with character tile images over the existing board image tiles
        """
        for i in range(self.rows):
            for j in range(self.columns):
                if self.boardObj.player_map[i][j]!="":
                    self.boardTileImgs[i][j]=Image.open(self.config_dir + '/images/' + self.combinedTileDict[self.boardObj.player_map[i][j]]["img_src"])
    
    def generate_door_tiles(self):
        """
            Overwrites tiles with door tile images over the existing board image tiles
        """
        for i in range(self.rows):
            for j in range(self.columns):
                if self.boardObj.door_map[i][j]!="":
                    self.boardTileImgs[i][j]=Image.open(self.config_dir + '/images/' + self.combinedTileDict[self.boardObj.door_map[i][j]]["img_src"])
    
    def generate_weapon_tiles(self):
        """
            Overwrites tiles with weapon tile images over the existing board image tiles
        """
        for i in range(self.rows):
            for j in range(self.columns):
                if self.boardObj.weapon_map[i][j]!="":
                    self.boardTileImgs[i][j]=Image.open(self.config_dir + '/images/' + self.combinedTileDict[self.boardObj.weapon_map[i][j]]["img_src"])

    def output_tile_images(self):
        """
            places the images in the 2d list into the tkinter window in the correct grid order 
        """
        for i in range(self.rows):
            for j in range(self.columns):
                    img=ImageTk.PhotoImage(self.boardTileImgs[i][j])
                    currentLabel=Label(self.window, image=img)
                    currentLabel.image=img
                    currentLabel.grid(row=i, column=j)
    
    def generate_suggest_accuse_window(self,name):
        """
            creates a tkinter child window that will allow for suggestion or accusations to be fed into a later function 
        """
        if self.childWindowOpen==False:
            self.suggestaccusewindow=Toplevel(self.window)
            if name=="accuse":
                self.suggestaccusewindow.title("Make Accusation")
            elif name=="suggest":
                self.suggestaccusewindow.title("Make Suggestion")
            self.suggestaccusewindow.windowtype=name
            
            listPlayers=self.boardObj.get_tile_names(self.boardObj.player_cards)
            listWeapons=self.boardObj.get_tile_names(self.boardObj.weapons)
            listRooms=self.boardObj.get_tile_names(self.boardObj.rooms)

            Label(self.suggestaccusewindow, text = "Character:").grid(row=1,column=1, padx=40,pady=20)
            Label(self.suggestaccusewindow, text = "Weapon:").grid(row=3,column=1, padx=40,pady=20)
            Label(self.suggestaccusewindow, text = "Room:").grid(row=5,column=1, padx=40,pady=20)
            Button(self.suggestaccusewindow, text = "Submit", command=self.submit_accusation).grid(row=7,column=5,padx=10,pady=10)

            self.suggestaccusewindow.accusedPlayer= StringVar(self.suggestaccusewindow,listPlayers[0])
            self.suggestaccusewindow.accusedWeapon= StringVar(self.suggestaccusewindow,listWeapons[0])
            self.suggestaccusewindow.accusedRoom=StringVar(self.suggestaccusewindow,listRooms[0])

            self.suggestaccusewindow.playerOption=OptionMenu(self.suggestaccusewindow,  self.suggestaccusewindow.accusedPlayer,*listPlayers).grid(row=1,column=3)
            self.suggestaccusewindow.weaponOption=OptionMenu(self.suggestaccusewindow,  self.suggestaccusewindow.accusedWeapon,*listWeapons).grid(row=3,column=3)
            self.suggestaccusewindow.roomOption=OptionMenu(self.suggestaccusewindow,  self.suggestaccusewindow.accusedRoom,*listRooms).grid(row=5,column=3)
            x=int(self.window.winfo_x()+(self.window.winfo_width()/2)-(self.suggestaccusewindow.winfo_width()/2))
            y=int(self.window.winfo_y()+(self.window.winfo_height()/2)-(self.suggestaccusewindow.winfo_height()/2))
            self.suggestaccusewindow.geometry("+{}+{}".format(x,y))
            self.childWindowOpen=True

    def submit_accusation(self):
    
        if self.suggestaccusewindow.windowtype=="suggest": 
            #this can later be replaced with the necessary function
            print(self.suggestaccusewindow.windowtype,self.suggestaccusewindow.accusedPlayer.get(),self.suggestaccusewindow.accusedRoom.get(),self.suggestaccusewindow.accusedWeapon.get())
        elif self.suggestaccusewindow.windowtype=="accuse":
            #this can later be replaced with the necessary function
            print(self.suggestaccusewindow.windowtype,self.suggestaccusewindow.accusedPlayer.get(),self.suggestaccusewindow.accusedRoom.get(),self.suggestaccusewindow.accusedWeapon.get())
        self.suggestaccusewindow.destroy()
        self.childWindowOpen=False
