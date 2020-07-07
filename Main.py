import pygame as pyg
import random as random
import math

pyg.init()

screenWindow = pyg.display.set_mode((800, 600))  # setting up the screen size

pyg.display.set_caption("Ballon Shooting")
icon = pyg.image.load('Icon.png')
pyg.display.set_icon(icon)


cannonImage = pyg.image.load('player.png')
cannonXCoordinate = 370
cannonYCoordinate = 530
cannonXChanges = 0

ballonImage = pyg.image.load('balloon.png')
ballonXCoordinate = random.randint(0, 736)
ballonYCoordinate = 450
ballonXChange = 0.3
ballonYChange = 20

bulletImage = pyg.image.load('bullet.png')
bulletXCoordinate = random.randint(0,736)
bulletYCoordinate = 530
bulletXChange = 0
bulletYChange = 1
bullet_state = "ready"

missedBullets = 0
bulletText = pyg.font.Font('freesansbold.ttf', 32)
bulletTextXCoordinate = 20
bulletTextYCoordinate = 20

gameOverText = pyg.font.Font('freesansbold.ttf',64)

def gameOver():
    overText = gameOverText.render("GAME OVER",True,(0,0,0))
    screenWindow.blit(overText,(200,200))

def missedBulletText(xCoordinate, yCoordinate):
    missed = bulletText.render("Bullets: " + str(missedBullets), True, (0, 0, 0))
    screenWindow.blit(missed,(xCoordinate,yCoordinate))

def player(xCoordinate, yCoordinate):
    screenWindow.blit(cannonImage, (xCoordinate, yCoordinate))

def ballon(xCoordinate, yCoordinate):
    screenWindow.blit(ballonImage, (xCoordinate, yCoordinate))

def fireBullet(xCoordinate, yCoordinate):
    global bullet_state
    bullet_state = 'fire'
    screenWindow.blit(bulletImage,(xCoordinate + 16,yCoordinate + 10))

def isCollision(ballonXCoordinate,ballonYCoordinate,bulletXCoordinate,bulletYCoordinate):
    distance = math.sqrt(math.pow(ballonXCoordinate - bulletXCoordinate,2) + math.pow(ballonYCoordinate - bulletYCoordinate,2))
    if distance <= 27:
        return True
    return False

def gameOverCollision(ballXCoordinate,ballYCoordinate,playerXCoordinate,playerYCoordinate):
    distance = math.sqrt(math.pow(ballXCoordinate - playerXCoordinate,2) + math.pow(ballYCoordinate - playerYCoordinate,2))
    if distance <= 50:
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
                cannonXChanges = -0.5
            if event.key == pyg.K_RIGHT:
                cannonXChanges = 0.5
            if event.key == pyg.K_SPACE:
                if bullet_state is 'ready':
                    bulletXCoordinate = cannonXCoordinate
                    fireBullet(bulletXCoordinate, bulletYCoordinate)

        if event.type == pyg.KEYUP:
            if event.key == pyg.K_RIGHT or event.key == pyg.K_LEFT:
                cannonXChanges = 0


    cannonXCoordinate += cannonXChanges
    if cannonXCoordinate <= 0:
        cannonXCoordinate = 0
    elif cannonXCoordinate > 736:
        cannonXCoordinate = 736

    ballonXCoordinate += ballonXChange

    overCollision = gameOverCollision(ballonXCoordinate, ballonYCoordinate, cannonXCoordinate, cannonYCoordinate)
    collision = isCollision(ballonXCoordinate, ballonYCoordinate, bulletXCoordinate, bulletYCoordinate)

    if ballonXCoordinate <= 0:
        ballonXChange = 0.3
        ballonYCoordinate += ballonYChange
    elif ballonXCoordinate > 736:
        ballonXChange = -0.3
        ballonYCoordinate += ballonYChange

    if bulletYCoordinate <= 0:
        missedBullets += 1
        bulletYCoordinate = 530
        bullet_state = 'ready'

    if bullet_state is 'fire':
        fireBullet(bulletXCoordinate, bulletYCoordinate)
        bulletYCoordinate -= bulletYChange

    if overCollision:
        gameOver()
        while True:
            bulletYCoordinate = 530
            bullet_state = 'ready'
            ballonYCoordinate = 1500
            break

    ballon(ballonXCoordinate, ballonYCoordinate)
    player(cannonXCoordinate, cannonYCoordinate)
    missedBulletText(bulletTextXCoordinate, bulletTextYCoordinate)
    pyg.display.update()
