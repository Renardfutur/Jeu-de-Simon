import pygame
from pygame.locals import *
from random import *
from pygame.mixer import*
import time
from pygame.time import*
from random import randint




pygame.init()
pygame.display.init()
pygame.mixer.init()

#couleur
GRIS=(64,64,64)
RED = (100, 0, 0)
RED2=(255,0,0)
GREEN = (0, 100, 0)
GREEN2=(0,255,0)
BLUE = (0, 0, 100)
BLUE2=(0,0,255)
JAUNE=(100,100,0)
JAUNE2=(255,255,0)
VIOLET2=(255,0,255)
VIOLET=(150,0,150)
ORANGE2=(255,155,0)
ORANGE=(190,90,0)
NOIR=(0,0,0)



#plateau
fenetre = pygame.display.set_mode((655, 427))
rougeu=pygame.draw.rect(fenetre, RED,[260, 105, 150, 100])
jauneu=pygame.draw.rect(fenetre, JAUNE,[420, 105, 150, 100])
vertu=pygame.draw.rect(fenetre, GREEN, [260, 220, 150, 100])
bleuu=pygame.draw.rect(fenetre, BLUE, [420, 220, 150, 100])
violetu=pygame.draw.rect(fenetre, VIOLET, [100, 105, 150, 100])
orangeu=pygame.draw.rect(fenetre, ORANGE, [100, 220, 150, 100])
pygame.draw.rect(fenetre, NOIR,[0, 95, 800, 240])


rouge2=pygame.draw.rect(fenetre, RED,[170, 105, 150, 100])
jaune2=pygame.draw.rect(fenetre, JAUNE,[330, 105, 150, 100])
vert2=pygame.draw.rect(fenetre, GREEN, [170, 220, 150, 100])
bleu2=pygame.draw.rect(fenetre, BLUE, [330, 220, 150, 100])
pygame.draw.rect(fenetre, NOIR,[0, 95, 800, 240])


#touché
zoner=pygame.Rect(170,105,150,100)
zoner2=pygame.Surface(rouge2.size)
zonej=pygame.Rect(330, 105, 150, 100)
zonej2=pygame.Surface(jaune2.size)
zonev=pygame.Rect(170, 220, 150, 100)
zonev2=pygame.Surface(vert2.size)
zoneb=pygame.Rect(330, 220, 150, 100)
zoneb2=pygame.Surface(bleu2.size)

#touché difficile
zoner1=pygame.Rect(260,105,150,100)
zoner3=pygame.Surface(rougeu.size)
zonej1=pygame.Rect(420, 105, 150, 100)
zonej3=pygame.Surface(jauneu.size)
zonev1=pygame.Rect(260, 220, 150, 100)
zonev3=pygame.Surface(vertu.size)
zoneb1=pygame.Rect(420, 220, 150, 100)
zoneb3=pygame.Surface(bleuu.size)
zonevi1=pygame.Rect(100, 105, 150, 100)
zonevi3=pygame.Surface(zonevi1.size)
zoneo1=pygame.Rect(100, 200, 150, 100)
zoneo3=pygame.Surface(zoneo1.size)





#son
son2 = pygame.mixer.Sound("monkey.ogg")
son1 = pygame.mixer.Sound("cowboy.ogg")
son3 = pygame.mixer.Sound("clown.ogg")
son4 = pygame.mixer.Sound("rot.ogg")
son5=pygame.mixer.Sound("error.ogg")
son6=pygame.mixer.Sound("bulle.ogg")
son7=pygame.mixer.Sound("cloche.ogg")




pygame.time.get_ticks()


#def

def rougem():
    son1.play()
    pygame.draw.rect(fenetre, RED2,[170, 105, 150, 100])
    pygame.display.flip()
    time.sleep(0.5)
    pygame.draw.rect(fenetre, RED,[170, 105, 150, 100])
    pygame.display.flip()
    time.sleep(0.2)

def bleum():
    son2.play()
    pygame.draw.rect(fenetre, BLUE2,[330, 220, 150, 100])
    pygame.display.flip()
    time.sleep(0.5)
    pygame.draw.rect(fenetre, BLUE,[330, 220, 150, 100])
    pygame.display.flip()
    time.sleep(0.2)

