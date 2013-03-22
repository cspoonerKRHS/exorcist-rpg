import pygame, math, sys

class Counter():
    def __init__(self, pos, screenSize):
        self.font = pygame.font.Font(None, 60)
        self.value = 0
        self.surface = self.font.render(str(self.value), 1, (200, 20, 20))
        self.rect = self.surface.get_rect(centerx=pos[0], centery=pos[1])
        self.screenWidth = screenSize[0]
        self.screenHeight = screenSize[1]
        self.end = False
            
    def place(self, pt):
        self.rect = self.rect.move(pt)
    
    def increase(self, num=1):
        self.value += num
        self.surface = self.font.render(str(self.value), 1, (200, 20, 20))
        
    def set(self, num=0):
        self.value = num
        self.surface = self.font.render(str(self.value), 1, (200, 20, 20))
        
    def decrease(self, num=-1):
        self.value += num
        self.surface = self.font.render(str(self.value), 1, (200, 20, 20))
        
    def stop(self, stopnum):
        if self.value == stopnum:
            sys.exit()