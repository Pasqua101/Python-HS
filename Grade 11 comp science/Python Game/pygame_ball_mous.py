import pygame, sys, math
from pygame.locals import *

w = 640
h = 480

x = int(w / 2)
y = int(h / 2)

radius = 5  # aka speed

pygame.init()
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('go to mouse')

# pygame.mouse.set_visible(False) # remove the mouse pointer
colour = pygame.Color(255, 0, 0)  # start with red

while True:
    screen.fill(pygame.Color(255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION:
            mouse_x, mouse_y = event.pos
        if event.type == MOUSEBUTTONUP:
            print(event.button)
            if event.button == 1:
                colour = pygame.Color(0, 255, 0)
            elif event.button == 2:
                colour = pygame.Color(0, 0, 255)
            elif event.button == 3:
                colour = pygame.Color(255, 255, 0)
            elif event.button == 4:
                colour = pygame.Color(255, 255, 255)
            else:
                colour = pygame.Color(255, 0, 0)

    # calculate the angle
    dx = mouse_x - x
    dy = mouse_y - y

    # print (dx + "," + dy)
    if (dx ** 2 + dy ** 2) ** 0.5 > radius:

        if dx != 0:
            radian = (math.atan(dy / dx)) - math.pi / 2
        else:
            radian = math.pi / 2

        if dx < 0:
            x += math.sin(radian) * radius * 2
            y -= math.cos(radian) * radius * 2
        else:
            x -= math.sin(radian) * radius * 2
            y += math.cos(radian) * radius * 2

    pygame.draw.circle(screen, colour, (int(x), int(y)), 10)
    pygame.display.update()
    fpsClock.tick(30)