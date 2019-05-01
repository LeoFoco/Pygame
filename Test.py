import pygame
pygame.init()

#Displays window
win = pygame.display.set_mode((750, 750))

#Sets the caption
pygame.display.set_caption("Escape room")

ScreenWidth = 500
#Charcter dimesions and speed
x = 50
y = 50
width = 40
height = 60
vel = 25

run = True
while run:
    #The time delay(1000 = 1 second)
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #Moves the Charcter
    keys = pygame.key.get_pressed()
        
    if keys[pygame.K_a] or keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_d] or keys[pygame.K_RIGHT] and x < 500:
        x += vel
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        y += vel

    

    #Makes the charcter
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()
    #Removes the trail
    win.fill((0,0,0))
    
pygame.quit()

