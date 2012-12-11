import pygame, math, sys

class Block():
    def __init__(self, pos, screenSize, image):
        self.font = pygame.font.Font(None, 60)
        self.value = 0
        self.surface = pygame.image.load(image)
        self.rect = self.surface.get_rect(centerx=pos[0], centery=pos[1])
        self.screenWidth = screenSize[0]
        self.screenHeight = screenSize[1]
            
    def place(self, pt):
        self.rect.center = (pt)

    def wallCollide(self, other):
        if (self.rect.right > other.rect.left 
            and self.rect.left < other.rect.right):
            if (self.rect.bottom > other.rect.top and 
                self.rect.top < other.rect.bottom): 
                    other.speed[0] = other.speed[0] = 0
                    other.speed[1] = other.speed[1] = 0
    
    def BadCollide(self, other):
        if (self.rect.right > other.rect.left 
            and self.rect.left < other.rect.right):
            if (self.rect.bottom > other.rect.top and 
                self.rect.top < other.rect.bottom): 
                    other.speed[0] = other.speed[0] * -1
