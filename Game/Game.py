import pygame
pygame.init()

win = pygame.display.set_mode((500,480))

pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('GameImages/S00.png'), pygame.image.load('GameImages/R01.png'), pygame.image.load('GameImages/R02.png'), pygame.image.load('GameImages/R03.png'), pygame.image.load('GameImages/R04.png'), pygame.image.load('GameImages/R05.png'), pygame.image.load('GameImages/R06.png'), pygame.image.load('GameImages/R07.png'), pygame.image.load('GameImages/R08.png'), pygame.image.load('GameImages/R09.png'), pygame.image.load('GameImages/R10.png'), pygame.image.load('GameImages/R11.png')]
walkLeft = [pygame.image.load('GameImages/S00.png'), pygame.image.load('GameImages/L01.png'), pygame.image.load('GameImages/L02.png'), pygame.image.load('GameImages/L03.png'), pygame.image.load('GameImages/L04.png'), pygame.image.load('GameImages/L05.png'), pygame.image.load('GameImages/L06.png'), pygame.image.load('GameImages/L07.png'), pygame.image.load('GameImages/L08.png'), pygame.image.load('GameImages/L09.png'), pygame.image.load('GameImages/L10.png'), pygame.image.load('GameImages/L11.png')]
bg = pygame.image.load('GameImages/bg.jpg')
char = pygame.image.load('GameImages/S00.png')

clock = pygame.time.Clock()

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



    #Charcter movement
    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not (self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        #Hitbox for player  
        #For self.y it changes base, then height 
        #For self.x in changes poistion on the grid you set
        self.hitbox = (self.x +17, self.y + 11, 29, 57)
        #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
#Bullet
class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
    #Bullet style
    def draw(self,win):
        pygame.draw.circle(win,self.color, (self.x,self.y), self.radius)



#Code below makes the enemy
class enemy(object):
    #Loads the images
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

    def draw(self,win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 15:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10)) 
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 1:
            self.health -= 1
        else:
            self.visible = False
        print('Ouch my nads')

        
#This is how you put stuff onto the display/window
def redrawGameWindow():
    win.blit(bg, (0,0))
    text = font.render('Score: ' + str(score), 1, (0,0,0))
    win.blit(text, (390,10))
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
                goblin.hit()
                score += 1
                bullets.pop(bullets.index(bullet))
                
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        if man.left:
            facing = -1
        else:
            facing = 1
            
        if len(bullets) < 5:
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
            man.right = False
            man.left = False
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
