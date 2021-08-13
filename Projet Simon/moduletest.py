import pygame
from pygame.locals import *
from random import *
from pygame.mixer import*
import time
from random import randint


pygame.init()
pygame.display.init()
pygame.mixer.init()



#couleur
GRIS=(64,64,64)
RED = (150, 0, 0)
RED2=(255,0,0)
GREEN = (0, 150, 0)
GREEN2=(0,255,0)
BLUE = (0, 0, 100)
BLUE2=(0,0,255)
JAUNE=(150,150,0)
JAUNE2=(255,255,0)
NOIR=(0,0,0)

son1 = pygame.mixer.Sound("cowboy.ogg")
son3 = pygame.mixer.Sound("clown.ogg")
son4 = pygame.mixer.Sound("rot.ogg")

fenetre = pygame.display.set_mode((655, 427))
rouge2=pygame.draw.rect(fenetre, RED,[177.5, 113.5, 150, 100])
jaune2=pygame.draw.rect(fenetre, JAUNE,[327.5, 113.5, 150, 100])
pygame.display.flip()

zoner=pygame.Rect(177.5,113.5,150,100)
zoner2=pygame.Surface(rouge2.size)
zonej=pygame.Rect(327.5, 113.5, 150, 100)
zonej2=pygame.Surface(jaune2.size)
pygame.display.flip()

font=pygame.font.Font(None, 24)
#demmarer

dem=pygame.Rect(100, 400, 70, 20)
zone1= pygame.Surface(dem.size)
fenetre.blit(zone1, (100,400))
pygame.display.flip()
text1 = font.render("Demarer",1,(0,255,0))
fenetre.blit(text1,(100,400))
pygame.display.flip()

def rougem():
    son1.play()
    pygame.draw.rect(fenetre, RED2,[177.5, 113.5, 150, 100])
    pygame.display.flip()
    time.sleep(1)
    pygame.draw.rect(fenetre, RED,[177.5, 113.5, 150, 100])
    pygame.display.flip()

def jaunem():
    son3.play()
    pygame.draw.rect(fenetre, JAUNE2, [327.5, 113.5, 150, 100])
    pygame.display.flip()
    time.sleep(1)
    pygame.draw.rect(fenetre, JAUNE, [327.5, 113.5, 150, 100])
    pygame.display.flip()

io=0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == MOUSEBUTTONUP and event.button == 1 and dem.collidepoint(event.pos):
            io=1
            print("por")
        if io==1:
                if event.type == MOUSEBUTTONUP and event.button == 1 and zoner.collidepoint(event.pos):
                    print("touché")
                    rougem()
                    pygame.display.flip()
                    io=3
                elif event.type == MOUSEBUTTONUP and event.button == 1 and zonej.collidepoint(event.pos):
                    print("touché")
                    jaunem()
                    pygame.display.flip()
                    io=3

