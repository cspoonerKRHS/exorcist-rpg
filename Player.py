import pygame, math, sys, random

class Player():
    def __init__(self, images, speed, screenSize, position):
        self.surfaces = []
        for image in images:
            self.surfaces += [pygame.image.load(image)]
        self.frame = 0
        self.maxFrame = len(self.surfaces)-1
        self.surface = self.surfaces[self.frame]
        self.rect = self.surface.get_rect()
        self.maxSpeed = speed
        self.speed = [0,0]
        self.place(position)
        self.screenWidth = screenSize[0]
        self.screenHeight = screenSize[1]
        self.living = True
        
    def  __str__(self):
        return "I'm a Player " + str(self.rect.center) + str(self.speed) + str(self.living)
     
    def place(self, pt):
        print "I've moved to", pt
        
    def direction(self, dir):
        if dir == "up":
            self.speed[1] = -self.maxSpeed
        elif dir == "stop up":
            self.speed[1] = 0
        elif dir == "down":
            self.speed[1] = self.maxSpeed
        elif dir == "stop down":
            self.speed[1] = 0
        elif dir == "left":
            self.speed[0] = -self.maxSpeed
        elif dir == "stop left":
            self.speed[0] = 0
        elif dir == "right":
            self.speed[0] = self.maxSpeed
        elif dir == "stop right":
            self.speed[0] = 0
        
    def move(self):
        print "I've moved", self.speed
    
    def distToPoint(self, pt):
        print "I am this far from it."
    
    def collide(self, other):
        print "trying to hit other", self.screenHeight, other
    
    def collideWall(self):
        print "trying to hit edges of screen", self.screenWidth, self.screenHeight
        
    def attack(self, other):
        print "trying to hit other", str(other)
        #if pygame.mixer:
        #   self.bounceSound.play()
        