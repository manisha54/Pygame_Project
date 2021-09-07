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
def player():
    #blit -->draw
    screen.blit(playerImg, (playerX, playerX))



#Game loop
running = True

while running:

    screen.fill((58, 0, 58))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        player()

        pygame.display.update()



