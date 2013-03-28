import pygame, math, sys, time
from Block import Block
from LevelBlock import LevelBlock

class Level():
    def __init__(self, level, screenSize):
        self.screenSize = screenSize
        self.screenWidth = screenSize[0]
        self.screenHeight = screenSize[1]
        self.load(level)
        
        
    def load(self, level):
        st = time.time()
        geoMap="rcs/maps/"+ level +".lvl"
        thingMap="rcs/maps/"+ level +".tng"
        self.level = level
        self.blocks = []
        self.lockblocks = []
        self.lock2blocks = []
        self.floorblocks = []
        self.wblocks = []
        self.hpblocks = []
        self.darkblocks = []
        self.killblocks = []
        self.enemyblocks = []
        self.mblocks = []
        self.oblocks = []
        geofile = open(geoMap, "r")
        lines = geofile.readlines()
        geofile.close()
        newlines = []
        self.nspawn = False
        

        for line in lines:
            newline = ""
            for character in line:
                if character != "\n":
                    newline += character
            newlines += [newline]
            
        for y, line in enumerate(newlines):
            for x, c in enumerate(line):
                if c == "W":
                    self.blocks += [Block([(x*10)+5, (y*10)+5], 
                                           self.screenSize,
                                           "rcs/imgs/block/cobblestone.png",
                                           (10,10)
                                           )]
                if c == "w":
                    self.floorblocks += [Block([(x*10)+5, (y*10)+5], 
                                           self.screenSize,
                                           "rcs/imgs/block/cobblestone.png",
                                           (10,10)
                                           )]
