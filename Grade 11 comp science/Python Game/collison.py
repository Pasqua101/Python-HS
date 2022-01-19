import pygame, sys

pygame.init()

x,y = 0,0 #Starting x and y coordinates for rectangle 1
a,b = 450, 450 #Starting coordinates for rectangle 2
s = 50 #Width and height of rectangles
xscreen,yscreen = 800, 600 #Screen dimensions

windowSize = (xscreen,yscreen)
screen = pygame.display.set_mode(windowSize)

directionX, directionY, directionA, directionB = 1,1,2,2 #direction of X and Y
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill((0,0,0))

    rec1 = pygame.draw.rect(screen, (0,255,0), (x, y, s, s))
    rec2 = pygame.draw.rect(screen, (255,0,0), (a, b, s, s))

    x +=5 * directionX
    y +=5 * directionY
    a +=5 * directionA
    b +=5 * directionB

def intersectsX(x1,x2,w1,w2):
    if x1 >= x2 and x1 <= x2 + w2:
        return True
    if (x1 + w1) > x2 and (x1 + w1) <= (x2 + w2):
        return True
    return False
intX = intersectsX(x, a, s, s)

if intX == True:
    directionX *= -1
    directionA *= -1

if x + s > xscren or x < 0:
    directionX *= -1
if y + s > yscreen or y < 0:
    directionA *= -1
if a + s > xscren or a < 0:
    directionA *= -1
if b + s > yscreen or B < 0:
    directionB *= -1
pygame.display.updte()
clock.tick(40)

