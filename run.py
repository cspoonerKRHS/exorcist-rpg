import pygame, math, sys, random
from Player import Player
from Enemies import Enemy
from BlackEnemy import BlackEnemy
from Sword import Sword
from Screen import Screen
from Menu import Button
from Bosses import Boss
from Block import Block
from Counter import Counter
from pygame.locals import*
from Map import Level
from Player_Effects import Player_Effects
from Key import Key
from Score import Score
from HighScore import HighScore
from HighScoreReader import HighScoreReader

if pygame.mixer:
    pygame.mixer.init()

pygame.init()
maxEnemies = 5

TIMEREVENT = USEREVENT+1
pygame.time.set_timer(TIMEREVENT, 1000)

clk = pygame.time.Clock()
screenWidth = 800
screenHeight = 600

screenSize = screenWidth, screenHeight
screen = pygame.display.set_mode(screenSize)

namept1 = Score([200, 200], screenSize)
namept1.selected = True
namept2 = Score([250, 200], screenSize)
namept3 = Score([300, 200], screenSize)
namept4 = Score([350, 200], screenSize)
score1 = HighScore([500, 100], [""], screenSize)
score2 = HighScore([500, 200], [""], screenSize)
score3 = HighScore([500, 300], [""], screenSize)
score4 = HighScore([500, 400], [""], screenSize)
yourscore = HighScore([300, 300], [""], screenSize) 
counter = Counter([45,25], screenSize)

highscorereader = HighScoreReader("rcs/scores.txt", yourscore, counter)
background = Screen(["rcs/imgs/screens/Background.png"], [0,0], screenSize, 10)
death = Screen(["rcs/imgs/screens/ending_screen.png"], [0,0], screenSize, 10)
singleplayer = Button("SINGLEPLAYER", [250,300], (200, 10, 10))
exit = Button("EXIT", [250,400], (200, 10, 10))
opexit = Button("EXIT", [0,10], (20, 100, 20))
hgexit = Button("EXIT", [0,10], (200, 10, 20))
option = Button("OPTIONS", [0,10], (20, 100, 20))
aidif = Button("AI DIFFICULTY", [0,10], (20, 100, 20))
easy = Button("n00b", [0,10], (20, 100, 20))
normal = Button("NORMAL", [0,10], (20, 100, 20))
hard = Button("EVIL", [0,10], (20, 100, 20))
option.place([250, 345])
aidif.place([100, 100])
easy.place([100, 200])
normal.place([250, 200])
hard.place([500, 200])
opexit.place([600, 500])
hgexit.place([600, 500])
enemies = []
darkEnemies = []
keys = []

dif = 2

canScrollUp = False
canScrollDown = False

hurt = Player_Effects(["rcs/imgs/player/hurt.png"], [0,0], screenSize, 10)

map = Level("map1", screenSize)

boss = Boss(['rcs/imgs/bosses/boss.png'], [0,0], screenSize, 10)
boss.place([300,500])
sword = Sword(screenSize)
counter = Counter([45,25], screenSize) 

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
run2 = False
run3 = False

