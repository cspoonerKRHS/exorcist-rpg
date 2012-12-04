import pygame, math, sys, random

class Sword():
    def __init__(self, speed, position):
        self.surfaces = []
        self.frame = 0
        self.maxFrame = len(self.surfaces)-1
        self.surface = self.surfaces[self.frame]
        self.rect = self.surface.get_rect()
        self.speed = speed
        self.place(position)
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