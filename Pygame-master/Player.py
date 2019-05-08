import Game
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
        if self.walkCount + 1 >= 27:
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
                goblin.health = 10
                self.health = 10
                #REsets to left portion of screen
                self.isJump = False
                self.jumpCount = 10
                self.x = 60
                self.y = 410
                #sets the anaimation of the walk to zero so not wierd looking while spawning back
                self.walkCount = 0