# Menu
while True:
    while not run and not run2 and not run3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if singleplayer.collidePt(event.pos):
                        singleplayer.clicked = True
                        run = True                     
                    elif option.collidePt(event.pos):
                        option.clicked = True
                        run2 = True
                    elif exit.collidePt(event.pos):
                        exit.clicked = True
                        sys.exit()

        singleplayer.update((200, 10, 10))
        option.update((200, 10, 10))
        exit.update((200, 10, 10))
        
        screen.fill(bgColor)
        screen.blit(background.surface, background.rect)
        screen.blit(option.surface, option.rect)
        screen.blit(singleplayer.surface, singleplayer.rect)
        screen.blit(exit.surface, exit.rect)
        player = Player(7, screenSize, [360, 510])
        pygame.display.flip()
        
    while run2 and not run3:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if opexit.collidePt(event.pos):
                            opexit.clicked = True
                            run2 = False
                        if normal.collidePt(event.pos):
                            normal.clicked = True
                            dif = 2
                        if easy.collidePt(event.pos):
                            easy.clicked = True
                            dif = 1        
                        if hard.collidePt(event.pos):
                            hard.clicked = True
                            dif = 3
                            
            opexit.update((200, 10, 10))
            easy.update((200, 10, 10))
            normal.update((200, 10, 10))
            hard.update((200, 10, 10))
            aidif.update((200, 10, 10))
            
            screen.fill(bgColor)
            screen.blit(opexit.surface, opexit.rect)
            screen.blit(aidif.surface, aidif.rect)
            screen.blit(easy.surface, easy.rect)
            screen.blit(normal.surface, normal.rect)
            screen.blit(hard.surface, hard.rect)
            pygame.display.flip()
        
            
    # Game    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            # if event.type == TIMEREVENT:
                # counter.increase() 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.direction("left")
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.direction("right")
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.direction("up")
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.direction("down")
                if event.key == pygame.K_j or event.key == pygame.K_SPACE:
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
                if event.key == pygame.K_j or event.key == pygame.K_SPACE:  
                    sword.living = False
                    
        
        for block in map.enemyblocks:
            if block.playerDetect(player):
                enemies += [Enemy([3,3], screenSize, block.rect.center, dif, 1)]
        for block in map.darkblocks:
            if block.playerDetect(player):
                darkEnemies += [BlackEnemy([1.5,1.5], screenSize, block.rect.center, dif, 1)]        
                
        for block in map.killblocks:
            block.deathplayerCollide(player, healthbar)        
        if sword.living:
            sword.slash(player)
        hurt.place2(player)
        # Stuff that objects do
        player.move()
        player.wallCollide()
        healthbar.check(player)
        healthbar.animate2(player)
        player.update(healthbar)
        for block in map.blocks:
            block.playerCollide(player)
        for block in map.mblocks:
            if block.playerCollide(player):
                if ((block.dir == "N" and (player.dir == "up" or player.dir == "stop up"))
                    or (block.dir == "S" and (player.dir == "down" or player.dir == "stop down"))
                    or (block.dir == "E" and (player.dir == "right" or player.dir == "stop right"))
                    or (block.dir == "W" and (player.dir == "left" or player.dir == "stop left"))
                    or (block.dir == "1" and (player.dir == "up" or player.dir == "stop up"))):
                    map.load(block.newMap)
                    player.place(block.dest)
                
