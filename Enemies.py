import pygame, math, sys, random

class Enemy():
    def __init__(self, images, speed, screenSize, position, waitMax = 1000):
        self.surfaces = []
        for image in images:
            self.surfaces += [pygame.image.load(image)]
        self.frame = 0
        self.maxFrame = len(self.surfaces)-1
        self.waitCount = 0
        self.waitMax = waitMax
        self.surface = self.surfaces[self.frame]
        self.rect = self.surface.get_rect()
        self.speed = speed
        self.place(position)
        self.screenWidth = screenSize[0]
        self.screenHeight = screenSize[1]
        self.living = True
        
    def  __str__(self):
        return "I'm a Enemy " + str(self.rect.center) + str(self.speed) + str(self.living)
     
    def place(self, pt):
        print "I've moved to", pt
        
    def dir(self, dir):
        print "I have change direction" 
        
    def move(self):
        print "I've moved", self.speed
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
        print "I am this far from it."
    
#    def collide(self, other):
#        print "trying to hit other", screenHeight
#    if (self.rect.right > other.rect.left          
#        and self.rect.left < other.rect.right):
#            self.speed[0] = self.speed[0] * -1
#            self.speed[1] = self.speed[1] * -1
#    if (self.distToPoint(other.rect.center)
#        < self.radius + other.radius): 
#            self.speed[0] = self.speed[0] * -1
#            self.speed[1] = self.speed[1] * -1
#            other.speed[0] = other.speed[0] * -1
#            other.speed[1] = other.speed[1] * -1
    
    def collideWall(self):
        print "trying to hit edges of screen", self.screenWidth, self.screenHeight
        if (self.rect.left < 0 
            or self.rect.right > self.screenWidth):
            self.speed[0] = self.speed[0]*-1
        if (self.rect.top < 0 
            or self.rect.bottom >self.screenHeight):
            self.speed[1] = self.speed[1]*-1
   

    def attack(self, other):
        print "trying to hit other", str(other)
    
    def shoot(self, other):
        print "trying to shoot other", str(other)
    
    def melee(self, other):
        print "trying to melee other", str(other)
        
    def playerDetect(self, other):
        print "trying to detect player", str(other)