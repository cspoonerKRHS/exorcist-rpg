import pygame, math, sys, random
from Player import Player
from Enemies import Enenmies
from Sword import Sword
from Screen import Screen
from Menu import Button
from Bosses import Boss
from NPC import NPC

if pygame.mixer:
    pygame.mixer.init()

pygame.init()


clk = pygame.time.Clock()
screenWidth = 800
screenHeight = 600

screenSize = screenWidth, screenHeight
screen = pygame.display.set_mode(screenSize)


singleplayer = Button("SINGLEPLAYER", [0,10], (10, 100, 10))
exit = Button("EXIT", [0,10], (10, 100, 10))
singleplayer.place([300, 300])
exit.place([300, 400])
player = Player(["player.png"], [0,0], screenSize, 10)
player.place([300,500])



if pygame.mixer:    song = pygame.mixer.music.load('02.Plutonium_Telecom-Attempt_3.ogg')
if pygame.mixer:    
    pygame.mixer.music.play()
    
red = 0
green = 0
blue = 0
bgColor = red, green, blue

run = False

# Menu
while True:
    while not run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_UP or event.key == pygame.K_w) and not singleplayer.highlighted:
                    singleplayer.highlighted = True
                    exit.highlighted = False
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s and not exit.highlighted:
                    exit.highlighted = True
                    singleplayer.highlighted = False
                elif event.key == pygame.K_SPACE and exit.highlighted == True:
                    sys.exit()
                elif event.key == pygame.K_SPACE and singleplayer.highlighted == True:
                    run = True
            elif event.type == pygame.MOUSEMOTION:
                if singleplayer.collidePt(event.pos):
                    singleplayer.highlighted = True
                    exit.highlighted = False
                elif exit.collidePt(event.pos):
                    singleplayer.highlighted = False
                    exit.highlighted = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if singleplayer.collidePt(event.pos):
                        singleplayer.clicked = True
                        run = True
                    elif exit.collidePt(event.pos):
                        exit.clicked = True
                        sys.exit()

        singleplayer.update((10, 200, 10))
        exit.update((10, 200, 10))
        
        screen.fill(bgColor)
        screen.blit(singleplayer.surface, singleplayer.rect)
        screen.blit(exit.surface, exit.rect)
        pygame.display.flip()
    # Game    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.speed[0] = player.speed[0] =-10
                if event.key == pygame.K_d:
                    player.speed[0] = player.speed[0] =10
                if event.key == pygame.K_SPACE:
                    player.speed[0] = player.speed[0] =0
                if event.key == pygame.K_j:
                   
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player.speed[1] = player.speed[0] = 0
                if event.key == pygame.K_d:
                    player.speed[1] = player.speed[0] = 0
                
       
        # Stuff that objects do
        player.move()
        player.wallCollide()
          
        # Blitting
        screen.fill(bgColor)
        screen.blit(background.surface, background.rect)   
        screen.blit(player.surface, player.rect)  
        pygame.display.flip()
        clk.tick(90)