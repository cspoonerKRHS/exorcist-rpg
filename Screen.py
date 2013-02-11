import pygame, math, time

class Screen():

    # Methods or Functions
    def __init__(self, images, speed, screenSize, waitMax = 10):
        self.surfaces = []
        for image in images:
            self.surfaces += [pygame.image.load(image)]
        self.frame = 0
        self.waitCount = 0
        self.waitMax = waitMax
        self.maxFrame = len(self.surfaces)-1
        self.surface = self.surfaces[self.frame]
        self.rect = self.surface.get_rect()
        self.speed = speed
        self.radius = self.rect.width/2
        self.screenWidth = screenSize[0]
        self.screenHeight = screenSize[1]
        self.attacked = False
        self.select = False
        self.ran = False
        self.living = False
        self.value = 0
        self.neg = False
        self.upframe = False


    def place(self, pt):
        self.rect = self.rect.move(pt)

        
    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.frame < self.maxFrame:
            self.frame += 1
        else: 
            self.frame = 0
        self.surface = self.surfaces[self.frame]
            
    def animate(self):
        if self.upframe == True:
            if self.frame < self.maxFrame:
                self.frame += 1
            else:
                self.frame = 0
            self.upframe = False
            self.surface = self.surfaces[self.frame]
            

    def update(self, other):
        if self.frame < self.maxFrame and self.select == True:
            self.frame += 1
            other.frame += 1
        if self.frame == self.maxFrame and self.select == True or other.frame == other.maxFrame and other.select == True:
           other.frame = 0
           self.frame = 0
        self.surface = self.surfaces[self.frame]
        other.surface = other.surfaces[other.frame]
        
    def reset(self):
        self.frame = 0
        self.value = 0


    def distToPoint(self, pt):
        x1 = self.rect.center[0]
        x2 = pt[0]
        y1 = self.rect.center[1]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2))
        
    def wallCollide(self):
        if(self.rect.top > 0):
            self.rect.topleft = [0, -2500]
            self.living = False           
            return True
        return False   
            
    def lanimate(self):
        if self.waitCount < self.waitMax:
            self.waitCount += 1
        else:
            self.waitCount = 0
            if self.frame == 0 and self.neg == False:
                self.frame += 1
            if self.frame == 1 and self.neg == False:
                self.frame += 1
            if self.frame == 2:
                self.frame -= 1
                self.neg = True
            if self.frame == 1 and self.neg == True:
                self.frame -= 1
                self.neg = False

            else:
                self.frame = 0
                # self.living = False
            self.surface = self.surfaces[self.frame]

		
