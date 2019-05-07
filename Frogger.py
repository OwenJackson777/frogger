import pygame
import sys
import random

from pygame.locals import*
pygame.init()

WINDOW = pygame.display.set_mode((1100,600))

FPS = 60
fpsClock = pygame.time.Clock()


WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (7, 100, 1)
BLUE = (0,0,255)
YELLOW = (255,255,0)
PURPLE = (128,0,255)
PINK = (255,0,210)
PURPLEBLUE = (84,0,255)
BROWN = (130, 94, 33)

scoreVar = "0"
livesVar = "3"

FrogX = 519
FrogY = 498

LogHitRight = "no"
LogHitLeft = "no"

Log1x = 750
Log2x = 250
Log3x = 500
Log4x = 40
Log5x = random.randrange(0,1000)
Log6x = 10
Log7x = 600
Log8x = 890
Log9x = random.randrange(0,1000)
Log10x = random.randrange(0,1000)


font = pygame.font.SysFont("Berlin Sans FB", 40, False, False)
font2 = pygame.font.SysFont("Berlin Sans FB", 70, False, False)
Score = font.render("Score:", True, WHITE)
Final = font.render("Your Final score was:",True,WHITE)
Lives = font.render("Lives:", True, WHITE)
Again = font2.render("Would you like",True, WHITE)
Again2 = font2.render("to play again?",True, WHITE)
Again3 = font2.render("[y/n]",True, WHITE)
lives = font.render(livesVar, True, WHITE)
score = font.render(scoreVar, True, WHITE)

Frog = pygame.image.load("Frog.jpg")

pygame.display.set_caption("Frogger!")

