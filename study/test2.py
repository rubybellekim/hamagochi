import pygame, sys
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


W = 1000
H = 1000

#Set the display with its size fixed 300x300
mainWindowSurface = pygame.display.set_mode((W, H))
mainWindowSurface.fill(WHITE)
pygame.display.set_caption("Test")

#Creating shapes
# pygame.draw.line(mainWindowSurface, BLACK, (5, 5), (295, 5))
# pygame.draw.line(mainWindowSurface, BLACK, (295, 5), (295, 295))
# pygame.draw.line(mainWindowSurface, BLACK, (295, 295), (10, 295))
# pygame.draw.line(mainWindowSurface, BLACK, (10, 295), (10, 10))
# pygame.draw.line(mainWindowSurface, BLACK, (10, 10), (295, 15))
# pygame.draw.line(mainWindowSurface, BLACK, (295, 5), (295, 5))

# x1 = a * sH
# y1 = a * sV
# x2 = W - (1 * sH)
# y2 = y
# x3 = x2
# y3 = H = (1 * sV)
# x4 = 2 * sH
# y4 = y3


#starting point
sH = 50
sV = 50

v = 35

limit = (W / sH) / 2

a = 1

while a < limit:
    x1 = a * sH
    y1 = a * sV
    x2 = W - (a * sH)
    y2 = y1 + v
    x3 = x2
    y3 = H - (a * sV) + v
    x4 = (a + 1) * sH
    y4 = y3 - v
    x5 = x4
    y5 = (a + 1) * sV

    pygame.draw.line(mainWindowSurface, BLACK, (x1, y1), (x2, y2)) #A
    pygame.draw.line(mainWindowSurface, BLACK, (x2, y2), (x3, y3))
    pygame.draw.line(mainWindowSurface, BLACK, (x3, y3), (x4, y4))
    pygame.draw.line(mainWindowSurface, BLACK, (x4, y4), (x5, y5))
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
