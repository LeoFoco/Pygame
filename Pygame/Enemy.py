#All the imports
import pygame
from Settings import *


#Code below makes the enemy
class enemy(object):
    #Imports images
    walkRight = [pygame.image.load('Enemy/E0.png'), pygame.image.load('Enemy/E1.png'), pygame.image.load('Enemy/E2.png'), pygame.image.load('Enemy/E3.png'), pygame.image.load('Enemy/E4.png')]
    walkLeft = [pygame.image.load('Enemy/E0.png'), pygame.image.load('Enemy/E1.png'), pygame.image.load('Enemy/E2.png'), pygame.image.load('Enemy/E3.png'), pygame.image.load('Enemy/E4.png')]

    #Variables for enemy
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True

    #Draws the enemy
    def draw(self,win):
        self.move()

        #Saying if the goblin if visible then it will move left or right if not it will not be moving 
        if self.visible:
            if self.walkCount + 1 >= 15:
                self.walkCount = 0

            #Makes the enemy walk right animation only if visible
            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1

            #Makes the enemy walk left animation if visible only
            else:
                win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1

            #Health Bar
            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10)) 
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))

            #Make the hitbox
            self.hitbox = (self.x + 0, self.y + 2, 64, 64)
            #Display Hitbox
            pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    #Makes the goblin path
    def move(self):
        #Walks right i think
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

        #Walks left i think
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    #Code for if the bullet hits the Enemy
    def hit(self):
        if self.health > 1:
            self.health -= 1
        #If the enemy has less than one health then it will do the following
        else:
            self.visible = False
            print('Ow my bones')
