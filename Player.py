import pygame, math, sys, random

class Player():
    def __init__(self, speed, screenSize, pos):
        self.surfaces = []
        imgs = ["rcs/imgs/player/player.png","rcs/imgs/player/player_walk1.png","rcs/imgs/player/player_walk2.png", 
        "rcs/imgs/player/player_right.png","rcs/imgs/player/player_right_walk1.png","rcs/imgs/player/player_right_walk2.png", 
        "rcs/imgs/player/player_left.png","rcs/imgs/player/player_left_walk1.png","rcs/imgs/player/player_left_walk2.png", 
        "rcs/imgs/player/player_back.png","rcs/imgs/player/player_back_walk1.png","rcs/imgs/player/player_back_walk2.png"]
        for img in imgs:
            print img
            surf = pygame.image.load(img)
            surf = pygame.transform.scale(surf, (16,50))
            self.surfaces += [surf]
        self.frontstill = self.surfaces[0:1]
        self.frontimgs = self.surfaces[1:3]
        self.backstill = self.surfaces[3:4]
        self.rightimgs = self.surfaces[4:6]
        self.leftstill = self.surfaces[6:7]
        self.leftimgs = self.surfaces[7:9]
        self.rightstill = self.surfaces[9:10]
        self.backimgs = self.surfaces[10:12]
        self.surfaces = self.frontimgs
        self.frame = 0
        self.maxFrame = len(self.surfaces)-1
        self.surface = self.surfaces[self.frame]
        self.rect = self.surface.get_rect()
        self.maxSpeed = speed
        self.place(pos)
        self.speed = [0,0]
        self.waitCount = 0
        self.waitMax = 4
        self.placed = False
        self.screenWidth = screenSize[0]
        self.screenHeight = screenSize[1]
        self.living = True
        self.dir = "none"
        self.moving = False
        
    def  __str__(self):
        return "I'm a Player " + str(self.rect.center) + str(self.speed) + str(self.living)
     
    def place(self, pt):
        self.rect = self.rect.move(pt)
            
        
    def direction(self, dir):
        if dir == "up":
            self.speed[1] = -self.maxSpeed
            self.dir = "up"
            self.moving = True
        elif dir == "stop up":
            self.speed[1] = 0
            self.dir = "stop up"
            self.moving = False
        elif dir == "down":
            self.speed[1] = self.maxSpeed
            self.dir = "down"
            self.moving = True
        elif dir == "stop down":
            self.speed[1] = 0
            self.dir = "stop down"
            self.moving = False
        elif dir == "left":
            self.speed[0] = -self.maxSpeed
            self.dir = "left"
            self.moving = True
        elif dir == "stop left":
            self.speed[0] = 0
            self.dir = "stop left"
            self.moving = False
        elif dir == "right":
            self.speed[0] = self.maxSpeed
            self.dir = "right"
            self.moving = True
        elif dir == "stop right":
            self.speed[0] = 0
            self.dir = "stop right"
            self.moving = False
        
    def move(self):
        
        if self.dir == "up":
            self.surfaces = self.backimgs
        if self.dir == "down":
            self.surfaces = self.frontimgs
        if self.dir == "left":
            self.surfaces = self.leftimgs
        if self.dir == "right":
            self.surfaces = self.rightimgs  
        if self.dir == "stop up":
            self.surfaces = self.backstill
        if self.dir == "stop down":
            self.surfaces = self.frontstill
        if self.dir == "stop left":
            self.surfaces = self.leftstill
        if self.dir == "stop right":
            self.surfaces = self.rightstill    
        
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
                    
        