import pygame, sys, time, random
from pygame.locals import *
fpsClock = pygame.time.Clock()

#set the stage
w = 800
h = 600
wso = pygame.display.set_mode((w,h))
pygame.display.set_caption("snake")

#colour definitions
colourRed = pygame.Color(255, 51, 0)
colourBlue = pygame.Color(0, 153, 255)
colourGreen = pygame.Color(102, 255, 51)
colourWhite = pygame.Color(255,255,255)
colourBlack = pygame.Color(0,0,0)


colours = (colourRed, colourBlue, colourGreen)
step = 10
x_dir = -1
y_dir = 0

board_w = w/step
board_h = h/step

snake_start_x = board_w / 2
snake_start_y = board_h / 2

snake = [[snake_start_x,snake_start_y],[snake_start_x - 1,snake_start_y],[snake_start_x - 2, snake_start_y]]


count = len(snake)
def drawBox (wso, x, y, s, c):
    pygame.draw.rect(wso, c, (x * s, y * s, s, s))

done = False
wso.fill(colourWhite)

#Code for determining where on the board the fruit will spawn
mouse = (random.randint(1,board_w - 1), random.randint(1,board_h - 1))
print (mouse)
drawBox (wso,mouse[0],mouse[1],step,colourBlack)

for i in range(len(snake)):
    drawBox (wso, snake[i][0],snake[i][1],step,colours[count % len(colours)])

while not done:
    for event in pygame.event.get():
        if (event.type == KEYDOWN):
            if (event.key == K_ESCAPE):
                done = True
            if (event.key == K_UP):
                if y_dir == 0:
                    y_dir = -1
                    x_dir = 0
            if (event.key == K_DOWN):
                if y_dir == 0:
                    y_dir = 1
                    x_dir = 0
            if (event.key == K_RIGHT):
                if x_dir == 0:
                    x_dir = 1
                    y_dir = 0
            if (event.key == K_LEFT):
                if x_dir == 0:
                    x_dir = -1
                    y_dir = 0


    drawBox (wso, snake[0][0],snake[0][1],step,colourWhite)
    new_x = snake[-1][0] + x_dir
    new_y = snake[-1][1] + y_dir
    print (snake,new_x,new_y)
    print ("---")

    #How to get the snake to change colours when it passes through the screen to eat a pellet
    if new_x == mouse[0] and new_y == mouse[1]:
        count += 1
        mouse = (random.randint(1,board_w - 1), random.randint(1,board_h - 1))
        drawBox (wso,mouse[0],mouse[1],step,colourBlack)


    for i in range(len(snake)):
        if snake[i][0] == new_x and snake[i][1] == new_y:
            print ('exit',snake)
            done = True
    if count == len(snake):
        snake.pop(0)
    snake.append([snake[-1][0] + x_dir,snake[-1][1] + y_dir])

    if snake[-1][0] >= board_w -1:
        snake[-1][0] = 1
        count += 1
    elif snake[-1][0] < 1:
        snake[-1][0] = board_w - 2
        count += 1

    if snake[-1][1] >= board_h -1:
        snake[-1][1] = 1
        count += 1
    elif snake[-1][1] < 1:
        snake[-1][1] = board_h - 2
        count += 1

    drawBox (wso, snake[-1][0],snake[-1][1],step,colours[count % len(colours)])


    # window is not drawn until the update command is called
    pygame.display.update()
    fpsClock.tick(30)


for i in range(len(snake)):
    drawBox (wso, snake[i][0],snake[i][1],step,colourWhite)
    pygame.display.update()
    #How fast the snake disapears from the screen when the player loses
    fpsClock.tick(24)

#How long it takes for the program to stop running
time.sleep(.8)
sys.exit(0)