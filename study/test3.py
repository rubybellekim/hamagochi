import pygame, sys
import math
from pygame.locals import *

#initialization
pygame.init()

#Setting frame per sec
FPS = 30
pygameClock = pygame.time.Clock()

#Set RGB colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

W = 500
H = 600

#Set the display with its size fixed 300x300
mainWindowSurface = pygame.display.set_mode((W, H))
mainWindowSurface.fill(WHITE)
pygame.display.set_caption("Test")


#starting point
interval = 90
circle_radius = 50.5
circle_diameter = (circle_radius * 2)

sH = (interval + circle_diameter)
sV = (interval + circle_diameter)

corners_W = W - (sH * 2)
corners_H = H - (sV * 3)

limit = (W - sH)

a = 1

while a < limit:

    x1 = a * sH
    y1 = a * sV
    # x2 =

    # x1 = a * sH
    # y1 = a * sV
    # x2 = W - (a * sH)
    # y2 = y1
    # x3 = x2
    # y3 = H - (a * sV)
    # x4 = (a + 1) * sH
    # y4 = y3
    # x5 = x4
    # y5 = (a + 1) * sV

    # pygame.draw.polygon(surface, color, pointlist, width)
    # pygame.draw.line(surface, color, start_point, end_point, width)
    # pygame.draw.lines(surface, color, closed, pointlist, width)
    # pygame.draw.circle(surface, color, center_point, radius, width)
    # pygame.draw.ellipse(surface, color, bounding_rectangle, width)
    # pygame.draw.rect(surface, color, rectangle_tuple, width)
    pygame.draw.arc(mainWindowSurface, BLACK, [50, 50, 100, 100], math.radians(0), math.radians(360))

    a += 1





#Game loop

while True:
    # update visual elements and redraw them
    pygame.display.update()

    # handle pending user/system events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygameClock.tick(FPS)