#        for block in map.killblocks:
#            block.lavaCollide(player)
        for block in map.blocks:
            for enemy in enemies:
                if block.distToPoint(enemy.rect.center) < 20:
                    block.enemyCollide(enemy)
        for block in map.killblocks:
            for darkEnemy in darkEnemies:
                if block.distToPoint(darkEnemy.rect.center) < 20:
                    block.enemyCollide(darkEnemy)
        for block in map.lockblocks:
            block.keyCollide(player)
        for block in map.lock2blocks:
            block.keyCollide(player)
            if block.living == False:
                map.lockblocks.remove(block)
        for block in map.oblocks:
            block.playerKeyCollide(player)
            if not block.living:
                map.oblocks.remove(block)
                
        
        
        # boss.attack(player)
        # boss.playerDetect(player)
        # boss.move
        # boss.collide(player)
        for enemy in enemies:
            enemy.collideWall()
            enemy.move()
            sword.attack(enemy, player)
            enemy.attack(player)
            enemy.playerDetect(player)
            enemy.playerCollide(player, healthbar)
            enemy.enemyCollide(enemy)
            if not enemy.living:
                player.hurt = False
                enemies.remove(enemy)
                counter.increase()
        for darkEnemy in darkEnemies:
            darkEnemy.collideWall()
            darkEnemy.move()
            sword.attack(darkEnemy, player)
            darkEnemy.attack(player)
            darkEnemy.playerDetect(player)
            darkEnemy.playerCollide(player, healthbar)
            darkEnemy.enemyCollide(darkEnemy)
            if not darkEnemy.living:
                player.hurt = False
                darkEnemies.remove(darkEnemy)   
                counter.increase(100)               
           
        # print len(enemies)
        # Blitting
        screen.fill(bgColor)
        for block in map.blocks:
            screen.blit(block.surface, block.rect)
        for block in map.floorblocks:
            screen.blit(block.surface, block.rect)
        for block in map.darkblocks:   
            screen.blit(block.surface, block.rect)
        for block in map.enemyblocks:   
            screen.blit(block.surface, block.rect)
        for block in map.oblocks:   
            screen.blit(block.surface, block.rect)
        for block in map.mblocks:   
            screen.blit(block.surface, block.rect)
        for block in map.killblocks:   
            screen.blit(block.surface, block.rect)
        for block in map.lockblocks:   
            screen.blit(block.surface, block.rect)
        screen.blit(player.surface, player.rect)  
        if sword.living == True:
            screen.blit(sword.surface, sword.rect)  
        for enemy in enemies:
            screen.blit(enemy.surface, enemy.rect)
        for darkEnemy in darkEnemies:
            screen.blit(darkEnemy.surface, darkEnemy.rect)    
        for key in keys:
            screen.blit(key.surface, key.rect)
        # screen.blit(boss.surface, boss.rect)  
        screen.blit(healthbar_background.surface, healthbar_background.rect)  
        screen.blit(healthbar.surface, healthbar.rect)  
        screen.blit(energybar_background.surface, energybar_background.rect)  
        screen.blit(energybar.surface, energybar.rect)
        screen.blit(counter.surface, counter.rect)
        if player.hurt == True:
            screen.blit(hurt.surface, hurt.rect)
        if player.living == False:
            run3 = True
            # player.living = True
        pygame.display.flip()
        clk.tick(90)
        
        while run3:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if hgexit.collidePt(event.pos):
                            hgexit.clicked = True
                            run3 = False
                            run = False
                            run2 = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        namept2.switch("left", namept1)
                        namept3.switch("left", namept2)
                        namept4.switch("left", namept3)
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        namept3.switch("right", namept4)
                        namept2.switch("right", namept3)
                        namept1.switch("right", namept2)
                    elif event.key == pygame.K_w or event.key == pygame.K_UP:
                        canScrollUp = True
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        canScrollDown = True
                    elif event.key == pygame.K_RETURN:
                        yourscore.run = True
                        score1.run = True
                        score2.run = True
                        score3.run = True
                        score4.run = True
                        highscorereader.canSend = True
                        namept1.living = False
                        namept2.living = False
                        namept3.living = False
                        namept4.living = False
                        highscorereader.canRun = True
                
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        canScrollUp = False
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        canScrollDown = False
            if canScrollUp == True:
                namept1.scroll("up")
                namept2.scroll("up")
                namept3.scroll("up")
                namept4.scroll("up")
            if canScrollDown == True:
                namept1.scroll("down")
                namept2.scroll("down")
                namept3.scroll("down")
                namept4.scroll("down")
                
            characters =  str(namept1.character)+ str(namept2.character)+ str(namept3.character)+ str(namept4.character)      
            hgexit.update((200, 10, 10))
            namept1.update()                            
            namept2.update()                            
            namept3.update()
            namept4.update()
            yourscore.update(characters)
            highscorereader.reload("rcs/scores.txt", yourscore, counter)
            highscorereader.send("rcs/scores.txt", score1, score2, score3, score4)
            score1.update(score1.display)
            score2.update(score2.display)
            score3.update(score3.display)
            score4.update(score4.display)
            screen.fill(bgColor)
            if namept1.living == True:
                screen.blit(namept1.surface, namept1.rect)
            if namept2.living == True:    
                screen.blit(namept2.surface, namept2.rect)
            if namept3.living == True:
                screen.blit(namept3.surface, namept3.rect)
            if namept4.living == True:
                screen.blit(namept4.surface, namept4.rect)    
            screen.blit(hgexit.surface, hgexit.rect)
            screen.blit(score1.surface, score1.rect)
            screen.blit(score2.surface, score2.rect)
            screen.blit(score3.surface, score3.rect)
            screen.blit(score4.surface, score4.rect)
            pygame.display.flip()    