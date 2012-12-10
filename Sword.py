import pygame, math, sys, random

class Sword():
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
        if pygame.mixer:
            self.bounceSound = pygame.mixer.Sound("bounce.wav")
        
    def  __str__(self):
        return "I'm a sword " + str(self.rect.center) + str(self.speed) + str(self.living)
     
    def place(self, pt):
        print "I've moved to", pt
    
    def distToPoint(self, pt):
        print "I am this far from it."

    def attack(self, other):
        print "trying to hit other", str(other)