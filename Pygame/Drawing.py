import pygame
from Settings import *
from Enemy import *
from Player import *
from Bullet import *
pygame.init()

backgroundState = 0

#This is how you put stuff onto the display/window
def redrawGameWindow():
    global backgroundState
    #Speed of frames a second
    backgroundState += .25
    #Calls the anaimatipn sort of
    if backgroundState > 12:
        backgroundState = 0
    win.blit(AL[round(backgroundState)], (0,0))
    text = font.render('Score: ' + str(score), 1, (0,0,0))
    win.blit(text, (10,10))
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()
    #p1 = Platform(0, HEIGHT-40, WIDTH, 40)
