# course: ICS3U1-01
# exercise: Pygame culminating assignment
# date: 2019-12-06
# student number: 349612614
# name: Marco Pasqua
# description: This program/game that I made is known as snake. The objective of this game is to eat as much fruit as possible withput hitting the border of the screen or hitting yourself. In this code I will be using functions that will allows the user/player to see their score and make the computer go to a game over and start screen
#
#   ______  ___                               ________
# ___   |/  /_____ ___________________      ___  __ \_____ _____________ ____  _______ _
# __  /|_/ /_  __ `/_  ___/  ___/  __ \     __  /_/ /  __ `/_  ___/  __ `/  / / /  __ `/
# _  /  / / / /_/ /_  /   / /__ / /_/ /     _  ____// /_/ /_(__  )/ /_/ // /_/ // /_/ /
# /_/  /_/  \__,_/ /_/    \___/ \____/      /_/     \__,_/ /____/ \__, / \__,_/ \__,_/
#                                                                   /_/


import pygame, sys, time, random
from pygame.constants import *

pygame.init()
# Initialize the joysticks
pygame.joystick.init()

# Setting the area for the board
screen = w, h = 800, 600
# Setting borders
board = pygame.display.set_mode(screen)
pygame.display.set_caption("Snake, Pygame culminating - Pasqua, Marco")

# colours
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
# Allowing music to be played in the game
game_music = 'Snake_music.ogg'
pygame.mixer.music.load(game_music)
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)

# Variables for the start screen
start_font = pygame.font.Font('PressStart2P-vaV7.ttf', 50)
start_text1 = start_font.render('Snake', True, white)
start_text2 = start_font.render('By: Marco Pasqua', True, white)
start_text3 = start_font.render('Press any key to start playing', True, white)

# Setting variable for fps
fpsClock = pygame.time.Clock()
# Setting for the game
# Snake speed
speed = 10
# Spawn point for the part of the snake that is controlled by the player
snake_Pos = [400, 300]

# Position for the rest of the snake's body
snake_Body = [[390, 300], [380, 300], [370, 300]]

# Spawn point for the first piece of fruit
fruit = [300, 50]

# Variable for spawning fruit
fruit_Spawn = True

# Score variable is being used to count the player's score
score = 0

# Creating a snake_dir variable so this way the computer always know which snake_dirion the snake is moving in and how it starts.
snake_dir = 'RIGHT'

# Creating a variable that will allow the snake_dir variable to change
change_dir = ''

# My attempt at a start screen unfortunately I ran out of time to work on this as I focused more on make a game over function, a score function and making sure that my code properly worked. Originally, I was going to make the start screen through pygame. But I decided that making it through Microsoft Paint would've of been easier to display because then I can make a picture to say press e to start or press t for tutorial/how to play.
""""def Game_Start():
    # Needed six quotes here to properly document my function
    """"""Game_Start() : Will display a start screen that will get the players input by pressing enter to start the game or press t to learn how the game works.""""""
    Start_font = pygame.font.Font('PressStart2P-vaV7.ttf', 50)
    board.fill(black)
    gs_surf1 = Start_font.render('Snake', True, white)
    gs_surf2 = Start_font.render('Press c or q to start the game', True, white)
    # Draws a rectangle that allows the string to be displayed over the game
    gs_rect1 = gs_surf1.get_rect()
    gs_rect2 = gs_surf2.get_rect()
    # Allows the rectangle that is being drawn that displays the word Snake to be moved
    gs_rect1.midtop = (320, 25)
    gs_rect2.midtop = (100, 25)
    board.blit(gs_surf1, gs_rect1)
    board.blit(gs_surf2, gs_rect2)
    pygame.display.update()
    # Using a time.sleep to make it act like the code is loading
    time.sleep(.5)"""


