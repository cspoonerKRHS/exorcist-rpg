import pygame, math, sys, random

class Enemy():
    def __init__(self, speed, position):
        self.surfaces = []
        self.frame = 0
        self.maxFrame = len(self.surfaces)-1
        self.surface = self.surfaces[self.frame]
        self.rect = self.surface.get_rect()
        self.speed = speed
        self.place(position)
        self.living = True
        
    def  __str__(self):
        return "I'm a Enemy " + str(self.rect.center) + str(self.speed) + str(self.living)
     
	def place(self, pt):
		print "I've moved to", pt
		
    def dir(self, dir):
		print "I have change direction" 
        
    def move(self):
        print "I've moved", self.speed
    
	def distToPoint(self, pt):
		print "I am this far from it."
    
    def collide(self, other):
        print "trying to hit other", screenHeight
    
    def collideWall(self, screenWidth, screenHeight):
        print "trying to hit edges of screen", screenWidth, screenHeight
        
    def attack(self, other):
        print "trying to hit other", str(other)
        #if pygame.mixer:
        #   self.bounceSound.play()
    
	def shoot(self, other):
        print "trying to shoot other", str(other)
	
	def melee(self, other):
        print "trying to melee other", str(other)