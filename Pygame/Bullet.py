import pygame 
#Bullet
class projectile(object):
    #Variables
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color 
        self.facing = facing
        self.vel = 8 * facing
    #Bullet style/draw
    def draw(self,win):
        pygame.draw.circle(win,self.color, (self.x,self.y), self.radius)
