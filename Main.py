import pygame as pyg
import random as random

pyg.init()

screenWindow = pyg.display.set_mode((800, 600))  # setting up the screen size

pyg.display.set_caption("Ballon Shooting")
icon = pyg.image.load('Icon.png')
pyg.display.set_icon(icon)

playerImage = pyg.image.load('player.png')
playerXCoordinate = 370
playerYCoordinate = 530
playerXChanges = 0

enemyImage = pyg.image.load('balloon.png')
enemyXCoordinate = random.randint(0,736)
enemyYCoordinate = 0
enemyXChange = 0.3
enemyYChange = 20

def player(xCoordinate, yCoordinate):
    screenWindow.blit(playerImage, (xCoordinate, yCoordinate))

def enemy(xCoordinate,yCoordinate):
    screenWindow.blit(enemyImage,(xCoordinate,yCoordinate))

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

    enemy(enemyXCoordinate,enemyYCoordinate)
    player(playerXCoordinate, playerYCoordinate)

    pyg.display.update()
