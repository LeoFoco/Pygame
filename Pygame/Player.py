#All the imports
import pygame
from Settings import *
from Enemy import *



#First row, player wlaking right, second row player walking left, third row background, fourth standing animation which is inc.
walkRight = [pygame.image.load('PlayerRight/R00.png'), pygame.image.load('PlayerRight/R01.png'), pygame.image.load('PlayerRight/R02.png'), pygame.image.load('PlayerRight/R03.png'), pygame.image.load('PlayerRight/R04.png'), pygame.image.load('PlayerRight/R05.png'), pygame.image.load('PlayerRight/R06.png'), pygame.image.load('PlayerRight/R07.png'), pygame.image.load('PlayerRight/R08.png'), pygame.image.load('PlayerRight/R09.png'), pygame.image.load('PlayerRight/R10.png'), pygame.image.load('PlayerRight/R11.png')]
walkLeft = [pygame.image.load('PlayerLeft/L00.png'), pygame.image.load('PlayerLeft/L01.png'), pygame.image.load('PlayerLeft/L02.png'), pygame.image.load('PlayerLeft/L03.png'), pygame.image.load('PlayerLeft/L04.png'), pygame.image.load('PlayerLeft/L05.png'), pygame.image.load('PlayerLeft/L06.png'), pygame.image.load('PlayerLeft/L07.png'), pygame.image.load('PlayerLeft/L08.png'), pygame.image.load('PlayerLeft/L09.png'), pygame.image.load('PlayerLeft/L10.png'), pygame.image.load('PlayerLeft/L11.png')]
AL = [pygame.image.load('Background/AL00.png'), pygame.image.load('Background/AL01.png'), pygame.image.load('Background/AL02.png'), pygame.image.load('Background/AL03.png'), pygame.image.load('Background/AL04.png'), pygame.image.load('Background/AL05.png'), pygame.image.load('Background/AL06.png'), pygame.image.load('Background/AL07.png'), pygame.image.load('Background/AL08.png'), pygame.image.load('Background/AL09.png'), pygame.image.load('Background/AL10.png'), pygame.image.load('Background/AL11.png'), pygame.image.load('Background/AL12.png')]
char = pygame.image.load('Random/S00.png')


#All the variables
class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x +17, self.y + 11, 29, 57)
        self.health = 10


    #Charcter movement
    def draw(self, win):
        if self.walkCount + 1 >= 36:
            self.walkCount = 0

        #If the player isn't standing if statement
        if not (self.standing):

            #Moving left
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1

            #Moving Right
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1

        #Standing
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))

        #Hitbox for player  
        #For self.y it changes base, then height 
        #For self.x in changes poistion on the grid you set
        self.hitbox = (self.x +17, self.y + 4, 29, 60)
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

        #Health Bar
        pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10)) 
        pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))


    #If the player gets hit/collides with enemy
    def hit(self):
        if self.health > 0:
            self.health -= 1

            #THis basically restarts the game atm if you die
            if self.health <= 0:
                #REsets score
                global score
                score = 1
                #Will reset everyones health
                enemy.health = 10
                self.health = 10
                #REsets to left portion of screen
                self.isJump = False
                self.jumpCount = 10
                self.x = 0
                self.y = 675
                #sets the anaimation of the walk to zero so not wierd looking while spawning back
                self.walkCount = 0

