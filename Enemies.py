import pygame, math, sys, random

class Enemy():
    def __init__(self, speed, screenSize, position, waitMax = 1000):
        self.surfaces = []
        images = ["rcs/imgs/enemies/enemywalkup1.png", "rcs/imgs/enemies/enemywalkup2.png", "rcs/imgs/enemies/enemywalk3.png", 
            "rcs/imgs/enemies/enemywalkdown1.png", "rcs/imgs/enemies/enemywalkdown2.png", "rcs/imgs/enemies/enemywalkdown3.png",
            "rcs/imgs/enemies/enemywalkleft1.png", "rcs/imgs/enemies/enemywalkleft2.png", "rcs/imgs/enemies/enemywalkleft3.png", 
            "rcs/imgs/enemies/enemywalkright1.png", "rcs/imgs/enemies/enemywalkright2.png", "rcs/imgs/enemies/enemywalkright3.png",
            "rcs/imgs/enemies/enemy.png"]
        for image in images:
            self.surfaces += [pygame.image.load(image)]
        self.frontimgs = self.surfaces[0:2]
        self.rightimgs = self.surfaces[3:5]
        self.leftimgs = self.surfaces[6:8]
        self.backimgs = self.surfaces[9:11]
        self.attackimg = self.surfaces[12]
        self.surfaces = self.frontimgs
        self.frame = 0
        self.maxFrame = len(self.surfaces) - 1
        self.surface = self.surfaces[self.frame]
        self.rect = self.surface.get_rect()
        self.speed = speed
        self.waitCount = 0
        self.waitMax = waitMax
        self.place(position)
        self.screenWidth = screenSize[0]
        self.screenHeight = screenSize[1]
        self.living = True
        self.health = 10
        self.detectRadius = 100
        
    def  __str__(self):
        pass
#        return "I'm a Enemy " + str(self.rect.center) + str(self.speed) + str(self.living)
     
    def place(self, pt):
        self.rect.center = pt
#        print "I've moved to", pt
        
    def dir(self, dir):
        if dir == "up":
            self.speed[1] = -self.maxSpeed
            self.dir = "up"
        elif dir == "stop up":
            self.speed[1] = 0
            self.dir = "stop up"
        elif dir == "down":
            self.speed[1] = self.maxSpeed
            self.dir = "down"
        elif dir == "stop down":
            self.speed[1] = 0
            self.dir = "stop down"
        elif dir == "left":
            self.speed[0] = -self.maxSpeed
            self.dir = "left"
        elif dir == "stop left":
            self.speed[0] = 0
            self.dir = "stop left"
        elif dir == "right":
            self.speed[0] = self.maxSpeed
            self.dir = "right"
        elif dir == "stop right":
            self.speed[0] = 0
            self.dir = "stop right"
        
    def move(self):
#        print "I've moved", self.speed
        if self.dir == "up":
            if self.dir == "up":
                self.surfaces = self.backimgs
            if self.dir == "down":
                self.surfaces = self.frontimgs
            if self.dir == "left":
                self.surfaces = self.leftimgs
            if self.dir == "right":
                self.surfaces = self.rightimgs
                
        if self.frame > len(self.surfaces)-1:
            self.frame = len(self.surfaces)-1

        if self.waitCount < self.waitMax:
            self.waitCount += 1
        
        else:
            self.waitCount = 0
            if self.frame == len(self.surfaces)-1:
                self.frame = 0
            else:
                self.frame += 1
                
        self.surface = self.surfaces[self.frame]
        self.rect = self.rect.move(self.speed) 
    
    def distToPoint(self, pt):
#        print "I am this far from it."
        x1 = self.rect.center[0]
        x2 = pt[0]
        y1 = self.rect.center[1]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2))
        
         
    def collideWall(self):
#        print "trying to hit edges of screen", self.screenWidth, self.screenHeight
        if (self.rect.left < 0 
            or self.rect.right > self.screenWidth):
                self.speed[0] = self.speed[0]*-1
        if (self.rect.top < 0 
            or self.rect.bottom >self.screenHeight):
                self.speed[1] = self.speed[1]* -1
   

    def attack(self, other):
#        print "trying to hit other", str(other)
        pass
    
    def shoot(self, other):
#        print "trying to shoot other", str(other)
        pass
    
    def melee(self, other):
#        print "trying to melee other", str(other)
        pass
 
    def playerDetect(self, player):
#        print "trying to detect" + player
        if self.distToPoint(player.rect.center) < self.detectRadius:
            if self.rect.center[0] < player.rect.center[0]:
                self.speed[0] = 5
            if self.rect.center[0] > player.rect.center[0]:
                self.speed[0] = -5
            if self.rect.center[1] < player.rect.center[1]:
                self.speed[1] = 5
            if self.rect.center[1] > player.rect.center [1]:
                self.speed[1] = -5
            if self.rect.center[0] == player.rect.center[0]:
                self.speed[0] = 0
            if self.rect.center[1] == player.rect.center[1]:
                self.speed[1] = 0
                
    def enemyCollide(self, other):
        if (self.rect.right > other.rect.left 
            and self.rect.left < other.rect.right):
            if (self.rect.bottom > other.rect.top and 
                self.rect.top < other.rect.bottom):
               
                    self.speed[0] = self.speed[0] * -1
                    self.speed[1] = self.speed[1] * -1
                    other.speed[0] = other.speed[0] * -1
                    other.speed[1] = other.speed[1] * -1'
                    
    def bounce(self)
        if self.bounce == "X"
            self.speed[0] = self.speed[0]*-1
        if self.bounce == "Y"
            self.speed[1] = self.speed[1]*-1
        
        