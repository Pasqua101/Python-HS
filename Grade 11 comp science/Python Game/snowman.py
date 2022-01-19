import pygame, sys, time, random
from pygame.constants import *
pygame.init()

fpsClock = pygame.time.Clock()

#Creating color for the snowman and for the snow flakes
WHITE = (255, 255, 255)
color_flakes = (176, 252, 255)

#Setting the screen boundaries
w = 800
h = 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Do you want to build a snowman?")

#Music for the snowman
Frozen = 'c:/Doyouwanttobuildasnowman.ogg'
pygame.mixer.music.load(Frozen)
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)


#Creating radius and x and y for the snowman
r = 60
x = int(w / 2)
y = int(h / 2)
s = 50
xscreen, yscreen = 800, 600

directionX, directionY, directionA, directionB = 1,1,2,2 #Direction of x and y

# snow list
flakes = []

for i in range(100):
    flakes.append([random.randint(1, w), random.randint(1, h), random.randint(1, 5)])

# Function for drawing the first part of the snowman
def drawSm(x, y, r):
    # code for drawing first part of the snowman
    pygame.draw.circle(screen, WHITE, (x, y - 125), int(r * 1.05))

    # code for drawing the second part of the snowman
    pygame.draw.circle(screen, WHITE, (x, y), int(r * 1.50))

    # code for drawing the third part of the snowman
    pygame.draw.circle(screen, WHITE, (x, y + 125), int(r * 2))
    BLACK = (0, 0, 0)

    # Code for drawing the eyes
    eyes = int(r/10)
    pygame.draw.circle(screen, BLACK, (x - 25, y - 130), eyes)
    pygame.draw.circle(screen, BLACK, (x + 25, y - 130), eyes)
    ORANGE = (255, 167, 0)

    # code for drawing the nose
    pygame.draw.circle(screen, ORANGE, (x, y - 110), int(r / 10))

    # code for drawing the mouth
    mouth = int(r/10)
    pygame.draw.circle(screen, BLACK, (x - 20, y - 100), mouth)
    pygame.draw.circle(screen, BLACK, (x - 15, y - 90), mouth)
    pygame.draw.circle(screen, BLACK, (x - 5, y - 85), mouth)
    pygame.draw.circle(screen, BLACK, (x + 5, y - 85), mouth)
    pygame.draw.circle(screen, BLACK, (x + 15, y - 90), mouth)
    pygame.draw.circle(screen, BLACK, (x + 20, y - 100), mouth)

    # code for making buttons
    buttons = int(r/8)
    pygame.draw.circle(screen, BLACK, (x, y - 50), buttons)
    pygame.draw.circle(screen, BLACK, (x, y - 20), buttons)
    pygame.draw.circle(screen, BLACK, (x, y + 10), buttons)
    pygame.draw.circle(screen, BLACK, (x, y + 40), buttons)
    pygame.draw.circle(screen, BLACK, (x, y + 70), buttons)
    pygame.draw.circle(screen, BLACK, (x, y + 100), buttons)

    # code for hat
    pygame.draw.rect(screen, BLACK, (x-60, y-185, 120, 25))
    pygame.draw.rect(screen, BLACK, (x-50, y-280, 100, 100))
    RED = (225, 0, 0 )
    pygame.draw.rect(screen, RED, (x-50, y-220, 100, 20))

    #code for snow
    pygame.draw.rect(screen, WHITE, (0, 500, 900, 100))


# Variable for moving snowman
vel = 5

#Creating text for the program
font = pygame.font.Font(pygame.font.get_default_font(), 20)
text = font.render("Do you want to build a snowman?", False, (125, 125, 125))

# looping the program

while True:
    #Filling the screen
    screen.fill(pygame.Color(20, 69, 204))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #Keyborad events
    keys = pygame.key.get_pressed()

    #Movement when a is pressed on keyboard
    if keys[pygame.K_a]:
        x -= vel

    #Movement when d is pressed on keyboard
    if keys[pygame.K_d]:
        x += vel

    #Movement when w is pressed on keyboard
    if keys[pygame.K_w]:
        y -= vel

    #Movement when s is pressed on keyboard
    if keys[pygame.K_s]:
        y += vel

    #To make snowflakes fall
    for i in range(len(flakes)):
        pygame.draw.circle(screen, color_flakes, (flakes[i][0], flakes[i][1]), 2)
        flakes[i][1] += flakes[i][2]
        if (flakes[i][1] > h):
            flakes[i][1] = 0
            flakes[i][0] = random.randint(1, w)

    #Drawing the snowman
    drawSm(x, y, r)
    pygame.display.update()
    #Setting the frame rate
    fpsClock.tick(24)
