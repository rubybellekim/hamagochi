import pygame, sys
import math
from pygame.locals import *


def star_magic(x, y, w, h):
    #draw a square
    pygame.draw.rect(mainWindowSurface, BLACK, (x, y, w, h))

    #calculate the points
    x1 = x + (w / 4)
    y1 = y
    x2 = x + (w / 4) * 3
    y2 = y
    x3 = x
    y3 = y + (h / 2)
    x4 = (x + w)
    y4 = y + (w / 2)
    x5 = x + (w / 2)
    y5 = (y + h)

    #save the points into tuple
    s1 = (x1, y1)
    s2 = (x2, y2)
    s3 = (x3, y3)
    s4 = (x4, y4)
    s5 = (x5, y5)

    #draw star lines
    pygame.draw.line(mainWindowSurface, GREEN, s1, s5, 5)
    pygame.draw.line(mainWindowSurface, GREEN, s5, s2, 5)
    pygame.draw.line(mainWindowSurface, GREEN, s2, s3, 5)
    pygame.draw.line(mainWindowSurface, GREEN, s3, s4, 5)
    pygame.draw.line(mainWindowSurface, GREEN, s4, s1, 5)

    # pygame.draw.line(mainWindowSurface, GREEN, [x1, y1], [x5, y5], 5)
    # pygame.draw.line(mainWindowSurface, GREEN, [x5, y5], [x2, y2], 5)
    # pygame.draw.line(mainWindowSurface, GREEN, [x2, y2], [x3, y3], 5)
    # pygame.draw.line(mainWindowSurface, GREEN, [x3, y3], [x4, y4], 5)
    # pygame.draw.line(mainWindowSurface, GREEN, [x4, y4], [x1, y1], 5)


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
H = 500

mainWindowSurface = pygame.display.set_mode((W, H))
mainWindowSurface.fill(WHITE)
pygame.display.set_caption("Test")

star_magic(20, 30, 50, 70)
star_magic(10, 100, 30, 30)
star_magic(200, 300, 100, 100)
star_magic(150, 150, 80, 100)
star_magic(400, 250, 100, 50)
star_magic(10, 300, 150, 150)
star_magic(200, 200, 55, 55)
star_magic(300, 10, 150, 150)

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
