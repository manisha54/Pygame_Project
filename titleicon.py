import pygame

pygame.init()
#create the screen
screen = pygame.display.set_mode((800,600))

#title and icon
pygame.display.set_caption("SPACE INVADERS")
icon = pygame.image.load('img.png')
pygame.display.set_icon(icon)





#Game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        screen.fill((58,0,58))
        pygame.display.update()