while True:

    for event in pygame.event.get():

        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                FrogY = FrogY - 62
                print(FrogX,":",FrogY)
            elif event.key == pygame.K_s:
                FrogY = FrogY + 62
                print(FrogX,":",FrogY)
            elif event.key == pygame.K_a:
                FrogX = FrogX - 31
            elif event.key == pygame.K_d:
                FrogX = FrogX + 31
            elif event.key == pygame.K_y and int(livesVar) < 0:
                livesVar = "3"
                scoreVar = "0"
                FrogX = 519
                FrogY = 498
            elif event.key == pygame.K_n and int(livesVar) < 0:
                exit()
    
    WINDOW.fill(PURPLEBLUE)
    WINDOW.blit(Lives, (250,560))
    WINDOW.blit(Score, (720,560))
    pygame.draw.line(WINDOW, BLACK, (0, 560), (1100, 560), 5)
    pygame.draw.rect(WINDOW, BLUE,(0,0,1100,559))
    pygame.draw.rect(WINDOW, GREEN,(0,498,1100,62))
    pygame.draw.rect(WINDOW, GREEN,(0,250,1100,62))
    pygame.draw.rect(WINDOW, GREEN,(0,0,1100,64))
    pygame.draw.rect(WINDOW, BROWN,(Log1x,440,200,54))
    pygame.draw.rect(WINDOW, BROWN,(Log2x,440,200,54))
    pygame.draw.rect(WINDOW, BROWN,(Log3x,378,200,54))
    pygame.draw.rect(WINDOW, BROWN,(Log4x,378,200,54))
    pygame.draw.rect(WINDOW, BROWN,(Log5x,316,200,54))
    pygame.draw.rect(WINDOW, BROWN,(Log6x,192,200,54))
    pygame.draw.rect(WINDOW, BROWN,(Log7x,192,200,54))
    pygame.draw.rect(WINDOW, BROWN,(Log8x,192,200,54))
    pygame.draw.rect(WINDOW, BROWN,(Log9x,130,200,54))
    pygame.draw.rect(WINDOW, BROWN,(Log10x,68,200,54))

    Log1x = Log1x + 4
    Log2x = Log2x + 4
    Log3x = Log3x - 4
    Log4x = Log4x - 4
    Log5x = Log5x + 4
    Log6x = Log6x - 4
    Log7x = Log7x - 4
    Log8x = Log8x - 4
    Log9x = Log9x + 4
    Log10x = Log10x - 4
    if Log1x >= 1100:
        Log1x = -200
    if Log2x >= 1100:
        Log2x = -200
    if Log3x <= -200:
        Log3x = 1100
    if Log4x <= -200:
        Log4x = 1100
    if Log5x >= 1100:
        Log5x = -200
    if Log6x <= -200:
        Log6x = 1100
    if Log7x <= -200:
        Log7x = 1100
    if Log8x <= -200:
        Log8x = 1100
    if Log9x >= 1100:
        Log9x = -200
    if Log10x <= -200:
        Log10x = 1100
    
    WINDOW.blit(Frog,(FrogX,FrogY))

    if FrogY == 498:
        LogHitRight = "no"
        LogHitLeft = "no"     

    if FrogY == 436:
        if FrogX >= Log1x and FrogX + 62 <= Log1x + 200:
            LogHitRight = "yes"
            LogHitLeft = "no"
        elif FrogX >= Log2x and FrogX + 62 <= Log2x + 200:
            LogHitRight = "yes"
            LogHitLeft = "no"
        else:
            FrogX = 519
            FrogY = 498
            LogHitRight = "no"
            LogHitLeft = "no"
            livesVar = int(livesVar) - 1
    if FrogY == 374:
        if FrogX >= Log3x and FrogX + 62 <= Log3x + 200:
            LogHitLeft = "yes"
            LogHitRight = "no"
        elif FrogX >= Log4x and FrogX + 62 <= Log4x + 200:
            LogHitLeft = "yes"
            LogHitRight = "no"
        else:
            FrogX = 519
            FrogY = 498
            LogHitLeft = "no"
            LogHitRight = "no"
            livesVar = int(livesVar) - 1
    if FrogY == 312:
        if FrogX >= Log5x and FrogX + 62 <= Log5x + 200:
            LogHitLeft = "no"
            LogHitRight = "yes"
        else:
            FrogX = 519
            FrogY = 498
            LogHitLeft = "no"
            LogHitRight = "no"
            livesVar = int(livesVar) - 1
    if FrogY == 250:
        LogHitRight = "no"
        LogHitLeft = "no"
    if FrogY == 188:
        if FrogX >= Log6x and FrogX + 62 <= Log6x + 200:
            LogHitLeft = "yes"
            LogHitRight = "no"
        elif FrogX >= Log7x and FrogX + 62 <= Log7x + 200:
            LogHitLeft = "yes"
            LogHitRight = "no"
        elif FrogX >= Log8x and FrogX + 62 <= Log8x + 200:
            LogHitLeft = "yes"
            LogHitRight = "no"
        else:
            FrogX = 519
            FrogY = 498
            LogHitLeft = "no"
            LogHitRight = "no"
            livesVar = int(livesVar) - 1
    if FrogY == 126:
        if FrogX >= Log9x and FrogX + 62 <= Log9x + 200:
            LogHitLeft = "no"
            LogHitRight = "yes"
        else:
            FrogX = 519
            FrogY = 498
            LogHitLeft = "no"
            LogHitRight = "no"
            livesVar = int(livesVar) - 1
    if FrogY == 64:
        if FrogX >= Log10x and FrogX + 62 <= Log10x + 200:
            LogHitLeft = "yes"
            LogHitRight = "no"
        else:
            FrogX = 519
            FrogY = 498
            LogHitLeft = "no"
            LogHitRight = "no"
            livesVar = int(livesVar) - 1
    if FrogY == 2:
        FrogX = 519
        FrogY = 498
        LogHitRight = "no"
        LogHitLeft = "no"
        scoreVar = int(scoreVar) + 1

    if LogHitRight == "yes":
        FrogX = FrogX + 4
    if LogHitLeft == "yes":
        FrogX = FrogX - 4

    if FrogY > 498:
        FrogX = 519
        FrogY = 498
    if FrogX >= 1100 or FrogX <= -64:
        FrogX = 519
        FrogY = 498
        LogHitRight = "no"
        LogHitLeft = "no"
        livesVar = int(livesVar) - 1

    lives = font.render(str(livesVar), True, WHITE)
    score = font.render(str(scoreVar), True, WHITE)
    WINDOW.blit(score, (840,560))
    WINDOW.blit(lives, (370,560))

    if int(livesVar) < 0:
        WINDOW.fill(PURPLEBLUE)
        WINDOW.blit(Again, (300,30))
        WINDOW.blit(Again2, (300,100))
        WINDOW.blit(Again3, (300,170))
        WINDOW.blit(Final, (300,400))
        WINDOW.blit(score, (660,400))
          
    pygame.display.update()
    fpsClock.tick(FPS)
