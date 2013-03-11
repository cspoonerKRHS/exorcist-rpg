import pygame, math, sys
from Block import Block

class LevelBlock(Block):
    def __init__(self, pos, screenSize, image, size, newMap, dest, dir):
        Block.__init__(self, pos, screenSize, image, size)
        self.newMap = newMap
        self.dest = dest
        self.dir = dir
    
    def playerCollide(self, other):
        if (self.rect.right > other.rect.left 
            and self.rect.left < other.rect.right):
            if (self.rect.bottom > other.rect.top and 
                self.rect.top < other.rect.bottom): 
                #print "I'm going to ", self.newMap
                return True
        return False


    
#-------------infinite spawn-----------        
#    def playerDetect(self, other):
#        if self.distToPoint(other.rect.center) < self.radius:
#            return True
#        return False