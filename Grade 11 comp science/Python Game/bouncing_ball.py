# import libraries
import pygame, sys, time, random
from pygame.locals import *

# global variables
width = 800
height = 600
r = 10
# (x, y, dir_x, dir_y)
balls = [[random.randint(r,width - r), random.randint(r,height - r), random.randint(1, 10), random.randint(1,10), pygame.Color(255,0,0)]]


# initialization
pygame.init()
fpsClock = pygame.time.Clock()
windowSurfaceObject = pygame.display.set_mode((width,height))
pygame.display.set_caption ("Bounce - multiples")

# main loop
while True:
    # check for window driven events
    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    # fill the screen with white
    windowSurfaceObject.fill (pygame.Color(255,255,255))

    # move all the balls
    for ball in balls:
        # modify the location
        ball[0] = ball[0] + ball[2]
        ball[1] = ball[1] + ball[3]

        if ball[0] + r > width or ball[0] - r < 0:
            ball[2] = ball[2] * -1
            if (len(balls) < 50):
                balls.append([random.randint(r, width - r), random.randint(r, height - r), random.randint(1, 10),random.randint(1, 10), pygame.Color(random.randint(0, 255), random.randint(0,255), random.randint(0, 255))])
        if ball[1] + r > height or ball[1] - r < 0:
            ball[3] = ball[3] * -1


        # draw the ball
        pygame.draw.circle(windowSurfaceObject, ball[4],(ball[0],ball[1]),r)

    # check for collision
    for i in range (len(balls)):
        for j in range (len(balls)):
            if i != j:
                # don't need to check against itself

                # check for collision by seeing the distance between the two centres
                dx = balls[i][0] - balls[j][0]
                dy = balls[i][1] - balls[j][1]
                distance = ((dx ** 2) + (dy ** 2)) ** .5
                if distance < r * 2:
#                    print ("collision " + str(i) + " : " + str(j))

                    # simple bounce (change both directions)
                    balls[i][2] *= -1
                    balls[i][3] *= -1
#                    balls[j][2] *= -1
#                    balls[j][3] *= -1

    # check for collision detection
    # things to consider
    # - direction of the ball (tangental to the line created between the two balls)
    # - side of collision
    # - speed of the ball

    # update the screen
    pygame.display.update()
    # frames per second
    fpsClock.tick(30)
