import pygame, math, sys

class HighScore():
    def __init__(self, pos, display, screenSize):
        self.font = pygame.font.Font(None, 60)
        self.surface = self.font.render(str(display), 1, (200, 20, 20))
        self.rect = self.surface.get_rect(centerx=pos[0], centery=pos[1])
        self.screenWidth = screenSize[0]
        self.screenHeight = screenSize[1]
        self.end = False
        self.run = False
        self.display = ""
            
    def place(self, pt):
        self.rect = self.rect.move(pt)
    
    def update(self, newstr):
        if self.run == True:
            self.display = newstr
            
        self.surface = self.font.render(str(self.display), 1, (200, 20, 20))    