def jaunem():
    son3.play()
    pygame.draw.rect(fenetre, JAUNE2, [330, 105, 150, 100])
    pygame.display.flip()
    time.sleep(0.5)
    pygame.draw.rect(fenetre, JAUNE, [330, 105, 150, 100])
    pygame.display.flip()
    time.sleep(0.2)
def vertm():
    son4.play()
    pygame.draw.rect(fenetre, GREEN2, [170, 220, 150, 100])
    pygame.display.flip()
    time.sleep(0.5)
    pygame.draw.rect(fenetre, GREEN, [170, 220, 150, 100])
    pygame.display.flip()
    time.sleep(0.2)
#version dur
def rouged():
    son1.play()
    pygame.draw.rect(fenetre, RED2,[260, 105, 150, 100])
    pygame.display.flip()
    time.sleep(0.2)
    pygame.draw.rect(fenetre, RED,[260, 105, 150, 100])
    pygame.display.flip()
    time.sleep(0.2)

def bleud():
    son2.play()
    pygame.draw.rect(fenetre, BLUE2,[420, 220, 150, 100])
    pygame.display.flip()
    time.sleep(0.2)
    pygame.draw.rect(fenetre, BLUE,[420, 220, 150, 100])
    pygame.display.flip()
    time.sleep(0.2)

def jauned():
    son3.play()
    pygame.draw.rect(fenetre, JAUNE2, [420, 105, 150, 100])
    pygame.display.flip()
    time.sleep(0.2)
    pygame.draw.rect(fenetre, JAUNE, [420, 105, 150, 100])
    pygame.display.flip()
    time.sleep(0.2)
def vertd():
    son4.play()
    pygame.draw.rect(fenetre, GREEN2, [260, 220, 150, 100])
    pygame.display.flip()
    time.sleep(0.2)
    pygame.draw.rect(fenetre, GREEN, [260, 220, 150, 100])
    pygame.display.flip()
    time.sleep(0.2)
def violetd():
    son7.play()
    pygame.draw.rect(fenetre, VIOLET2, [100, 105, 150, 100])
    pygame.display.flip()
    time.sleep(0.2)
    pygame.draw.rect(fenetre, VIOLET, [100, 105, 150, 100])
    pygame.display.flip()
    time.sleep(0.2)
def oranged():
    son6.play()
    pygame.draw.rect(fenetre, ORANGE2, [100, 220, 150, 100])
    pygame.display.flip()
    time.sleep(0.2)
    pygame.draw.rect(fenetre, ORANGE, [100, 220, 150, 100])
    pygame.display.flip()
    time.sleep(0.2)




def seq(no):
    if v==0:
        no.append(v)
    if v==1:
        no.append(v)
    if v==2:
        no.append(v)
    if v==3:
        no.append(v)
    if v==4:
        no.append(v)
    if v==5:
        no.append(v)




font=pygame.font.Font(None, 45)
pygame.draw.rect(fenetre, BLUE, [25, 350, 110, 25])
#quitter

quitter=pygame.Rect(25, 350, 110, 25)
zone= pygame.Surface(quitter.size)
fenetre.blit(zone, (25, 350))
pygame.display.flip()
text = font.render("Quitter",1,(255,155,0))
fenetre.blit(text,(25,350))
pygame.display.flip()

#demmarer

dem=pygame.Rect(25, 25, 140, 28)
zone1= pygame.Surface(dem.size)
fenetre.blit(zone1, (25,25))
pygame.display.flip()
text1 = font.render("Demarer",1,(0,0,255))
fenetre.blit(text1,(25,25))
pygame.display.flip()

#difficulté
dif=pygame.Rect(25, 125, 120, 28)
zone7= pygame.Surface(dif.size)
fenetre.blit(zone7, (25,125))
pygame.display.flip()
text1 = font.render("Difficile",1,(150,0,0))
fenetre.blit(text1,(25,125))
pygame.display.flip()

