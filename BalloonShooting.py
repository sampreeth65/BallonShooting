"""
Author Name: Sampreeth Amith Kumar
Start date: 05-07-2020
last modified: 07-07-2020
Description: Balloon Shooting game, to shoot the balloon that is moving
             game is completed when the balloon is shot down.
             if bullet misses the balloon, number of bullets used is shown
"""

import pygame as pyg
import random as random
import math


pyg.init()                                                                      # initializing pygame

screenWindow = pyg.display.set_mode((800, 600))                                 # setting up the screen size
screenOpen = True                                                               # screen is open as long as game is quit

"""Adding Icon to window."""
pyg.display.set_caption("Balloon Shooting")
icon = pyg.image.load('Icon.png')
pyg.display.set_icon(icon)

"""Adding image of cannon."""
cannonImage = pyg.image.load('player.png')
cannonXCoordinate = 370                                                         # Initial Coordinate of x
cannonYCoordinate = 530                                                         # Initial Coordinate of y
cannonXChanges = 0                                                              # Cannon movement in x axis

"""Adding balloon image."""
balloonImage = pyg.image.load('balloon.png')
balloonXCoordinate = random.randint(0, 736)
balloonYCoordinate = 0
balloonXChange = 0.3                                                            # Speed of change of balloon in x
balloonYChange = 20                                                             # Change of Y coordinate of balloon

"""Adding bullet image."""
bulletImage = pyg.image.load('bullet.png')
bulletXCoordinate = random.randint(0,736)
bulletYCoordinate = 530
bulletXChange = 0
bulletYChange = 0.45
bullet_state = "ready"

"""Missed bullets values."""
missedBullets = 0
bulletText = pyg.font.Font('freesansbold.ttf', 32)
bulletTextXCoordinate = 20                                                    # placement of bullet used value
bulletTextYCoordinate = 20

gameOverTitle = False
gameOverText = pyg.font.Font('game_over.ttf',128)                             # Adding game over font.

def gameOver():
    """To display Game Over."""
    overText = gameOverText.render("GAME OVER",True,(0,0,0))
    screenWindow.blit(overText,(250,200))

def missedBulletText(xCoordinate, yCoordinate):
    """Missed bullet value is incremented"""
    missed = bulletText.render("Bullets: " + str(missedBullets), True, (0, 0, 0))
    screenWindow.blit(missed,(xCoordinate,yCoordinate))

def player(xCoordinate, yCoordinate):
    """Change player coordinate when player uses arrow key."""
    screenWindow.blit(cannonImage, (xCoordinate, yCoordinate))

def ballon(xCoordinate, yCoordinate):
    """Movement of balloon."""
    screenWindow.blit(balloonImage, (xCoordinate, yCoordinate))

def fireBullet(xCoordinate, yCoordinate):
    """Movement of bullet"""
    global bullet_state
    bullet_state = 'fire'
    screenWindow.blit(bulletImage,(xCoordinate + 16,yCoordinate + 10))

def isCollision(ballonXCoordinate,ballonYCoordinate,bulletXCoordinate,bulletYCoordinate):
    """Check if the balloon and the bullet collids."""
    distance = math.sqrt(math.pow(ballonXCoordinate - bulletXCoordinate,2) + math.pow(ballonYCoordinate - bulletYCoordinate,2))
    if distance <= 27:
        return True
    return False

def gameOverCollision(ballXCoordinate,ballYCoordinate,playerXCoordinate,playerYCoordinate):
    """Check if the cannon and balloon collids."""
    distance = math.sqrt(math.pow(ballXCoordinate - playerXCoordinate,2) + math.pow(ballYCoordinate - playerYCoordinate,2))
    if distance <= 50:
        return True
    return False

while screenOpen:
    """Game play area."""
    screenWindow.fill((255, 255, 255))                                          # Adding white screen to window
    for event in pyg.event.get():
        """Itterating through events that occur in window."""
        if event.type == pyg.QUIT:
            """End game when close button pressed."""
            screenOpen = False

        if event.type == pyg.KEYDOWN:
            """Check if a key is pressed."""
            if event.key == pyg.K_LEFT:
                """If key pressed is left arrow key."""
                cannonXChanges = -0.5                                           # Move cannon to left(decreasing x value)
            if event.key == pyg.K_RIGHT:
                """If key pressed is right arrow key."""
                cannonXChanges = 0.5                                            # Move Cannon to right(increase x value)
            if event.key == pyg.K_SPACE:
                """If key pressed is space bar."""
                if bullet_state is 'ready':
                    """Bullets are fired only when they have moved out of window."""
                    bulletXCoordinate = cannonXCoordinate                       # Point when Cannon fired bullet
                    fireBullet(bulletXCoordinate, bulletYCoordinate)            # Bullet is fired

        if event.type == pyg.KEYUP:
            """When arrow key is released stop movement of cannon."""
            if event.key == pyg.K_RIGHT or event.key == pyg.K_LEFT:
                cannonXChanges = 0

    """Check if Cannon crashes with the balloon or bullet has hit the balloon."""
    overCollision = gameOverCollision(balloonXCoordinate, balloonYCoordinate, cannonXCoordinate, cannonYCoordinate)
    collision = isCollision(balloonXCoordinate, balloonYCoordinate, bulletXCoordinate, bulletYCoordinate)

    cannonXCoordinate += cannonXChanges                                  # cannon distance moved when arrow key pressed

    """Setting up boundary for cannon to stay within the window."""
    if cannonXCoordinate <= 0:
        cannonXCoordinate = 0
    elif cannonXCoordinate > 736:                                        # Cannon is 64 pixels
        cannonXCoordinate = 736


    balloonXCoordinate += balloonXChange                                # Balloon distance moved

    """Balloon Boundaries."""
    if balloonXCoordinate <= 0:
        balloonXChange = 0.3
        balloonYCoordinate += balloonYChange
    elif balloonXCoordinate > 736:
        balloonXChange = -0.3
        balloonYCoordinate += balloonYChange


    if bulletYCoordinate <= 0:
        """Missed bullet"""
        if not gameOverTitle:
            """If game not over and bullet missed, Increase bullet used value."""
            missedBullets += 1
        bulletYCoordinate = 530
        bullet_state = 'ready'

    if bullet_state is 'fire':
        """Movement of bullet when in fire state."""
        fireBullet(bulletXCoordinate, bulletYCoordinate)
        bulletYCoordinate -= bulletYChange



    if collision or overCollision:
        """If collision occurred,end game."""
        while True:
            bullet_state = 'ready'
            bulletYCoordinate = 530                                 # Bullet back to ready state
            balloonYCoordinate = 1500                               # Balloon moved out of boundary
            gameOverTitle = True
            break

    if gameOverTitle:
        """Display game over when game has ended."""
        gameOver()


    ballon(balloonXCoordinate, balloonYCoordinate)                  # Balloon movement.
    player(cannonXCoordinate, cannonYCoordinate)                    # Player movement when key pressed
    missedBulletText(bulletTextXCoordinate, bulletTextYCoordinate)  # Bullet movement when space pressed.
    pyg.display.update()                                            # Update changes on screen
