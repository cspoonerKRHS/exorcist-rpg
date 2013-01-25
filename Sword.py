import pygame, math, sys, random

class Sword():
    def __init__(self, screenSize):
        self.surfaces = []
        imgs = ["rcs/imgs/sword/swordfront.png", "rcs/imgs/sword/swordleft.png", "rcs/imgs/sword/swordright.png"]
        for img in imgs:
            surf = pygame.image.load(img)
            surf = pygame.transform.scale(surf, (8,25))
            self.surfaces += [surf]
        self.front = self.surfaces[0]
        self.left = self.surfaces[1]
        self.right = self.surfaces[2]
        self.surface = self.front  
        self.frame = 0
        self.maxFrame = len(self.surfaces)-1
        self.surface = self.surfaces[self.frame]
        self.rect = self.surface.get_rect()
        self.screenWidth = screenSize[0]
        self.screenHeight = screenSize[1]
        self.living = False
        if pygame.mixer:
            self.bounceSound = pygame.mixer.Sound("bounce.wav")
        self.place = False    
        
    def  __str__(self):
        return "I'm a sword " + str(self.rect.center) + str(self.speed) + str(self.living)
     
    def place(self, pt):
        pass
    def distToPoint(self, pt):
        pass
       
    def attack(self, other, other2):
        if other2.dir == "up":
            self.surfaces = self.front
        if other2.dir == "down":
            self.surfaces = self.front
        if other2.dir == "left":
            self.surfaces = self.left
        if other2.dir == "right":
            self.surfaces = self.right 
    
        # if self.frame > len(self.surfaces)-1:
            # self.frame = len(self.surfaces)-1
        
        # if self.waitCount < self.waitMax:
            # self.waitCount += 1
        # else:
            # self.waitCount = 0
            # if self.frame == len(self.surfaces)-1:
                # self.frame = 0
            # else:
                # self.frame += 1

        self.surface = self.surfaces[self.frame]            
        self.rect = self.rect.move(self.speed) 
        
        if self.living == True:
            if (self.rect.right > other.rect.left 
                and self.rect.left < other.rect.right):
                    if (self.rect.bottom > other.rect.top and 
                        self.rect.top < other.rect.bottom):
                        other.living = False
                   