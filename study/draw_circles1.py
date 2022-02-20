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

W = 1000
H = 1000

#Set the display with its size fixed 300x300
mainWindowSurface = pygame.display.set_mode((W, H))
mainWindowSurface.fill(WHITE)
pygame.display.set_caption("Test")

# consts

# interval
I = 30
circles_per_line = 10
rows = circles_per_line
# radius
R = (W - (I * (circles_per_line + 1))) / (circles_per_line * 2)


# calculate circle centers
points = []
for r in range(rows):
    points.append([])
    for c in range(circles_per_line):
        x = (c + 1) * I + (c * 2 + 1) * R
        y = (r + 1) * I + (r * 2 + 1) * R
        points[r].append((x, y))

print(points)

# draw

for r in range(rows):
    for c in range(circles_per_line):
        (x, y) = points[r][c]
        # pygame.draw.circle(mainWindowSurface, RED, [x, y], R)
        pygame.draw.arc(mainWindowSurface, RED, [x-R, y-R, R*2, R*2], math.radians(0), math.radians(360))

for r in range(rows):
    for c in range(circles_per_line):
        (x, y) = points[r][c]
        r1 = (r-1)
        c1 = (c+1)
        r2 = r
        c2 = (c+1)
        r3 = (r+1)
        c3 = (c+1)
        r4 = (r+1)
        c4 = c

        if r1 >= 0 and c1 < circles_per_line:
            (x1, y1) = points[r1][c1]
            pygame.draw.line(mainWindowSurface, BLACK, (x, y), (x1, y1))
        if c2 < circles_per_line:
            (x2, y2) = points[r2][c2]
            pygame.draw.line(mainWindowSurface, BLACK, (x, y), (x2, y2))
        if r3 < rows and c3 < circles_per_line:
            (x3, y3) = points[r3][c3]
            pygame.draw.line(mainWindowSurface, BLACK, (x, y), (x3, y3))
        if r4 < rows:
            (x4, y4) = points[r4][c4]
            pygame.draw.line(mainWindowSurface, BLACK, (x, y), (x4, y4))

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
