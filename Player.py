import pygame, math, sys, random

class Player():
    def __init__(self, images, speed, screenSize, position):
        self.surfaces = []
        for image in images:
            self.surfaces += [pygame.image.load(image)]
        self.frame = 0
        self.maxFrame = len(self.surfaces)-1
        self.surface = self.surfaces[self.frame]
        self.rect = self.surface.get_rect()
        self.maxSpeed = speed
        self.speed = [0,0]
        self.place(position)
        self.screenWidth = screenSize[0]
        self.screenHeight = screenSize[1]
        self.living = True
        
    def  __str__(self):
        return "I'm a Player " + str(self.rect.center) + str(self.speed) + str(self.living)
     
    def place(self, pt):
        self.rect = self.rect.move(pt)
        
    def direction(self, dir):
        if dir == "up":
            self.speed[1] = -self.maxSpeed
        elif dir == "stop up":
            self.speed[1] = 0
        elif dir == "down":
            self.speed[1] = self.maxSpeed
        elif dir == "stop down":
            self.speed[1] = 0
        elif dir == "left":
            self.speed[0] = -self.maxSpeed
        elif dir == "stop left":
            self.speed[0] = 0
        elif dir == "right":
            self.speed[0] = self.maxSpeed
        elif dir == "stop right":
            self.speed[0] = 0
        
    def move(self):
        self.rect = self.rect.move(self.speed) 
    
    def animate(self):
        if self.frame < self.maxFrame:
            self.frame += 1
        else:
            self.frame = 0
            # self.living = False
        self.surface = self.surfaces[self.frame]
        
    def distToPoint(self, pt):
        x1 = self.rect.center[0]
        x2 = pt[0]
        y1 = self.rect.center[1]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2))

    
    def wallCollide(self):
        if (self.rect.left < 0 
            or self.rect.right > self.screenWidth):
            self.speed[1] = self.speed[1] = 0
            self.speed[0] = self.speed[0] = 0
        
    def enemyCollide(self, other, effect):
        if (self.rect.right > other.rect.left 
            and self.rect.left < other.rect.right):
                if (self.rect.bottom > other.rect.top and 
                    self.rect.top < other.rect.bottom):
                    pass
                    
    def blockCollide(self, other):
        if (self.rect.right > other.rect.left 
            and self.rect.left < other.rect.right):
                if (self.rect.bottom > other.rect.top and 
                    self.rect.top < other.rect.bottom):
                    if self.living == True:
                        other.hit = True
                        other.speed = [0, 0]
                        other.sound.play()
                        self.living = False
                        self.damage += 1
                        if other.ran == True:
                            other.living = False
                            other.hit = True       
                    
        