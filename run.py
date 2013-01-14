import pygame, math, sys, random
from Player import Player
from Enemies import Enemy
from Sword import Sword
from Screen import Screen
from Menu import Button
from Bosses import Boss
from Block import Block
#from Counter import Counter
from pygame.locals import*
from Map import level

if pygame.mixer:
    pygame.mixer.init()

pygame.init()
maxEnemies = 5

pygame.time.set_timer(USEREVENT+1, 1000)

clk = pygame.time.Clock()
screenWidth = 800
screenHeight = 600

screenSize = screenWidth, screenHeight
screen = pygame.display.set_mode(screenSize)

background = Screen(["rcs/imgs/screens/Background.png"], [0,0], screenSize, 10)
singleplayer = Button("SINGLEPLAYER", [250,300], (200, 10, 10))
exit = Button("EXIT", [250,400], (200, 10, 10))
enemies = []

map = level("map3.lvl", "map1.tng", screenSize)

boss = Boss(['rcs/imgs/bosses/boss.png'], [0,0], screenSize, 10)
boss.place([300,500])
sword = Sword(screenSize)
#counter = Counter([45,25], screenSize)

healthbar_imgs = []
for i in range(100, 0, -5):
    healthbar_imgs += ["rcs/imgs/stats_bar/health_bar_" + str(i) + "%.png"]
    
healthbar = Screen(healthbar_imgs, [0, 0], screenSize)
healthbar.place([645,13])
energybar_background = Screen(["rcs/imgs/stats_bar/energy_bar_background.png"], [0,0], screenSize)
energybar_background.place([640, 25])
energybar_imgs = ["rcs/imgs/stats_bar/nothing.png"]

for i in range(5, 105, 5):
    energybar_imgs += ["rcs/imgs/stats_bar/energy_bar_" + str(i) + "%.png"]
    
energybar = Screen(energybar_imgs, [0, 0], screenSize)
energybar.place([645,28])
healthbar_background = Screen(["rcs/imgs/stats_bar/healthbar_background.png"], [0,0], screenSize)
healthbar_background.place([640, 10])

if pygame.mixer:
    song = pygame.mixer.music.load('rcs/sounds/soundtracks/RPG_Soundtrack.ogg')
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

        singleplayer.update((200, 10, 10))
        exit.update((200, 10, 10))
        
        screen.fill(bgColor)
        screen.blit(background.surface, background.rect)
        screen.blit(singleplayer.surface, singleplayer.rect)
        screen.blit(exit.surface, exit.rect)
        player = Player(2, screenSize, [200, 200])
        pygame.display.flip()
    # Game    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
#            if event.type == USEREVENT+1:
#                counter.increase() 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.direction("left")
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.direction("right")
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.direction("up")
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.direction("down")
                if event.key == pygame.K_j:
                    sword.rect.clamp_ip(player.rect)
                    sword.living = True
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.direction("stop left")
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.direction("stop right")
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.direction("stop up")
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.direction("stop down")
                if event.key == pygame.K_j:
                    sword.rect.clamp_ip(player.rect)
                    sword.living = False    
                    
        # for block in map.dblocks:
            # if block.nspawn == True:
                # enemies += [Enemy(["rcs/imgs/enemies/enemy.png"], [0,3], screenSize, 1)]
            
            
        # Stuff that objects do
        player.move()
        player.wallCollide()
   
        
        # boss.attack(player)
        # boss.playerDetect(player)
        # boss.move
        # boss.collide(player)
        boss.collideWall()
        for enemy in enemies:
            enemy.collideWall()
            enemy.move()
            sword.attack(enemy)
            enemy.attack(player)
#            enemy.playerDetect(player)
            player.enemyCollide(enemy, healthbar)
        
        # Blitting
        screen.fill(bgColor)
        for block in map.blocks:
            screen.blit(block.surface, block.rect)
        for block in map.fblocks:
            screen.blit(block.surface, block.rect)
        for block in map.blocks:
            screen.blit(block.surface, block.rect)
        screen.blit(player.surface, player.rect)  
        if sword.living == True:
            screen.blit(sword.surface, sword.rect)  
        for enemey in enemies:
            screen.blit(enemy.surface, enemy.rect)
        # screen.blit(boss.surface, boss.rect)  
        screen.blit(healthbar_background.surface, healthbar_background.rect)  
        screen.blit(healthbar.surface, healthbar.rect)  
        screen.blit(energybar_background.surface, energybar_background.rect)  
        screen.blit(energybar.surface, energybar.rect)    
        pygame.display.flip()
        clk.tick(90)