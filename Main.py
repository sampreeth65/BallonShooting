import pygame as pyg
import random as random
import math

pyg.init()

screenWindow = pyg.display.set_mode((800, 600))  # setting up the screen size

pyg.display.set_caption("Ballon Shooting")
icon = pyg.image.load('Icon.png')
pyg.display.set_icon(icon)

playerScore = 0
playerImage = pyg.image.load('player.png')
playerXCoordinate = 370
playerYCoordinate = 530
playerXChanges = 0

enemyImage = pyg.image.load('balloon.png')
enemyXCoordinate = random.randint(0,736)
enemyYCoordinate = 0
enemyXChange = 0.3
enemyYChange = 20

# Bullet
bulletImage = pyg.image.load('bullet.png')
bulletXCoordinate = random.randint(0,736)
bulletYCoordinate = 530
bulletXChange = 0
bulletYChange = 0.5
bullet_state = "ready"

def player(xCoordinate, yCoordinate):
    screenWindow.blit(playerImage, (xCoordinate, yCoordinate))

def enemy(xCoordinate,yCoordinate):
    screenWindow.blit(enemyImage,(xCoordinate,yCoordinate))

def fire_bullet(xCoordinate,yCoordinate):
    global bullet_state
    bullet_state = 'fire'
    screenWindow.blit(bulletImage,(xCoordinate + 16,yCoordinate + 10))

def isCollision(enemyXCoordinate,enemyYCoordinate,bulletXCoordinate,bulletYCoordinate):
    distance = math.sqrt(math.pow(enemyXCoordinate - bulletXCoordinate,2) + math.pow(enemyYCoordinate - bulletYCoordinate,2))
    if distance <= 27:
        return True
    return False



screenOpen = True
while screenOpen:
    screenWindow.fill((255, 255, 255))
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            screenOpen = False

        if event.type == pyg.KEYDOWN:
            if event.key == pyg.K_LEFT:
                playerXChanges = -0.5
            if event.key == pyg.K_RIGHT:
                playerXChanges = 0.5
            if event.key == pyg.K_SPACE:
                if bullet_state is 'ready':
                    bulletXCoordinate = playerXCoordinate
                    fire_bullet(bulletXCoordinate,bulletYCoordinate)


        if event.type == pyg.KEYUP:
            if event.key == pyg.K_RIGHT or event.key == pyg.K_LEFT:
                playerXChanges = 0


    playerXCoordinate += playerXChanges
    if playerXCoordinate <= 0:
        playerXCoordinate = 0
    elif playerXCoordinate > 736:
        playerXCoordinate = 736

    enemyXCoordinate += enemyXChange

    if enemyXCoordinate <= 0:
        enemyXChange = 0.3
        enemyYCoordinate += enemyYChange
    elif enemyXCoordinate > 736:
        enemyXChange = -0.3
        enemyYCoordinate += enemyYChange

    if bulletYCoordinate <= 0:
        bulletYCoordinate = 530
        bullet_state = 'ready'

    if bullet_state is 'fire':
        fire_bullet(bulletXCoordinate,bulletYCoordinate)
        bulletYCoordinate -= bulletYChange

    collision = isCollision(enemyXCoordinate,enemyYCoordinate,bulletXCoordinate,bulletYCoordinate)
    if collision:
        bulletYCoordinate = 530
        bullet_state = 'ready'
        playerScore += 1
        # print(playerScore)
        enemyXCoordinate = random.randint(0, 736)
        enemyYCoordinate = 0



    enemy(enemyXCoordinate,enemyYCoordinate)
    player(playerXCoordinate, playerYCoordinate)

    pyg.display.update()
