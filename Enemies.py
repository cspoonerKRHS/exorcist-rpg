import pygame, math, sys, random

class Enemy():
    def __init__(self, images, speed, screenSize, position, waitMax = 1000):
        self.surfaces = []
        for image in images:
            self.surfaces += [pygame.image.load(image)]
        self.frame = 0
        self.maxFrame = len(self.surfaces) - 1
        self.waitCount = 0
        self.waitMax = waitMax
        self.surface = self.surfaces[self.frame]
        self.rect = self.surface.get_rect()
        self.speed = speed
        self.place(position)
        self.screenWidth = screenSize[0]
        self.screenHeight = screenSize[1]
        self.living = 0
        self.health = 10
        self.detectRadius = 100
        
    def  __str__(self):
        pass
#        return "I'm a Enemy " + str(self.rect.center) + str(self.speed) + str(self.living)
     
    def place(self, pt):
        self.rect.center = pt
#        print "I've moved to", pt
        
    def dir(self, dir):
        pass
#        print "I have change direction" 
        
    def move(self):
#        print "I've moved", self.speed
        self.rect = self.rect.move(self.speed)
        
        if self.waitCount < self.waitMax:
            self.waitCount += 1
        else:
            self.waitCount = 0
            
            if self.frame < self.maxFrame:
                self.frame += 1 
            else:
                self.frame = 0
            self.surface = self.surfaces[self.frame]
        
    
    def distToPoint(self, pt):
#        print "I am this far from it."
        x1 = self.rect.center[0]
        x2 = pt[0]
        y1 = self.rect.center[1]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2))
        
         
    def collideWall(self):
#        print "trying to hit edges of screen", self.screenWidth, self.screenHeight
        if (self.rect.left < 0 
            or self.rect.right > self.screenWidth):
                self.speed[0] = self.speed[0]*-1
        if (self.rect.top < 0 
            or self.rect.bottom >self.screenHeight):
                self.speed[1] = self.speed[1]* -1
   

    def attack(self, other):
        pass
#        print "trying to hit other", str(other)
    
    def shoot(self, other):
        pass
#        print "trying to shoot other", str(other)
    
    def melee(self, other):
        pass
#        print "trying to melee other", str(other)
 
    def playerDetect(self, player):
        if self.distToPoint(player.rect.center) < self.detectRadius:
            if self.rect.center[0] < player.rect.center[0]:
                self.speed[0] = 5
            if self.rect.center[0] > player.rect.center[0]:
                self.speed[0] = -5
            if self.rect.center[1] < player.rect.center[1]:
                self.speed[1] = 5
            if self.rect.center[1] > player.rect.center [1]:
                self.speed[1] = -5