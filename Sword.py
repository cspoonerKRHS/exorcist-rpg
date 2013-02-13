import pygame, math, sys, random

class Sword():
    def __init__(self, screenSize):
        self.surfaces = []
        imgs = ["rcs/imgs/sword/swordfront.png", "rcs/imgs/sword/swordleft.png", "rcs/imgs/sword/swordright.png"]
        for img in imgs:
            surf = pygame.image.load(img)  
            self.surfaces += [surf]
        
        front = [self.surfaces[0]]
        self.front = []
        for img in front:
            self.front += [pygame.transform.scale(img, (8,25))]
        
        left = [self.surfaces[1]]
        self.left = []
        for img in left:
            self.left += [pygame.transform.scale(img, (25,8))]
            
        right = [self.surfaces[2]]
        self.right = []
        for img in right:
            self.right += [pygame.transform.scale(img, (25,8))]
              
        self.frame = 0
        self.surfaces = self.front
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
        
    def slash(self, player):
        if player.dir == "down" or player.dir == "stop down":
            self.dir = "down"
            self.surfaces = self.front
            center = player.rect.center
            center = (center[0]-7, center[1] + 20)
        if player.dir == "up" or player.dir == "stop up":
            self.dir = "up"
            self.surfaces = self.front
            center = player.rect.center
            center = (center[0], center[1] - 20)
        if player.dir == "right" or player.dir == "stop right":
            self.dir = "right"
            self.surfaces = self.right
            center =  player.rect.center
            center = (center[0]+18, center[1])
        if player.dir == "left" or player.dir == "stop left":
            self.dir = "left"
            self.surfaces = self.left
            center = player.rect.center
            center = (center[0]-18, center[1])
        
        self.surface = self.surfaces[self.frame]  
        self.rect = self.surface.get_rect(center = center)
       
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
        
        if self.living == True:
            if (self.rect.right > other.rect.left 
                and self.rect.left < other.rect.right):
                    if (self.rect.bottom > other.rect.top and 
                        self.rect.top < other.rect.bottom):
                        other.health -= 1
                    if other.health == 0:
                        other.living = False
                   