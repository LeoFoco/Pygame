#All the imports
import pygame
import pygame as pg
from Settings import *
from Enemy import *
from Player import *
from Bullet import *
pygame.init()




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
    #pygame.draw.rect(win, Black,(50, 600, 10, 10))
    #p1 = Platform(0, HEIGHT-40, WIDTH, 40)
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

        if bullet.x < 1500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
                
        if bullet.x < 1500 and bullet.x > 0:
            bullet.x += bullet.vel

    keys = pygame.key.get_pressed()
    #Shooting the bullets
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