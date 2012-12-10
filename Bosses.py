import pygame, math, sys, random

class Boss():
    def __init__(self, images, speed, screenSize, position):
        self.surfaces = []
        for image in images:
            self.surfaces += [pygame.image.load(image)]
        self.frame = 0
        self.maxFrame = len(self.surfaces)-1
        self.surface = self.surfaces[self.frame]
        self.rect = self.surface.get_rect()
        self.speed = speed
        self.place(position)
        self.screenWidth = screenSize[0]
        self.screenHeight = screenSize[1]
        self.living = True
        
    def  __str__(self):
        return "I'm a Bosses " + str(self.rect.center) + str(self.speed) + str(self.living)
     
    def place(self, pt):
        print "I've moved to", pt
        
    def dir(self, dir):
        print "I have change direction"
        
    def move(self):
        print "I've moved", self.speed
    
    def distToPoint(self, pt):
        print "I am this far from it."
    
    def collide(self, other):
        print "trying to hit other", self.screenHeight
    
    def collideWall(self):
        print "trying to hit edges of screen", self.screenWidth, self.screenHeight
        
    def playerDetect(self, other):
        print "rying to detect player", str(other)
        
    def attack(self, other):
        print "trying to hit other", str(other)
    
    def shoot(self, other):
        print "trying to shoot other", str(other)
    
    def melee(self, other):
        print "trying to melee other", str(other)        