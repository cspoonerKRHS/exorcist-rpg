import pygame, math, sys
from Block import Block

class level():
    def __init__(self, geoMap, thingMap, screenSize):
        self.blocks = []
        self.fblocks = []
        self.wblocks = []
        geofile = open(geoMap, "r")
        lines = geofile.readlines()
        geofile.close()
        newlines = []
        self.screenWidth = screenSize[0]
        self.screenHeight = screenSize[1]
        self.nspawn = False
        

        for line in lines:
            newline = ""
            for character in line:
                if character != "\n":
                    newline += character
            newlines += [newline]
            
        for y, line in enumerate(newlines):
            for x, c in enumerate(line):
                if c == "w":
                    self.blocks += [Block([(x*10)+5, (y*10)+5], screenSize,"rcs/imgs/block/cobblestone.png",(10,10))]
                if c == " ":
                    self.fblocks += [Block([(x*10)+5, (y*10)+5], screenSize,"rcs/imgs/block/grass.png",(10,10))]
                if c == "c":
                    self.fblocks += [Block([(x*10)+5, (y*10)+5], screenSize,"rcs/imgs/block/wood.png" ,(10,10))]
                if c == "s":
                    self.fblocks += [Block([(x*10)+5, (y*10)+5], screenSize,"rcs/imgs/block/snow.png",(10,10))]
                if c == "r":
                    self.blocks += [Block([(x*10)+5, (y*10)+5], screenSize,"rcs/imgs/block/water2.png",(10,10))]
                if c == "d":
                    self.fblocks += [Block([(x*10)+5, (y*10)+5], screenSize,"rcs/imgs/block/dirt.png",(10,10))]
                if c == "f":
                    self.fblocks += [Block([(x*10)+5, (y*10)+5], screenSize,"rcs/imgs/block/sstone.png",(10,10))]
                if c == "o":
                    self.fblocks += [Block([(x*10)+5, (y*10)+5], screenSize,"rcs/imgs/block/incobblestone.png",(10,10))]
                if c == "p":
                    self.dblocks += [Block([(x*10)+5, (y*10)+5], screenSize,"rcs/imgs/block/spawnspace.png",(10,10))]
                
                
                    
        #----Done with file---
        
        thingfile = open(thingMap, "r")
        lines = thingfile.readlines()
        thingfile.close() 
        
    def wallCollide(self, other):
        if (self.rect.right > other.rect.left 
            and self.rect.left < other.rect.right):
            if (self.rect.bottom > other.rect.top and 
                self.rect.top < other.rect.bottom): 
                    other.speed[0] = other.speed[0] = 0
                    other.speed[1] = other.speed[1] = 0 
                    
    def Collide(self, other):
        if self.go == True:
            if (self.rect.right > other.rect.left 
                and self.rect.left < other.rect.right):
                if (self.rect.bottom > other.rect.top and 
                    self.rect.top < other.rect.bottom): 
                        self.nspawn = True
                        self.go = False