# Function for game over
def Game_Over():
    """ Game_Over() : Will display the text that I put saying game over on top of the screen with the player's score and will stop the program """
    go_font = pygame.font.Font('PressStart2P-vaV7.ttf', 50)
    # Displays the string game over on the screen with the font and size that was defined in the variable go_font
    go_surf = go_font.render("Game over", True, red)
    # Draws a rectangle that allows the string to be displayed over the game
    go_rect = go_surf.get_rect()
    # Allows the rectangle that is being drawn that displays the word Game over to be moved
    go_rect.midtop = (320, 25)
    board.blit(go_surf, go_rect)
    Score(0)
    pygame.display.update()
    time.sleep(3)
    pygame.quit()
    sys.exit(0)


# Function for showing the score
def Score(choice=1):
    """Score(choice=1) : Will display the player's score over the screen and will refresh whenever the player eats a fruit"""
    score_font = pygame.font.Font('PressStart2P-vaV7.ttf', 16)
    # Will use the font that was defined in score_font and the size to show the score on screen
    score_surf = score_font.render("score : {0}".format(score), True, white)
    score_rect = score_surf.get_rect()
    if choice == 1:
        score_rect.midtop = (80, 10)
    else:
        score_rect.midtop = (320, 100)
    board.blit(score_surf, score_rect)


while True:
    for event in pygame.event.get():
        # Keyboard events
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:

            # If user were to press right arrow or d on the keyboard it will make the snake move right
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                change_dir = 'RIGHT'

            # If user were to press left arrow or a on the keyboard it will make the snake move left
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                change_dir = 'LEFT'

            # If user were to press up arrow or w on the keyboard it will make the snake move up
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                change_dir = 'UP'

            # If user were to press down arrow or s on the keyboard it will make the snake move right
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                change_dir = 'DOWN'

            # If user were to press the escape key on the keyboard it will quit the program
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
    # My attempt at getting joysticks to work in my code.
    """"# Getting the number of joysticks
        joystick_count = pygame.joystick.get_count()

        # For each joystick
        for i in range(joystick_count):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()

            snake_Pos[i] += joystick.get_axis(1) * 10
            snake_Pos[i] -= joystick.get_axis(0) * 10"""

    # Validating the snake's direction
    if change_dir == 'RIGHT' and snake_dir != 'LEFT':
        snake_dir = change_dir
    if change_dir == 'LEFT' and snake_dir != 'RIGHT':
        snake_dir = change_dir
    if change_dir == 'UP' and snake_dir != 'DOWN':
        snake_dir = change_dir
    if change_dir == 'DOWN' and snake_dir != 'UP':
        snake_dir = change_dir

    # Updating the snake's position
    if snake_dir == 'RIGHT':
        snake_Pos[0] += speed
    if snake_dir == 'LEFT':
        snake_Pos[0] -= speed
    if snake_dir == 'DOWN':
        snake_Pos[1] += speed
    if snake_dir == 'UP':
        snake_Pos[1] -= speed

    # Snake body mechanics
    snake_Body.insert(0, list(snake_Pos))
    if snake_Pos == fruit:
        fruit_Spawn = False
        score += 1
    else:
        # Allows the snake's body to continue at the same size instead of just becoming a line
        snake_Body.pop()
    if fruit_Spawn == False:
        fruit = [random.randrange(1, w // 10) * speed, random.randrange(1, h // 10) * speed]
        fruit_Spawn = True

    board.fill(black)
    for pos in snake_Body:
        pygame.draw.rect(board, green, pygame.Rect(pos[0], pos[1], speed, speed))
    pygame.draw.rect(board, red, pygame.Rect(fruit[0], fruit[1], speed, speed))

    # Setting Boundaries
    if snake_Pos[0] >= w or snake_Pos[0] < 0:
        Game_Over()
    if snake_Pos[1] >= h or snake_Pos[1] < 0:
        Game_Over()

    # If player were to hit themself
    for hit in snake_Body[1:]:
        if snake_Pos == hit:
            Game_Over()

    # Game_Start()
    Score()
    pygame.display.update()
    fpsClock.tick(24)