#                if c == " ":
#                    self.floorblocks += [Block([(x*10)+5, (y*10)+5], 
#                                            self.screenSize,
#                                            "rcs/imgs/block/grass.png",
#                                            (10,10)
#                                            )]
                if c == "c":
                    self.floorblocks += [Block([(x*10)+5, (y*10)+5],
                                            self.screenSize,
                                            "rcs/imgs/block/wood.png",
                                            (10,10)
                                            )]
                if c == "s":
                    self.floorblocks += [Block([(x*10)+5, (y*10)+5],
                                            self.screenSize,
                                            "rcs/imgs/block/snow.png",
                                            (10,10)
                                            )]
                if c == "r":
                    self.blocks += [Block([(x*10)+5, (y*10)+5],
                                            self.screenSize,
                                            "rcs/imgs/block/water2.png",
                                            (10,10)
                                            )]
                if c == "d":
                    self.floorblocks += [Block([(x*10)+5, (y*10)+5],
                                            self.screenSize,
                                            "rcs/imgs/block/dirt.png",
                                            (10,10)
                                            )]
                if c == "f":
                    self.floorblocks += [Block([(x*10)+5, (y*10)+5],
                                            self.screenSize,
                                            "rcs/imgs/block/sstone.png",
                                            (10,10)
                                            )]
                if c == "o":
                    self.floorblocks += [Block([(x*10)+5, (y*10)+5],
                                            self.screenSize,
                                            "rcs/imgs/block/incobblestone.png",
                                            (10,10)
                                            )]
                if c == "O":
                    self.floorblocks += [Block([(x*10)+25, (y*10)+25],
                                            self.screenSize,
                                            "rcs/imgs/block/bigincobblestone.png",
                                            (50,50)
                                            )]
                if c == "b":
                    self.killblocks += [Block([(x*10)+5, (y*10)+5],
                                            self.screenSize,
                                            "rcs/imgs/block/lava.png",
                                            (10,10)
                                            )]
                if c == "g":
                    self.floorblocks += [Block([(x*10)+5, (y*10)+5],
                                            self.screenSize,
                                            "rcs/imgs/block/deadlava.png",
                                            (10,10)
                                            )]
                if c == "B":
                    self.killblocks += [Block([(x*10)+25, (y*10)+25],
                                            self.screenSize,
                                            "rcs/imgs/block/biglava.png",
                                            (50,50)
                                            )]
                if c == "5":
                    self.killblocks += [Block([(x*10)+5, (y*10)+5],
                                            self.screenSize,
                                            "rcs/imgs/block/black.png",
                                            (10,10)
                                            )]
                if c == "l":
                    self.floorblocks += [Block([(x*10)+5, (y*10)+5],
                                            self.screenSize,
                                            "rcs/imgs/block/pitcobblestone.png",
                                            (10,10)
                                            )]
                if c == "t":
                    self.floorblocks += [Block([(x*10)+5, (y*10)+5],
                                            self.screenSize,
                                            "rcs/imgs/block/pit2cobblestone.png",
                                            (10,10)
                                            )]
                if c == "y":
                    self.blocks += [Block([(x*10)+5, (y*10)+5],
                                            self.screenSize,
                                            "rcs/imgs/block/pit3cobblestone.png",
                                            (10,10)
                                            )]
                
                
                
                
                    
        #----Done with file---
        
        thingfile = open(thingMap, "r")
        lines = thingfile.readlines()
        thingfile.close() 
        
        newlines = []
        
        for line in lines:
            newline = ""
            for character in line:
                if character != "\n":
                    newline += character
            newlines += [newline]
            
        for y, line in enumerate(newlines):
            for x, c in enumerate(line):
                if c == "p":
                    self.darkblocks += [Block([(x*10)+5, (y*10)+5], 
                                            self.screenSize,
                                            "rcs/imgs/block/spawnspace.png",
                                            (10,10)
                                            )]
                if c == "r":
                    self.enemyblocks += [Block([(x*10)+5, (y*10)+5], 
                                            self.screenSize,
                                            "rcs/imgs/block/spawnspace.png",
                                            (10,10)
                                            )]
                if c == "A":
                    self.enemyblocks += [Block([(x*10)+5, (y*10)+5], 
                                            self.screenSize,
                                            "rcs/imgs/block/spawnspace.png",
                                            (10,10)
                                            )]
                if c == "N":
                    self.mblocks += [LevelBlock([(x*10)+5, (y*10)+5], 
                                            self.screenSize,
                                            "rcs/imgs/block/spawnspace.png",
                                            (10,10), 
                                            self.levelLoader(c),
                                            [(x*10)+5, self.screenSize[1]],
                                            c)]
                if c == "1":
                    self.mblocks += [LevelBlock([(x*10)+5, (y*10)+5], 
                                            self.screenSize,
                                            "rcs/imgs/block/spawnspace.png",
                                            (10,10), 
                                            self.levelLoader(c),
                                            [(x*10)+5, self.screenSize[1]],
                                            c)]
                if c == "2":
                    self.mblocks += [LevelBlock([(x*10)+5, (y*10)+5], 
                                            self.screenSize,
                                            "rcs/imgs/block/spawnspace.png",
                                            (10,10), 
                                            self.levelLoader(c),
                                            [(x*10)+5, self.screenSize[1]],
                                            c)]
                if c == "3":
                    self.mblocks += [LevelBlock([(x*10)+5, (y*10)+5], 
                                            self.screenSize,
                                            "rcs/imgs/block/spawnspace.png",
                                            (10,10), 
                                            self.levelLoader(c),
                                            [(x*10)+5, self.screenSize[1]],
                                            c)]
                if c == "4":
                    self.mblocks += [LevelBlock([(x*10)+5, (y*10)+5], 
                                            self.screenSize,
                                            "rcs/imgs/block/spawnspace.png",
                                            (10,10), 
                                            self.levelLoader(c),
                                            [(x*10)+5, self.screenSize[1]],
                                            c)]
                if c == "S":
                    self.mblocks += [LevelBlock([(x*10)+5, (y*10)+5], 
                                            self.screenSize,
                                            "rcs/imgs/block/spawnspace.png",
                                            (10,10), 
                                            self.levelLoader(c),
                                            [(x*10)+5, 0],
                                            c)]
                if c == "k":
                    self.lockblocks += [Block([(x*10)+5, (y*10)+5],
                                            self.screenSize,
                                            "rcs/imgs/block/keyhole.png",
                                            (10,10)
                                            )] 
                if c == "K":
                    self.lock2blocks += [Block([(x*10)+5, (y*10)+5],
                                            self.screenSize,
                                            "rcs/imgs/block/2keyhole.png",
                                            (10,10)
                                            )] 
                if c == "j":
                    self.oblocks += [Block([(x*10)+5, (y*10)+5],
                                            self.screenSize,
                                            "rcs\imgs\key\key.png",
                                            (15,7)
                                            )]
                if c == "h":
                    self.lockblocks += [Block([(x*10)+5, (y*10)+5],
                                            self.screenSize,
                                            "rcs/imgs/block/wall.png",
                                            (10,10)
                                            )] 


    def levelLoader(self, dir):
        if self.level == "map1":
            if dir == "N":
                return "map2"
                print "someting"
        if self.level == "map2":
            if dir == "S":
                return "map1"
                print "someting"
        if self.level == "map4":
            if dir == "2":
                return "map2"
                print "someting"
        if self.level == "map2":
            if dir == "1":
                return "map4"
                print "someting"
        if self.level == "map4":
            if dir == "3":
                return "map5"
                print "someting"
        if self.level == "map5":
            if dir == "4":
                return "map4"
                print "someting"
        if self.level == "map5":
            if dir == "5":
                return "map6"
                print "someting"
                
               