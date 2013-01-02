import pygame, math, sys, random

class Player():
    def __init__(self, speed, screenSize, pos):
        self.surfaces = []
        self.imgs = ["rcs/imgs/player/player.png","rcs/imgs/player/player_walk1.png","rcs/imgs/player/player_walk2.png", 
        "rcs/imgs/player/player_right.png","rcs/imgs/player/player_right_walk1.png","rcs/imgs/player/player_right_walk2.png", 
        "rcs/imgs/player/player_left.png","rcs/imgs/player/player_left_walk1.png","rcs/imgs/player/player_left_walk2.png", 
        "rcs/imgs/player/player_back.png","rcs/imgs/player/player_back_walk1.png","rcs/imgs/player/player_back_walk2.png"]
        for self.imgs in self.imgs:
            self.surfaces += [pygame.image.load(self.imgs)]
        self.frame = 0
        self.maxFrame = len(self.surfaces)-1
        self.surface = self.surfaces[self.frame]
        self.rect = self.surface.get_rect()
        self.maxSpeed = speed
        self.place(pos)
        self.speed = [0,0]
        self.waitCount = 0
        self.waitMax = 1
        self.placed = False
        self.frameran1 = False
        self.frameran2 = False
        self.frameran3 = False
        self.frameran4 = False
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
            self.dir = "none"
            self.moving = False
        elif dir == "down":
            self.speed[1] = self.maxSpeed
            self.dir = "down"
            self.moving = True
        elif dir == "stop down":
            self.speed[1] = 0
            self.dir = "none"
            self.moving = False
        elif dir == "left":
            self.speed[0] = -self.maxSpeed
            self.dir = "left"
            self.moving = True
        elif dir == "stop left":
            self.speed[0] = 0
            self.dir = "none"
            self.moving = False
        elif dir == "right":
            self.speed[0] = self.maxSpeed
            self.dir = "right"
            self.moving = True
        elif dir == "stop right":
            self.speed[0] = 0
            self.dir = "none"
            self.moving = False
        
    def move(self):
        if self.dir == "up":
            print "\n \n"
            if self.waitCount < self.waitMax:
                self.waitCount += 1
            else:
                self.waitCount = 0
                if self.moving == True:
                    if not self.frameran1:
                        self.frame = 10
                        self.frameran1 = True
                    if self.frame == 10:
                        self.frame = 11
                    elif self.frame == 11:
                        self.frame = 10    
                if not self.moving:
                    self.frame = 9
                    self.frameran1 = False
        elif self.dir == "down":
            if self.waitCount < self.waitMax:
                self.waitCount += 1
            else:
                self.waitCount = 0
                if self.moving == True:
                    if not self.frameran2:
                        self.frame = 1
                        self.frameran2 = True
                    if self.frame == 1:
                        self.frame = 2
                    elif self.frame == 2:
                        self.frame = 1    
                if not self.moving:
                    self.frame = 0
                    self.frameran2 = False
        elif self.dir == "left":
            if self.waitCount < self.waitMax:
                self.waitCount += 1
            else:
                self.waitCount = 0
                if self.moving == True:
                    if not self.frameran3:
                        self.frame = 7
                        self.frameran3 = True
                    if self.frame == 7:
                        self.frame = 8
                    elif self.frame == 8:
                        self.frame = 7    
                if not self.moving:
                    self.frame = 6
                    self.frameran3 = False
        elif self.dir == "right":
            if self.waitCount < self.waitMax:
                self.waitCount += 1
            else:
                self.waitCount = 0
                if self.moving == True:
                    if not self.frameran4:
                        self.frame = 4
                        self.frameran4 = True
                    if self.frame == 4:
                        self.frame = 5
                    elif self.frame == 5:
                        self.frame = 4    
                if not self.moving:
                    self.frame = 3 
                    self.frameran4 = False
  
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
                    
        