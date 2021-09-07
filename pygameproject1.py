#creating our first game window

import pygame

#initialize
pygame.init()

#create the screen
screen = pygame.display.set_mode((600,400))

#Game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
