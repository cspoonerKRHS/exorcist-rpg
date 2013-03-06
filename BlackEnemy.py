import pygame, math, sys, random
from Enemies import Enemy

class BlackEnemy(Enemy):
    def __init__(self, speed, screenSize, position, waitMax = 1000):
        Enemy.__init__(self, speed, screenSize, position, waitMax)
        self.surfaces = []
        imgs = ["rcs/imgs/enemies/darkenemywalkup1.png", "rcs/imgs/enemies/darkenemywalkup2.png", "rcs/imgs/enemies/darkenemywalk3.png", 
            "rcs/imgs/enemies/darkenemywalkdown1.png", "rcs/imgs/enemies/darkenemywalkdown2.png", "rcs/imgs/enemies/darkenemywalkdown3.png",
            "rcs/imgs/enemies/darkenemywalkleft1.png", "rcs/imgs/enemies/darkenemywalkleft2.png", "rcs/imgs/enemies/darkenemywalkleft3.png", 
            "rcs/imgs/enemies/darkenemywalkright1.png", "rcs/imgs/enemies/darkenemywalkright2.png", "rcs/imgs/enemies/darkenemywalkright3.png",
            "rcs/imgs/enemies/darkenemy.png"]
        for img in imgs:
            surf = pygame.image.load(img)
            surf = pygame.transform.scale(surf, (25,25))
            self.surfaces += [surf]
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
        self.place(position)
        
    def playerCollide(self, other, effect):
            other.hurt = False
            if (self.rect.right > other.rect.left 
                and self.rect.left < other.rect.right):
                    if (self.rect.bottom > other.rect.top and 
                        self.rect.top < other.rect.bottom):
                        other.hurt = True
                        if other.nodamage == 0:
                            effect.upframe = True
                            effect.countframe = 3
                            other.hit = True   
                        other.nodamage += 1
                        if other.nodamage == 25:
                            other.nodamage = 0    