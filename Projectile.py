import pygame, math, sys, random

class Projectile():
    
    def __init__(self, images, speed, screenSize, scaleFactor= 1):
        self.baseSurfaces = []
        for img in imgs:
            surf = pygame.image.load(img)
            x = surf.get_width()
            y = surf.get_height()
            surf = pygame.transform.scale(surf, (x*scaleFactor,y*scaleFactor))
            self.surfaces += [surf]
        self.frame = 0
        self.waitCount = 0
        self.maxFrame = len(self.baseSurfaces)-1
        self.surface = self.baseSurfaces[self.frame]
        self.rect = self.surface.get_rect()
        self.radius = self.rect.width/2
        self.maxSpeed = speed
        self.speed = [0,0]
        self.screenWidth = screenSize[0]
        self.screenHeight = screenSize[1]
        self.fired = False
        self.living = True
        
            
    def move(self):
        self.rect = self.rect.move(self.speed)      
            
    def place(self, pt):
        self.rect = self.rect.move(pt)
        
    def animate(self):
        if self.frame < self.maxFrame:
            self.frame += 1
        else:
            self.frame = 0
       
       
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
                other.health -= self.charge/5.0
                self.living = False
                if other.health <= 0:
                    effect.increase()
                
    def fire(self, other):
        if self.fired == False:
            if other.dir == "right" or other.dir == "stop right":
                self.speed[0] = 10
            elif other.dir == "left" or other.dir == "stop left":
                self.speed[0] = -10    
            elif other.dir == "down" or other.dir == "stop down":
                self.speed[1] = -10     
            elif other.dir == "left" or other.dir == "stop left":
                self.speed[1] = 10        
            self.fired = True    