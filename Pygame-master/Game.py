import pygame
pygame.init()

#Displays the screen
win = pygame.display.set_mode((1500, 750), pygame.RESIZABLE)

#Sets the name of the window
pygame.display.set_caption("First Game")

#First row, player wlaking right, second row player walking left, third row background, fourth standing animation which is inc.
walkRight = [pygame.image.load('PlayerRight/R00.png'), pygame.image.load('PlayerRight/R01.png'), pygame.image.load('PlayerRight/R02.png'), pygame.image.load('PlayerRight/R03.png'), pygame.image.load('PlayerRight/R04.png'), pygame.image.load('PlayerRight/R05.png'), pygame.image.load('PlayerRight/R06.png'), pygame.image.load('PlayerRight/R07.png'), pygame.image.load('PlayerRight/R08.png'), pygame.image.load('PlayerRight/R09.png'), pygame.image.load('PlayerRight/R10.png'), pygame.image.load('PlayerRight/R11.png')]
walkLeft = [pygame.image.load('PlayerLeft/L00.png'), pygame.image.load('PlayerLeft/L01.png'), pygame.image.load('PlayerLeft/L02.png'), pygame.image.load('PlayerLeft/L03.png'), pygame.image.load('PlayerLeft/L04.png'), pygame.image.load('PlayerLeft/L05.png'), pygame.image.load('PlayerLeft/L06.png'), pygame.image.load('PlayerLeft/L07.png'), pygame.image.load('PlayerLeft/L08.png'), pygame.image.load('PlayerLeft/L09.png'), pygame.image.load('PlayerLeft/L10.png'), pygame.image.load('PlayerLeft/L11.png')]
AL = [pygame.image.load('Background/AL00.png'), pygame.image.load('Background/AL01.png'), pygame.image.load('Background/AL02.png'), pygame.image.load('Background/AL03.png'), pygame.image.load('Background/AL04.png'), pygame.image.load('Background/AL05.png'), pygame.image.load('Background/AL06.png'), pygame.image.load('Background/AL07.png'), pygame.image.load('Background/AL08.png'), pygame.image.load('Background/AL09.png'), pygame.image.load('Background/AL10.png'), pygame.image.load('Background/AL11.png'), pygame.image.load('Background/AL12.png')]
char = pygame.image.load('Random/S00.png')

#The clock
clock = pygame.time.Clock()

#The music

#The -1 means it is on a loop if not the song would stop after the first time
music = pygame.mixer.music.load('Music/music.mp3')
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
                self.x = 0
                self.y = 675
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


#mainloop
font = pygame.font.SysFont('Times', 30, True)
#Where the charcter spawns and size
man = player(0, 675, 64,64)
goblin = enemy(285, 675, 64, 64, 450)
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

    if shootLoop > 4:
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
