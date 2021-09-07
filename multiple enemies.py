import pygame
import random
import math
# initialize pygame
pygame.init()
# Create the screen
screen = pygame.display.set_mode((800,600))
# Create background
background = pygame.image.load('background.png')
# title and icon
pygame.display.set_caption("SPACE INVADERS")
icon = pygame.image.load('img.png')
pygame.display.set_icon(icon)
# Adding player
playerImg = pygame.image.load('spaceinvader.png')
playerX = 370
playerY = 480
playerX_change = 0
# Adding enemy / multiple enemies
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 5

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    # increase the speed based upon your needs
    enemyX_change.append(1)
    enemyY_change.append(40)

# Adding bullet
bulletImg = pygame.image.load('bullet1.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 5
# Ready state - you can't see bullet on screen
# Fire state - bullet moving currently
bullet_state = "ready"
score = 0

# x and y coordinate passed
def player(x,y):
    #blit --> draw
    screen.blit(playerImg, (x,y))

def enemy(x,y,i):
    #blit --> draw
    screen.blit(enemyImg[i], (x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x+16, y+10))
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY - bulletY,2)))
    if distance < 27:
        return True
    else:
        return False

# Game loop
running = True
while running:
    # RGB COLOR TO RGB for background color
    screen.fill((0, 110, 178))
    # background image makes speed slow--> needs to increase speed
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # Increase to 0.3 if u want to increase the speed
                playerX_change = -2.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 2.5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    # Get the current x coordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    #   Checking for boundaries of spaceship so it doesn't go out of boundary
    playerX += playerX_change
    # Creating boundaries
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    # Enemy movement
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 1
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -1
            enemyY[i] += enemyY_change[i]
        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            # Reset the bullet
            bulletY = 480
            bullet_state = "ready"
            score += 1
            print(score)
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i],i)
    # Bullet movement
    if bulletY <=0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change



    player(playerX, playerY)

    pygame.display.update()
