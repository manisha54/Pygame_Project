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
def player(x,y):
    #blit -->draw
    screen.blit(playerImg, (x,y))



#Game loop
running = True

while running:
    #RGB COlOUR TO RGB for background color
    screen.fill((255,153,204))
    playerX +=0.1
    #playerY -=0.1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player(playerX, playerY)

    pygame.display.update()



