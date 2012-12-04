import pygame, math, sys, random

class Button():
    def __init__(self, text, location, color, highlighted = False):
        self.surfaces = []
        self.font = pygame.font.Font(None, 60)
        self.text = text
        self.surface = self.font.render(str(self.text), 1, color)
        self.frame = 0
        self.rect = self.surface.get_rect()
        self.clicked = False
        self.highlighted = highlighted
        self.place(location)
        
    def  __str__(self):
        return "I'm a button " + str(self.rect.center) + str(self.speed) + str(self.living)
     
	def place(self, pt):
		print "I've moved to", pt
    
	def update(self, pt):
		print "I updated."
    
    def collidePt(self, other):
        print "trying to hit other", screenHeight
