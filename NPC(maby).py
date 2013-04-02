import pygame, math, sys, random

class NPC():
    def __init__(self, speed, position):
        self.surfaces = []
        self.frame = 0
        self.maxFrame = len(self.surfaces)-1
        self.surface = self.surfaces[self.frame]
        self.rect = self.surface.get_rect()
        self.speed = speed
        self.place(position)
        self.living = True
        
#    def  __str__(self):
#        return "I'm a NPC " + str(self.rect.center) + str(self.speed) + str(self.living)
     
	def place(self, pt):
        self.rect.center = pt
		
    def dir(self, dir):
        if self.speed[1] < 0:
            self.dir = "up"
        elif self.speed[1] > 0:
            self.dir = "down"
        elif self.speed[0] < 0:
            self.dir = "left"
        elif self.speed[0] > 0:
            self.dir = "right"
        
    def move(self):
        if self.dir == "up":
            self.surfaces = self.upimgs
        if self.dir == "down":
            self.surfaces = self.downimgs
        if self.dir == "left":
            self.surfaces = self.leftimgs
        if self.dir == "right":
            self.surfaces = self.rightimgs
    
	def distToPoint(self, pt):
		x1 = self.rect.center[0]
        x2 = pt[0]
        y1 = self.rect.center[1]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    
    def collide(self, other):
        print "trying to hit other", screenHeight
    
    def collideWall(self, screenWidth, screenHeight):
        if (self.rect.left < 0 
            or self.rect.right > self.screenWidth):
                self.speed[0] = self.speed[0]*-1
        if (self.rect.top < 0 
            or self.rect.bottom >self.screenHeight):
                self.speed[1] = self.speed[1]* -1
        