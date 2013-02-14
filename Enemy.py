import pygame, math

class Enemy():
    # Attributes or Variables
    #surfaces = []
    #surface = ""
    #frame = 0
    #maxFrame = 0
    #waitCount = 0
    #waitMax = 0
    #rect = ""
    #radius = 0
    #speed = [0,0]
    #screenWidth = 0
    #screenHeight = 0
    
    # Methods or Functions
    def __init__(self, images, speed, location, screenSize):
        self.surfaces = []
        for image in images:
            self.surfaces += [pygame.image.load(image)]
        self.frame = 0
        self.waitCount = 0
        self.maxFrame = len(self.surfaces)-1
        self.surface = self.surfaces[self.frame]
        self.rect = self.surface.get_rect()
        self.radius = self.rect.width/2
        self.speed = speed
        self.screenWidth = screenSize[0]
        self.screenHeight = screenSize[1]
        self.place(location)
        self.dead = False
        self.damage = 0
    
    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.waitCount < self.waitMax:
            self.waitCount += 1
        else:
            self.waitCount = 0
            
            if self.frame < self.maxFrame:
                self.frame += 1
            else:
                self.frame = 0
            self.surface = self.surfaces[self.frame]
        
    def place(self, pt):
        self.rect = self.rect.move(pt)
        
    def distToPoint(self, pt):
        x1 = self.rect.center[0]
        x2 = pt[0]
        y1 = self.rect.center[1]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2))

    def wallCollide(self):
        if (self.rect.left < 0 
            or self.rect.right > self.screenWidth):
            self.speed[0] = self.speed[0]*-1
        if (self.rect.top < 0 
            or self.rect.bottom >self.screenHeight):
            self.speed[1] = self.speed[1]*-1    
            
    def Collide(self, other):
        if (self.rect.right > other.rect.left 
            and self.rect.left < other.rect.right):
            if (self.rect.bottom > other.rect.top and 
                self.rect.top < other.rect.bottom):
                if (self.distToPoint(other.rect.center)
                    < self.radius + other.radius):  
                    self.speed[0] = self.speed[0] * -1
                    self.speed[1] = self.speed[1] * -1
                    other.speed[0] = other.speed[0] * -1
                    other.speed[1] = other.speed[1] * -1
    
    def update(self):
        if self.damage == 3:
            print "dead"
            self.dead = True
    
    