dif2=pygame.Rect(25, 225, 95, 25)
zone8= pygame.Surface(dif.size)
fenetre.blit(zone8, (25,225))
pygame.display.flip()
text1 = font.render("Facile",1,(0,150,0))
fenetre.blit(text1,(25, 225))
pygame.display.flip()

#meilleur score
text1 = font.render("Votre score:",1,(255,255,255))
fenetre.blit(text1,(250,25))
pygame.display.flip()





pygame.display.flip()
diffic=0
touche=0
compo=[0,1,2,3]
compod=[0,1,2,3,4,5]
continuer=2
demar=0


#pour demmarer et quitter

while True:
    for event in pygame.event.get():
            if demar==0:
                if event.type == QUIT:
                    pygame.quit()
                elif event.type == MOUSEBUTTONUP and event.button == 1 and quitter.collidepoint(event.pos):
                    pygame.quit()
                if event.type == MOUSEBUTTONUP and event.button ==1 and dem.collidepoint(event.pos):
                    nob=1
                    o=0
                    tail=0
                    h=1
                    uil=[]
                    demar=1
                    continuer=1
                    sco=0
                    if diffic==0:
                        pygame.draw.rect(fenetre, NOIR,[0, 0, 1000, 600])
                        rouge2=pygame.draw.rect(fenetre, RED,[170, 105, 150, 100])
                        jaune2=pygame.draw.rect(fenetre, JAUNE,[330, 105, 150, 100])
                        vert2=pygame.draw.rect(fenetre, GREEN, [170, 220, 150, 100])
                        bleu2=pygame.draw.rect(fenetre, BLUE, [330, 220, 150, 100])
                        pygame.display.flip()
                    elif diffic==1:
                        pygame.draw.rect(fenetre, NOIR,[0, 0, 1000, 600])
                        rougeu=pygame.draw.rect(fenetre, RED,[260, 105, 150, 100])
                        jauneu=pygame.draw.rect(fenetre, JAUNE,[420, 105, 150, 100])
                        vertu=pygame.draw.rect(fenetre, GREEN, [260, 220, 150, 100])
                        bleuu=pygame.draw.rect(fenetre, BLUE, [420, 220, 150, 100])
                        violetu=pygame.draw.rect(fenetre, VIOLET, [100, 105, 150, 100])
                        orangeu=pygame.draw.rect(fenetre, ORANGE, [100, 220, 150, 100])
                        pygame.display.flip()
                elif event.type == MOUSEBUTTONUP and event.button == 1 and dif.collidepoint(event.pos):
                    diffic=1
                    pygame.draw.rect(fenetre, NOIR,[25, 125, 120, 28])
                    text1 = font.render("Difficile",1,(255,0,0))
                    fenetre.blit(text1,(25,125))
                    text1 = font.render("Facile",1,(0,150,0))
                    fenetre.blit(text1,(25,225))
                    pygame.display.flip()
                elif event.type == MOUSEBUTTONUP and event.button == 1 and dif2.collidepoint(event.pos):
                    diffic=0
                    pygame.draw.rect(fenetre, NOIR,[25, 225, 95, 25])
                    text1 = font.render("Facile",1,(0,255,0))
                    fenetre.blit(text1,(25,225))
                    text1 = font.render("Difficile",1,(150,0,0))
                    fenetre.blit(text1,(25,125))
                    pygame.display.flip()
            if continuer==1:
                lm=0
                lene=len(uil)
                if diffic==0:
                    for i in range(1):
                                print("jeu")
                                v=choice(compo)
                                seq(uil)
                                print(uil)
                    for i in range(lene+1):
                                if uil[lm]==0:
                                    rougem()
                                if uil[lm]==1:
                                    vertm()
                                if uil[lm]==2:
                                    bleum()
                                if uil[lm]==3:
                                    jaunem()
                                lm+=1
                elif diffic==1:
                    for i in range(1):
                                print("jeu")
                                v=choice(compod)
                                seq(uil)
                                print(uil)
                    for i in range(lene+1):
                                if uil[lm]==0:
                                    rouged()
                                if uil[lm]==1:
                                    vertd()
                                if uil[lm]==2:
                                    bleud()
                                if uil[lm]==3:
                                    jauned()
                                if uil[lm]==4:
                                    violetd()
                                if uil[lm]==5:
                                    oranged()
                                lm+=1
                touche=1
                continuer=2
                o=0
                der=0
                jou=[]
            elif touche==1:
                if diffic==0:
                    if event.type == MOUSEBUTTONDOWN and event.button == 1 and zoner.collidepoint(event.pos):
                        jou.append(0)
                        if jou[o]==uil[o]:
                            der+=1
                            rougem()
                            o+=1
                        elif jou[o]!=uil[o]:
                            son5.play()
                            print("perdu")
                            pygame.draw.rect(fenetre, NOIR,[0, 0, 1000, 600])
                            text = font.render("Quitter",1,(255,155,0))
                            fenetre.blit(text,(25,350))
                            text1 = font.render("Demarer",1,(0,0,255))
                            fenetre.blit(text1,(25,25))
                            text1 = font.render("Difficile",1,(150,0,0))
                            fenetre.blit(text1,(25,125))
                            text1 = font.render("Facile",1,(0,150,0))
                            fenetre.blit(text1,(25, 225))
                            text1 = font.render("Votre score:",1,(255,255,255))
                            fenetre.blit(text1,(250,25))
                            text1 = font.render(str(sco),1,(255,255,255))
                            fenetre.blit(text1,(250,50))
                            pygame.display.flip()
                            demar=0
                            touche=2
                    if event.type == MOUSEBUTTONDOWN and event.button == 1 and zonev.collidepoint(event.pos):
                        jou.append(1)
                        if jou[o]==uil[o]:
                            der+=1
                            vertm()
                            o+=1
                        elif jou[o]!=uil[o]:
                            son5.play()
                            print("perdu")
                            pygame.draw.rect(fenetre, NOIR,[0, 0, 1000, 600])
                            text = font.render("Quitter",1,(255,155,0))
                            fenetre.blit(text,(25,350))
                            text1 = font.render("Demarer",1,(0,0,255))
                            fenetre.blit(text1,(25,25))
                            text1 = font.render("Difficile",1,(150,0,0))
                            fenetre.blit(text1,(25,125))
                            text1 = font.render("Facile",1,(0,150,0))
                            fenetre.blit(text1,(25, 225))
                            text1 = font.render("Meilleur Score:",1,(255,255,255))
                            fenetre.blit(text1,(250,25))
                            text1 = font.render(str(sco),1,(255,255,255))
                            fenetre.blit(text1,(250,50))
                            pygame.display.flip()
                            demar=0
                            touche=2
                    if event.type == MOUSEBUTTONDOWN and event.button == 1 and zoneb.collidepoint(event.pos):
                        jou.append(2)
                        if jou[o]==uil[o]:
                            der+=1
                            bleum()
                            o+=1
                        elif jou[o]!=uil[o]:
                            son5.play()
                            print("perdu")
                            pygame.draw.rect(fenetre, NOIR,[0, 0, 1000, 600])
                            text = font.render("Quitter",1,(255,155,0))
                            fenetre.blit(text,(25,350))
                            text1 = font.render("Demarer",1,(0,0,255))
                            fenetre.blit(text1,(25,25))
                            text1 = font.render("Difficile",1,(150,0,0))
                            fenetre.blit(text1,(25,125))
                            text1 = font.render("Facile",1,(0,150,0))
                            fenetre.blit(text1,(25, 225))
                            text1 = font.render("Meilleur Score:",1,(255,255,255))
                            fenetre.blit(text1,(250,25))
                            text1 = font.render(str(sco),1,(255,255,255))
                            fenetre.blit(text1,(250,50))
                            pygame.display.flip()
                            demar=0
                            touche=2
                    if event.type == MOUSEBUTTONDOWN and event.button == 1 and zonej.collidepoint(event.pos):
                        jou.append(3)
                        if jou[o]==uil[o]:
                            der+=1
                            jaunem()
                            o+=1
                        elif jou[o]!=uil[o]:
                            son5.play()
                            print("perdu")
                            pygame.draw.rect(fenetre, NOIR,[0, 0, 1000, 600])
                            text = font.render("Quitter",1,(255,155,0))
                            fenetre.blit(text,(25,350))
                            text1 = font.render("Demarer",1,(0,0,255))
                            fenetre.blit(text1,(25,25))
                            text1 = font.render("Difficile",1,(150,0,0))
                            fenetre.blit(text1,(25,125))
                            text1 = font.render("Facile",1,(0,150,0))
                            fenetre.blit(text1,(25, 225))
                            text1 = font.render("Meilleur Score:",1,(255,255,255))
                            fenetre.blit(text1,(250,25))
                            text1 = font.render(str(sco),1,(255,255,255))
                            fenetre.blit(text1,(250,50))
                            pygame.display.flip()
                            demar=0
                            touche=2
                elif diffic==1:
                    if event.type == MOUSEBUTTONDOWN and event.button == 1 and zoner1.collidepoint(event.pos):
                        jou.append(0)
                        if jou[o]==uil[o]:
                            der+=1
                            rouged()
                            o+=1
                        elif jou[o]!=uil[o]:
                            son5.play()
                            print("perdu")
                            pygame.draw.rect(fenetre, NOIR,[0, 0, 1000, 600])
                            text = font.render("Quitter",1,(255,155,0))
                            fenetre.blit(text,(25,350))
                            text1 = font.render("Demarer",1,(0,0,255))
                            fenetre.blit(text1,(25,25))
                            text1 = font.render("Difficile",1,(150,0,0))
                            fenetre.blit(text1,(25,125))
                            text1 = font.render("Facile",1,(0,150,0))
                            fenetre.blit(text1,(25, 225))
                            text1 = font.render("Meilleur Score:",1,(255,255,255))
                            fenetre.blit(text1,(250,25))
                            text1 = font.render(str(sco),1,(255,255,255))
                            fenetre.blit(text1,(250,50))
                            pygame.display.flip()
                            demar=0
                            touche=2
                    if event.type == MOUSEBUTTONDOWN and event.button == 1 and zonev1.collidepoint(event.pos):
                        jou.append(1)
                        if jou[o]==uil[o]:
                            der+=1
                            vertd()
                            o+=1
                        elif jou[o]!=uil[o]:
                            son5.play()
                            print("perdu")
                            pygame.draw.rect(fenetre, NOIR,[0, 0, 1000, 600])
                            text = font.render("Quitter",1,(255,155,0))
                            fenetre.blit(text,(25,350))
                            text1 = font.render("Demarer",1,(0,0,255))
                            fenetre.blit(text1,(25,25))
                            text1 = font.render("Difficile",1,(150,0,0))
                            fenetre.blit(text1,(25,125))
                            text1 = font.render("Facile",1,(0,150,0))
                            fenetre.blit(text1,(25, 225))
                            text1 = font.render("Meilleur Score:",1,(255,255,255))
                            fenetre.blit(text1,(250,25))
                            text1 = font.render(str(sco),1,(255,255,255))
                            fenetre.blit(text1,(250,50))
                            pygame.display.flip()
                            demar=0
                            touche=2
                    if event.type == MOUSEBUTTONDOWN and event.button == 1 and zoneb1.collidepoint(event.pos):
                        jou.append(2)
                        if jou[o]==uil[o]:
                            der+=1
                            bleud()
                            o+=1
                        elif jou[o]!=uil[o]:
                            son5.play()
                            print("perdu")
                            pygame.draw.rect(fenetre, NOIR,[0, 0, 1000, 600])
                            text = font.render("Quitter",1,(255,155,0))
                            fenetre.blit(text,(25,350))
                            text1 = font.render("Demarer",1,(0,0,255))
                            fenetre.blit(text1,(25,25))
                            text1 = font.render("Difficile",1,(150,0,0))
                            fenetre.blit(text1,(25,125))
                            text1 = font.render("Facile",1,(0,150,0))
                            fenetre.blit(text1,(25, 225))
                            text1 = font.render("Meilleur Score:",1,(255,255,255))
                            fenetre.blit(text1,(250,25))
                            text1 = font.render(str(sco),1,(255,255,255))
                            fenetre.blit(text1,(250,50))
                            pygame.display.flip()
                            demar=0
                            touche=2
                    if event.type == MOUSEBUTTONDOWN and event.button == 1 and zonej1.collidepoint(event.pos):
                        jou.append(3)
                        if jou[o]==uil[o]:
                            der+=1
                            jauned()
                            o+=1
                        elif jou[o]!=uil[o]:
                            son5.play()
                            print("perdu")
                            pygame.draw.rect(fenetre, NOIR,[0, 0, 1000, 600])
                            text = font.render("Quitter",1,(255,155,0))
                            fenetre.blit(text,(25,350))
                            text1 = font.render("Demarer",1,(0,0,255))
                            fenetre.blit(text1,(25,25))
                            text1 = font.render("Difficile",1,(150,0,0))
                            fenetre.blit(text1,(25,125))
                            text1 = font.render("Facile",1,(0,150,0))
                            fenetre.blit(text1,(25, 225))
                            text1 = font.render("Meilleur Score:",1,(255,255,255))
                            fenetre.blit(text1,(250,25))
                            text1 = font.render(str(sco),1,(255,255,255))
                            fenetre.blit(text1,(250,50))
                            pygame.display.flip()
                            demar=0
                            touche=2
                    if event.type == MOUSEBUTTONDOWN and event.button == 1 and zonevi1.collidepoint(event.pos):
                        jou.append(4)
                        if jou[o]==uil[o]:
                            der+=1
                            violetd()
                            o+=1
                        elif jou[o]!=uil[o]:
                            son5.play()
                            print("perdu")
                            pygame.draw.rect(fenetre, NOIR,[0, 0, 1000, 600])
                            text = font.render("Quitter",1,(255,155,0))
                            fenetre.blit(text,(25,350))
                            text1 = font.render("Demarer",1,(0,0,255))
                            fenetre.blit(text1,(25,25))
                            text1 = font.render("Difficile",1,(150,0,0))
                            fenetre.blit(text1,(25,125))
                            text1 = font.render("Facile",1,(0,150,0))
                            fenetre.blit(text1,(25, 225))
                            text1 = font.render("Meilleur Score:",1,(255,255,255))
                            fenetre.blit(text1,(250,25))
                            text1 = font.render(str(sco),1,(255,255,255))
                            fenetre.blit(text1,(250,50))
                            pygame.display.flip()
                            demar=0
                            touche=2
                    if event.type == MOUSEBUTTONDOWN and event.button == 1 and zoneo1.collidepoint(event.pos):
                        jou.append(5)
                        if jou[o]==uil[o]:
                            der+=1
                            oranged()
                            o+=1
                        elif jou[o]!=uil[o]:
                            son5.play()
                            print("perdu")
                            pygame.draw.rect(fenetre, NOIR,[0, 0, 1000, 600])
                            text = font.render("Quitter",1,(255,155,0))
                            fenetre.blit(text,(25,350))
                            text1 = font.render("Demarer",1,(0,0,255))
                            fenetre.blit(text1,(25,25))
                            text1 = font.render("Difficile",1,(150,0,0))
                            fenetre.blit(text1,(25,125))
                            text1 = font.render("Facile",1,(0,150,0))
                            fenetre.blit(text1,(25, 225))
                            text1 = font.render("Meilleur Score:",1,(255,255,255))
                            fenetre.blit(text1,(250,25))
                            text1 = font.render(str(sco),1,(255,255,255))
                            fenetre.blit(text1,(475,50))
                            pygame.display.flip()
                            demar=0
                            touche=2
                if der==lene+1 and jou==uil:
                        touche=2
                        continuer=1
                        sco+=1


















#if event.type == MOUSEBUTTONUP and event.button == 1 and zoner.collidepoint(event.pos):
#if event.type == MOUSEBUTTONUP and event.button == 1 and zonev.collidepoint(event.pos):
#if event.type == MOUSEBUTTONUP and event.button == 1 and zoneb.collidepoint(event.pos):
#if event.type == MOUSEBUTTONUP and event.button == 1 and zonej.collidepoint(event.pos):





































