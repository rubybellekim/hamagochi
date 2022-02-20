import pygame, sys
import math
from pygame.locals import *


def draw_game():
    # print the images (rect standard -> top/left)
    # you can enter pure number of location of x,y
    mainWindowSurface.fill(WHITE)
    mainWindowSurface.blit(player, player_position)



#initialization
pygame.init()

#Setting frame per sec
FPS = 30
movement_speed = 2
pygameClock = pygame.time.Clock()
pygame.key.set_repeat(int(1000 / FPS), int(1000 / FPS))


#Set RGB colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

W = 400
H = 500

mainWindowSurface = pygame.display.set_mode((W, H))
pygame.display.set_caption("Test")

#load images
player = pygame.image.load('player.png')
player_position = player.get_rect()
# place the image to the middle
player_position.centerx = W / 2
player_position.centery = H / 2

#change image size
player_original = player
player = pygame.transform.scale(player_original, (40, 102))

#Game loop
while True:
    # update visual elements and redraw them
    draw_game()
    pygame.display.update()

    old_position = player_position

    # handle pending user/system events
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if K_UP == event.key:
                player_position.move_ip(0, -movement_speed)
            elif K_DOWN == event.key:
                player_position.centery += movement_speed
            elif K_RIGHT == event.key:
                player_position.centerx += movement_speed
            elif K_LEFT == event.key:
                player_position.centerx -= movement_speed
            elif K_SPACE == event.key:
                movement_speed = 5
            elif K_z == event.key or K_x == event.key:
                old_size = player.get_rect()
                now_position = player_position
                if K_z == event.key:
                    zoom_step = 5
                else:
                    zoom_step = -5
                player = pygame.transform.scale(player_original, (old_size.w + zoom_step, old_size.h + zoom_step))
                player_position = player.get_rect()
                player_position.centerx = now_position.centerx
                player_position.centery = now_position.centery


        elif event.type == KEYUP:
            if K_SPACE == event.key:
                movement_speed = 2
        elif event.type == MOUSEBUTTONDOWN:
            print(event.pos)
            player_position.centerx = event.pos[0]
            player_position.centery = event.pos[1]
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()

    if old_position == player_position:
        player_position.move_ip(0, -movement_speed)

    if (player_position.centery + (player_position.h / 2)) < 0:
        player_position.y = H

    pygameClock.tick(FPS)