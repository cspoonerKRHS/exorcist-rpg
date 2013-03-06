import pygame, math, sys

class Block():
    def __init__(self, pos, screenSize, image, size):
        self.font = pygame.font.Font(None, 60)
        self.value = 0
        self.surface = pygame.image.load(image)
        self.surface = pygame.transform.scale(self.surface, size)
        self.rect = self.surface.get_rect(centerx=pos[0], centery=pos[1])
        self.screenWidth = screenSize[0]
        self.screenHeight = screenSize[1]
        self.go = True
        self.radius = 50
        self.nodamage = False
        self.living = True
            
    def place(self, pt):
        self.rect.center = (pt)
        
    def distToPoint(self, pt):
        x1 = self.rect.center[0]
        x2 = pt[0]
        y1 = self.rect.center[1]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2))

    def playerCollide(self, other):
        if (self.rect.right > other.rect.left 
            and self.rect.left < other.rect.right):
            if (self.rect.bottom > other.rect.top and 
                self.rect.top < other.rect.bottom): 
                other.speed[0] = other.speed[0] * -.8
                other.speed[1] = other.speed[1] * -.8
                
                other.move()
                other.move()
                
                other.speed[0] = other.speed[0] = 0
                other.speed[1] = other.speed[1] = 0
    
    def lavaCollide(self, other):      
        if (self.rect.right > other.rect.left 
            and self.rect.left < other.rect.right):
            if (self.rect.bottom > other.rect.top and 
                self.rect.top < other.rect.bottom):   
                other.slow = True   
    def keyCollide(self, other):
        if (self.rect.right > other.rect.left 
            and self.rect.left < other.rect.right):
            if (self.rect.bottom > other.rect.top and 
                self.rect.top < other.rect.bottom): 
                if other.key > 0:
                    self.living = False
                
                other.speed[0] = other.speed[0] * -.8
                other.speed[1] = other.speed[1] * -.8
                
                other.move()
                other.move()
                
                other.speed[0] = other.speed[0] = 0
                other.speed[1] = other.speed[1] = 0
                    
    def deathplayerCollide(self, other, effect):
        other.hurt = False
        if (self.rect.right > other.rect.left 
            and self.rect.left < other.rect.right):
            if (self.rect.bottom > other.rect.top and 
                self.rect.top < other.rect.bottom): 
                    # print "Taylor"
                    if other.nodamage == 0:
                        effect.upframe = True
                        effect.countframe = 1
                        other.hit = True  
                    self.nodamage += 1
                    if self.nodamage == 50:
                        self.nodamage = 0    
    
    def enemyCollide(self, other):
        if (self.rect.right > other.rect.left-50 
            or self.rect.left < other.rect.right-50):
                other.bounce("X")
        if (self.rect.bottom > other.rect.top-50 or 
            self.rect.top < other.rect.bottom-50): 
                other.bounce("Y")
                    
    def playerDetect(self, other):
        if self.go == True:
            if self.distToPoint(other.rect.center) < self.radius:
                self.go = False
                return True
        return False
        
    def keySpawn(self):
        if self.go == True:
           self.go = False
           return True
        return False
    
    def playerKeyCollide(self, other):
        if (self.rect.right > other.rect.left 
            and self.rect.left < other.rect.right):
            if (self.rect.bottom > other.rect.top and 
                self.rect.top < other.rect.bottom):   
                self.living = False
                other.key += 1

        
    #-------------infinite spawn-----------        
    # def playerDetect(self, other):
        # if self.distToPoint(other.rect.center) < self.radius:
           # return True
        # return False
