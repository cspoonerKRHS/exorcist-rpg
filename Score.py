import pygame, sys, math, time

class Score():
    def __init__(self, pos, screenSize):
        self.font = pygame.font.Font(None, 60)
        self.characters = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWxXxYyZz0123456789"
        self.char = 0
        self.surface = self.font.render(str(self.characters[self.char]), 1, (200, 20, 20))
        self.rect = self.surface.get_rect(centerx=pos[0], centery=pos[1])
        self.screenWidth = screenSize[0]
        self.screenHeight = screenSize[1]
        self.end = False
        self.selected = False
        self.living = True
        self.character = ""
            
    def place(self, pt):
        self.rect = self.rect.move(pt)
    
    def scroll(self, dir):
        if self.living:
            if self.selected:
                if self.char >= len(self.characters):
                    self.char = 0
                elif dir == "up":
                    self.char -= 1
                elif dir == "down":
                    self.char += 1
                self.surface = self.font.render(str(self.characters[self.char]), 1, (200, 20, 20))    
    def update(self):
        if self.living:
            if self.selected:
                self.surface = self.font.render(str(self.characters[self.char]), 1, (200, 20, 20))    
            if not self.selected:
                self.surface = self.font.render(str(self.characters[self.char]), 1, (100, 0, 0))       
            self.character = self.characters[self.char]
    def switch(self, dir, other):
        if self.living:
            if self.selected:
                if dir == "left":
                    other.selected = True
                    self.selected = False
                if dir == "right":
                    other.selected = True    
                    self.selected = False
            