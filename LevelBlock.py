import pygame, math, sys

class LevelBlock(Block):
    def __init__(self, pos, screenSize, image, size, newMap):
        Block.__init__(self, pos, screenSize, image, size)
        self.newMap = newMap
    
    def playerCollide(self, other):
        if (self.rect.right > other.rect.left 
            and self.rect.left < other.rect.right):
            if (self.rect.bottom > other.rect.top and 
                self.rect.top < other.rect.bottom): 
                    return True
        return False


    
#-------------infinite spawn-----------        
#    def playerDetect(self, other):
#        if self.distToPoint(other.rect.center) < self.radius:
#            return True
#        return False