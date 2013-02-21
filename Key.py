import pygame, math, time

class Key():

    # Methods or Functions
    def __init__(self, screenSize, pos):
        self.surfaces = []
        imgs = ["rcs/imgs/key/key.png"]
        for img in imgs:
            surf = pygame.image.load(img)
            self.surfaces += [surf]
        self.frame = 0
        self.maxFrame = len(self.surfaces)-1
        self.surface = self.surfaces[self.frame]
        self.rect = self.surface.get_rect()
        self.place(pos)
        self.waitCount = 0
        self.waitMax = 4
        self.screenWidth = screenSize[0]
        self.screenHeight = screenSize[1]
        self.living = True
        
    def place(self, pt):
        self.rect = self.rect.move(pt)
        
    def playerCollide(self, other):
        if (self.rect.right > other.rect.left 
            and self.rect.left < other.rect.right):
            if (self.rect.bottom > other.rect.top and 
                self.rect.top < other.rect.bottom):    
                self.living = False
                other.key += 1