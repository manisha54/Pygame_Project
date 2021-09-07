import pygame

pygame.init()
#create the screen
screen = pygame.display.set_mode((800,600))

#title and icon
pygame.display.set_caption("SPACE INVADERS")
icon = pygame.image.load('img.png')
pygame.display.set_icon(icon)

#Adding player
playerImg = pygame.image.load("spaceinvader.png")
playerX = 370
playerY = 480
playerX_change = 0
def player(x,y):
    #blit -->draw
    screen.blit(playerImg, (x,y))



#Game loop
running = True

while running:
    #RGB COlOUR TO RGB for background color
    screen.fill((255,153,204))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed whether its right or left
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                 # Increase to 0.3 if u want to increase the speed
                playerX_change = -0.1
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    playerX += playerX_change
    #creating boundaries
    if playerX <=0:
        playerX = 0
    elif playerX >=360:
        PlayerX = 736


    player(playerX, playerY)

    pygame.display.update()



