import pygame, math, sys, random

class NPC():
    def __init__(self, speed, position):
        self.surfaces = []
        self.frame = 0
        self.maxFrame = len(self.surfaces)-1
        self.surface = self.surfaces[self.frame]
        self.rect = self.surface.get_rect()
        self.place(position)
        self.living = True
        
    def  __str__(self):
        return "I'm a NPC " + str(self.rect.center) + str(self.speed) + str(self.living)
     
	def place(self, pt):
		print "I've moved to", pt
		
    def collide(self, other):
        print "trying to hit other", screenHeight
    