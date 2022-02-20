import pygame, sys
from pygame.locals import *

# Initialize program
pygame.init()

# Assign FPS a value
FPS = 30
pygameClock = pygame.time.Clock()

# Setting up color objects
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# BG_COLOR = (255, 0, 255)

# Setup a 300x300 pixel display with caption
mainWindowSurface = pygame.display.set_mode((300, 300))
mainWindowSurface.fill(GREEN)
pygame.display.set_caption("Ruby Example ")

# Creating Lines and Shapes

# pygame.draw.polygon(surface, color, pointlist, width)
# pygame.draw.line(surface, color, start_point, end_point, width)
# pygame.draw.lines(surface, color, closed, pointlist, width)
# pygame.draw.circle(surface, color, center_point, radius, width)
# pygame.draw.ellipse(surface, color, bounding_rectangle, width)
# pygame.draw.rect(surface, color, rectangle_tuple, width)

pygame.draw.line(mainWindowSurface, BLUE, (150, 130), (130, 170), 7)
pygame.draw.line(mainWindowSurface, BLUE, (150, 130), (170, 170))
pygame.draw.line(mainWindowSurface, GREEN, (130, 170), (170, 170))
pygame.draw.circle(mainWindowSurface, BLACK, (100, 65), 30)
pygame.draw.circle(mainWindowSurface, BLACK, (200, 50), 45)
pygame.draw.rect(mainWindowSurface, RED, (100, 200, 100, 50), 2)
pygame.draw.rect(mainWindowSurface, BLACK, (110, 260, 80, 5))

pygame.draw.circle(mainWindowSurface, RED, (190, 110), 10)

r1 = 5
r2 = 10

# Beginning Game Loop
while True:
    # update visual elements and redraw them
    pygame.display.update()

    # handle pending user/system events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            pygame.draw.circle(mainWindowSurface, WHITE, (100, 65), r1)
            pygame.draw.circle(mainWindowSurface, WHITE, (200, 50), r2)
            r1 += 1
            r2 += 1
        elif event.type == KEYUP:
            print("KEYUP")

    # add app logic (check time, calculation, etc.)

    pygameClock.tick(FPS)


