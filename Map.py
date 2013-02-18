import pygame, math, sys, time
from Block import Block

class Level():
    def __init__(self, level, screenSize):
        self.screenSize = screenSize
        self.screenWidth = screenSize[0]
        self.screenHeight = screenSize[1]
        self.load(level)
        
        
    def load(self, level):
        stime = time.time()
        btime = []
        
        geoMap="rcs/maps/"+ level +".lvl"
        thingMap="rcs/maps/"+ level +".tng"
        self.level = level
        self.blocks = []
        self.fblocks = []
        self.wblocks = []
        self.dblocks = []
        self.kblocks = []
        self.mblocks = []
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
                bstime = time.time()
                if c == "W":
                    self.blocks += [Block([(x*10)+5, (y*10)+5], 
                                           self.screenSize,
                                           "rcs/imgs/block/cobblestonepath.png",
                                           (10,10)
                                           )]
                elif c == "w":
                    self.fblocks += [Block([(x*10)+5, (y*10)+5], 
                                           self.screenSize,
                                           "rcs/imgs/block/cobblestone.png",
                                           (10,10)
                                           )]
                elif c == " ":
                    self.fblocks += [Block([(x*10)+5, (y*10)+5], 
                                            self.screenSize,
                                            "rcs/imgs/block/grass.png",
                                            (10,10)
                                            )]
                elif c == "c":
                    self.fblocks += [Block([(x*10)+5, (y*10)+5],
                                            self.screenSize,
                                            "rcs/imgs/block/wood.png",
                                            (10,10)
                                            )]
                elif c == "s":
                    self.fblocks += [Block([(x*10)+5, (y*10)+5],
                                            self.screenSize,
                                            "rcs/imgs/block/snow.png",
                                            (10,10)
                                            )]
                elif c == "r":
                    self.blocks += [Block([(x*10)+5, (y*10)+5],
                                            self.screenSize,
                                            "rcs/imgs/block/water2.png",
                                            (10,10)
                                            )]
                elif c == "d":
                    self.fblocks += [Block([(x*10)+5, (y*10)+5],
                                            self.screenSize,
                                            "rcs/imgs/block/dirt.png",
                                            (10,10)
                                            )]
                elif c == "f":
                    self.fblocks += [Block([(x*10)+5, (y*10)+5],
                                            self.screenSize,
                                            "rcs/imgs/block/sstone.png",
                                            (10,10)
                                            )]
                elif c == "o":
                    self.fblocks += [Block([(x*10)+5, (y*10)+5],
                                            self.screenSize,
                                            "rcs/imgs/block/incobblestone.png",
                                            (10,10)
                                            )]
                elif c == "b":
                    self.kblocks += [Block([(x*10)+5, (y*10)+5],
                                            self.screenSize,
                                            "rcs/imgs/block/lava.png",
                                            (10,10)
                                            )]
                betime = time.time() - bstime
                btime += [betime]
                
                
        print btime
        #averageTime = 0
        for t in btime:
            averageTime += t
        print averageTime/len(btime)
                
                
         
        print "blocks loaded", time.time() - stime
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
                    self.dblocks += [Block([(x*10)+5, (y*10)+5], 
                                            self.screenSize,
                                            "rcs/imgs/block/spawnspace.png",
                                            (10,10)
                                            )]
                if c == "N":
                    self.mblocks += [Block([(x*10)+5, (y*10)+5], 
                                            self.screenSize,
                                            "rcs/imgs/block/spawnspace.png",
                                            (10,10), 
                                            self.levelLoader(c))]
        
    def levelLoader(self, dir):
        if self.level == "map1":
            if self.dir == "N":
                return "map2"
                print "someting"
               