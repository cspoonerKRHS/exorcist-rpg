import pygame, math, sys, random

class Projectile():
    
    def __init__(self, speed, images, screenSize, pos, dif =2):
        self.surfaces = []
        self.imgs = images
        for img in imgs:
            surf = pygame.image.load(img)
            surf = pygame.transform.scale(surf, (10,10))
            self.surfaces += [surf]
        self.frame = 0
        self.maxFrame = len(self.surfaces) - 1
        self.surface = self.surfaces[self.frame]
        self.rect = self.surface.get_rect()
        
    def move(self):
        self.rect = self.rect.move(self.speed)      
            
    def place(self, pt):
        self.rect = self.rect.move(pt)
        
    def animate(self):
        if self.frame < self.maxFrame:
            self.frame += 1
        else:
            self.frame = 0
    def animate2(self, other):        
        if self.waitCount < 10:
            self.waitCount += 1
        if self.waitCount == 10:    
            self.charge += 10
            self.surface = pygame.transform.scale(
                                self.baseSurfaces[self.frame], 
                                (self.charge, self.charge))
            if other.dir == "right" or other.dir == "stop right":
                    self.rect.center = other.rect.midright
            if other.dir == "left" or other.dir == "stop left":
                self.rect.center = other.rect.midleft
            self.waitCount = 0
                
    
    def distToPoint(self, pt):
        x1 = self.rect.center[0]
        x2 = pt[0]
        y1 = self.rect.center[1]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    def wallCollide(self):
        if (self.rect.left < 0 
            or self.rect.right > self.screenWidth):
                self.living = False
        if (self.rect.top < 0 
            or self.rect.bottom >self.screenHeight):
                self.living = False
    
    def otherCollide(self, other, effect):
        if (self.rect.right > other.rect.left 
            and self.rect.left < other.rect.right):
            if (self.rect.bottom > other.rect.top and 
                self.rect.top < other.rect.bottom): 
                effect.upframe = True
                effect.countframe = 1*dif
                self.living = False
                