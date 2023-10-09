from Tile import *
import numpy as np
from Colors import *
class Map:
    def __init__(self, x, y):
        self.sizeX = x
        self.sizeY = y
        self.tab = [[Tile for i in range(x)] for j in range(y)]

    def check_file(self, file):
        print("Checking the size of the map")
        lines = file.readlines()
        f_y = len(lines)
        f_x = len(lines[0][:-1])
        if f_x == self.sizeX and f_y == self.sizeY:
            print("Size : OK")
            return True
        else:
            print("Size : Error")
            return False

    def file_read(self, file):
        file.seek(0, 0)
        file_cont = str(file.read())
        file_spread = file_cont.split("\n")
        print("Reading the map from source file : "+str(file.name))
        for i in range(self.sizeY):
            for j in range(self.sizeX):
                new_tile = Tile(file_spread[i][j], i, j)
                self.tab[i][j] = new_tile
        print("File read")


    def display(self):
        c = ColorTab()
        for i in range(self.sizeY):
            nextline = ""
            for j in range(self.sizeX):
                nextline = nextline + c.tab[int(self.tab[i][j].nature)] + "██"
            print(nextline)