import pygame, math, sys, random

class Enemy():
    def __init__(self, speed, screenSize, position, dif = 2, waitMax = 1000):
        self.surfaces = []
        images = ["rcs/imgs/enemies/enemywalkup1.png", "rcs/imgs/enemies/enemywalkup2.png", "rcs/imgs/enemies/enemywalk3.png", 
            "rcs/imgs/enemies/enemywalkdown1.png", "rcs/imgs/enemies/enemywalkdown2.png", "rcs/imgs/enemies/enemywalkdown3.png",
            "rcs/imgs/enemies/enemywalkleft1.png", "rcs/imgs/enemies/enemywalkleft2.png", "rcs/imgs/enemies/enemywalkleft3.png", 
            "rcs/imgs/enemies/enemywalkright1.png", "rcs/imgs/enemies/enemywalkright2.png", "rcs/imgs/enemies/enemywalkright3.png",
            "rcs/imgs/enemies/enemy.png"]
        for image in images:
            self.surfaces += [pygame.image.load(image)]
        self.upimgs = self.surfaces[0:2]
        self.downimgs = self.surfaces[3:5]
        self.leftimgs = self.surfaces[6:8]
        self.rightimgs = self.surfaces[9:11]
        self.attackimg = self.surfaces[12]
        self.surfaces = self.upimgs
        self.frame = 0
        self.maxFrame = len(self.surfaces) - 1
        self.surface = self.surfaces[self.frame]
        self.rect = self.surface.get_rect()
        self.speed = [speed[0]*dif, speed[1]*dif]
        self.waitCount = 0
        self.waitMax = waitMax
        self.place(position)
        self.screenWidth = screenSize[0]
        self.screenHeight = screenSize[1]
        self.living = True
        self.health = 10
        self.detectRadius = 100
        self.dir = "up"
        self.playerDected = False
        self.dif = dif

    def  __str__(self):
        pass
#        return "I'm a Enemy " + str(self.rect.center) + str(self.speed) + str(self.living)

    def place(self, pt):
        self.rect.center = pt
#        print "I've moved to", pt

    def direction(self):
        if self.speed[1] < 0:
            self.dir = "up"
        elif self.speed[1] > 0:
            self.dir = "down"
        elif self.speed[0] < 0:
            self.dir = "left"
        elif self.speed[0] > 0:
            self.dir = "right"

    def move(self):
#        print "I've moved", self.speed
        
        if self.dir == "up":
            self.surfaces = self.upimgs
        if self.dir == "down":
            self.surfaces = self.downimgs
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
    
    def playerCollide(self, other, effect):
        other.hurt = False
        if (self.rect.right > other.rect.left 
            and self.rect.left < other.rect.right):
                if (self.rect.bottom > other.rect.top and 
                    self.rect.top < other.rect.bottom):
                    other.hurt = True
                    if other.nodamage == 0:
                        effect.upframe = True
                        effect.countframe = 1*self.dif
                        other.hit = True   
                    other.nodamage += 1
                    if other.nodamage == 25:
                        other.nodamage = 0    

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
        self.playerDected = False
        if self.distToPoint(player.rect.center) < self.detectRadius:
            if self.rect.center[0] < player.rect.center[0]:
                self.speed[0] = 2*self.dif
                self.playerDected = True
                xdiff = math.fabs(player.rect.center[0] - self.rect.center[0])
            elif self.rect.center[0] > player.rect.center[0]:
                self.speed[0] = -2*self.dif
                self.playerDected = True
                xdiff = math.fabs(player.rect.center[0] - self.rect.center[0])
            else:
                self.speed[0] = 0
                self.playerDected = False
                xdiff = 0
            
            if self.rect.center[1] < player.rect.center[1]:
                self.speed[1] = 2*self.dif
                self.playerDected = True
                ydiff = math.fabs(player.rect.center[1] - self.rect.center[1])
            elif self.rect.center[1] > player.rect.center [1]:
                self.speed[1] = -2*self.dif
                self.playerDected = True
                ydiff = math.fabs(player.rect.center[1] - self.rect.center[1])
            
            else:
                self.speed[1] = 0
                self.playerDected = False
                ydiff = 0
            
            
            if ydiff > xdiff:       
                if self.speed[1] < 0:
                    self.dir = "up"
                elif self.speed[1] > 0:
                    self.dir = "down"
            else:
                if self.speed[0] < 0:
                    self.dir = "left"
                elif self.speed[0] > 0:
                    self.dir = "right"

    def enemyCollide(self, other):
        if (self.rect.right > other.rect.left
            or self.rect.left < other.rect.right):
            if (self.rect.bottom > other.rect.top or
                self.rect.top < other.rect.bottom):
                    self.speed[0] = self.speed[0] * -1
                    self.speed[1] = self.speed[1] * -1
                    other.speed[0] = other.speed[0] * -1
                    other.speed[1] = other.speed[1] * -1

    def bounce(self, bounce):
        if bounce == "X":
            self.speed[0] = self.speed[0]*-1
        if bounce == "Y":
            self.speed[1] = self.speed[1]*-1