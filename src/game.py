from tkinter import *
import jsonschema
from pathlib import Path
from src.board import Board

class Game:
    window=None
    boardObj = None
    boardArr = None
    rows = None
    columns = None

    def __init__(self):
        self.boardObj=Board()
        self.boardArr=self.boardObj.get_tile_map()
        self.rows=len(self.boardArr)
        self.columns=len(self.boardArr[0])
        self.window=Tk()
        self.window.title("Clue!")
        for i in range(self.rows):
            for j in range(self.columns):
                currentLabel=Label(self.window, text=str(self.boardArr[i][j]))
                currentLabel.grid(row=i, column=j)
        self.window.mainloop()


