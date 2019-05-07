import pygame
pygame.init()

#Displats the screen
win = pygame.display.set_mode((500,480))

#Sets the name of the window
pygame.display.set_caption("First Game")

#First row, player wlaking right, second row player walking left, third row background, fourth standing animation which is inc.
walkRight = [pygame.image.load('GameImages/R00.png'), pygame.image.load('GameImages/R01.png'), pygame.image.load('GameImages/R02.png'), pygame.image.load('GameImages/R03.png'), pygame.image.load('GameImages/R04.png'), pygame.image.load('GameImages/R05.png'), pygame.image.load('GameImages/R06.png'), pygame.image.load('GameImages/R07.png'), pygame.image.load('GameImages/R08.png'), pygame.image.load('GameImages/R09.png'), pygame.image.load('GameImages/R10.png'), pygame.image.load('GameImages/R11.png')]
walkLeft = [pygame.image.load('GameImages/L00.png'), pygame.image.load('GameImages/L01.png'), pygame.image.load('GameImages/L02.png'), pygame.image.load('GameImages/L03.png'), pygame.image.load('GameImages/L04.png'), pygame.image.load('GameImages/L05.png'), pygame.image.load('GameImages/L06.png'), pygame.image.load('GameImages/L07.png'), pygame.image.load('GameImages/L08.png'), pygame.image.load('GameImages/L09.png'), pygame.image.load('GameImages/L10.png'), pygame.image.load('GameImages/L11.png')]
AL = [pygame.image.load('GameImages/AL00.png'), pygame.image.load('GameImages/AL01.png'), pygame.image.load('GameImages/AL02.png'), pygame.image.load('GameImages/AL03.png'), pygame.image.load('GameImages/AL04.png'), pygame.image.load('GameImages/AL05.png'), pygame.image.load('GameImages/AL06.png'), pygame.image.load('GameImages/AL07.png'), pygame.image.load('GameImages/AL08.png'), pygame.image.load('GameImages/AL09.png'), pygame.image.load('GameImages/AL10.png'), pygame.image.load('GameImages/AL11.png'), pygame.image.load('GameImages/AL12.png')]
char = pygame.image.load('GameImages/S00.png')

#The clock
clock = pygame.time.Clock()

#The sound variables

#The -1 means it is on a loop if not the song would stop after the first time
music = pygame.mixer.music.load('GameImages/music.mp3')
pygame.mixer.music.play(-1)

#Don't remember
backgroundState = 0

#The score (Displayed top right)
score = 0

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



#Code below makes the enemy
class enemy(object):

    #Imports images
    walkRight = [pygame.image.load('GameImages/E0.png'), pygame.image.load('GameImages/E1.png'), pygame.image.load('GameImages/E2.png'), pygame.image.load('GameImages/E3.png'), pygame.image.load('GameImages/E4.png')]
    walkLeft = [pygame.image.load('GameImages/E0.png'), pygame.image.load('GameImages/E1.png'), pygame.image.load('GameImages/E2.png'), pygame.image.load('GameImages/E3.png'), pygame.image.load('GameImages/E4.png')]

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

    #Code for if the bullet hits the goblin
    def hit(self):
        if self.health > 1:
            self.health -= 1
        #If the goblin has less than one health then it will do the following
        else:
            self.visible = False
            print('Ow my bones')

        
#This is how you put stuff onto the display/window
def redrawGameWindow():
    global backgroundState
    #Speed of frames a second
    backgroundState += 1
    #Calls the anaimatipn sort of
    if backgroundState > 12:
        backgroundState = 0
    win.blit(AL[round(backgroundState)], (0,0))
    text = font.render('Score: ' + str(score), 1, (0,0,0))
    win.blit(text, (365,10))
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


#mainloop
font = pygame.font.SysFont('Times', 30, True)
man = player(200, 410, 64,64)
goblin = enemy(100, 410, 64, 64, 450)
shootLoop = 0
bullets = []
run = True
while run:
    clock.tick(27)
    #If player gets hit then and goblin is visible
    if goblin.visible == True:
        if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                man.hit()
                score -= 1

    #Bullet shooting timeout
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                if goblin.visible == True:
                    goblin.hit()
                    score += 1
                    bullets.pop(bullets.index(bullet))
                else:
                    if bullet.x < 500 and bullet.x > 0:
                        bullet.x += bullet.vel
                    else:
                        bullets.pop(bullets.index(bullet))

        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
                
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        if man.left:
            facing = -1
        else:
            facing = 1
            
        if len(bullets) < 3:
            bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (0,0,0), facing))

        shootLoop = 1

    #Move left
    if keys[pygame.K_LEFT] or keys[pygame.K_a] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    #Move right
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else: #Standing
        man.standing = True
        man.walkCount = 0
    #Jumping
    if not(man.isJump):
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            man.isJump = True
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
            
    redrawGameWindow()

pygame.quit()
