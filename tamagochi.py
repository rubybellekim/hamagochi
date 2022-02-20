import pygame, sys
import math
from pygame.locals import *
import ui


class Tamagochi:
    def draw_game(self, surface, screenInfo, colors, res):
        # print the images (rect standard -> top/left)
        # you can enter pure number of location of x,y
        surface.fill(colors['WHITE'])
        surface.blit(res['background'], [0, 0])

        btn2Center = (surface.get_width()/2, surface.get_height()-screenInfo['topPadding']*4)
        btn1Center = (btn2Center[0] - 40, btn2Center[1] - 10)
        btn3Center = (btn2Center[0] + 40, btn2Center[1] - 10)

        pygame.draw.ellipse(surface, colors['BLUE'],
                            [screenInfo['leftPadding'], screenInfo['topPadding'],
                            surface.get_width()-screenInfo['leftPadding']*2, surface.get_height()-screenInfo['topPadding']*2])
        pygame.draw.rect(surface, colors['WHITE'], [screenInfo['gameAreaPadding'], screenInfo['gameAreaPadding'],
                                                    screenInfo['gameAreaWidth'], screenInfo['gameAreaHeight']])
        pygame.draw.circle(surface, colors['RED'], btn2Center, 10)
        pygame.draw.circle(surface, colors['RED'], btn1Center, 10)
        pygame.draw.circle(surface, colors['RED'], btn3Center, 10)
        # pygame.draw.rect(surface, colors['GREEN'], [gameAreaPadding + 30, gameAreaPadding + 30, 90, 25])
        # pygame.draw.rect(surface, colors['GREEN'], [gameAreaPadding + 5, gameAreaPadding + 30, 20, 25])
        # pygame.draw.rect(surface, colors['GREEN'], [gameAreaPadding + 125, gameAreaPadding + 30, 20, 25])


    def create_colors(self):
        colors = {}
        colors['BLUE'] = (0, 0, 255)
        colors['RED'] = (255, 0, 0)
        colors['GREEN'] = (0, 255, 0)
        colors['BLACK'] = (0, 0, 0)
        colors['WHITE'] = (255, 255, 255)
        return colors


    def load_resources(self):
        res = {}
        res['background'] = pygame.image.load('./res/background.png')
        # TODO: load other resources
        return res


    def on_btnAction(self):
        print(f"click: ACTION: {self.btnAction.text}")
        # TODO


    def on_btnLeft(self):
        print("click: LEFT")
        # self.btnAction.text = "Bathroom"
        self.progress.current_value -= 5
        # TODO


    def on_btnRight(self):
        print("click: RIGHT")
        # self.btnAction.text = "Bedroom"
        self.progress.current_value += 5
        # TODO


    def start(self):
        #initialization
        pygame.init()
        pygame.font.init() # you have to call this at the start, if you want to use this module.

        #Setting frame per sec
        FPS = 30
        movement_speed = 2
        pygameClock = pygame.time.Clock()
        pygame.key.set_repeat(int(1000 / FPS), int(1000 / FPS))

        #Set RGB colors
        self.colors = self.create_colors()

        self.screenInfo = {}
        W = 300
        H = 300
        self.screenInfo['leftPadding'] = 30
        self.screenInfo['topPadding'] = 10
        self.screenInfo['gameAreaPadding'] = self.screenInfo['leftPadding']*2 + 10
        self.screenInfo['gameAreaWidth'] = W - self.screenInfo['gameAreaPadding']*2
        self.screenInfo['gameAreaHeight'] = H - self.screenInfo['gameAreaPadding']*2

        mainWindowSurface = pygame.display.set_mode((W, H))
        pygame.display.set_caption("Tamagochi")

        #load images
        self.res = self.load_resources()

        # create UI
        self.btnAction = ui.Button("Kitchen", (self.screenInfo['gameAreaPadding'] + ((self.screenInfo['gameAreaWidth'] - 90) / 2),
                                    (self.screenInfo['gameAreaPadding'] + self.screenInfo['gameAreaHeight'] - 10 - 25)), (90, 25), "", self.on_btnAction)

        btnLeft = ui.Button("<", (self.btnAction.rect.x - 20 - 5, self.btnAction.rect.y), (20, 25), "", self.on_btnLeft)
        btnRight = ui.Button(">", (self.btnAction.rect.right + 5, self.btnAction.rect.y), (20, 25), "", self.on_btnRight)
        uiItems = [self.btnAction, btnLeft, btnRight]

        uiItems.append(ui.Label("age: 2", (100, 100), 15))
        uiItems.append(ui.Label("money: $55", (100, 115), 15))
        self.progress = ui.ProgressBar((100, 150), (100, 20), self.colors["BLACK"], self.colors["GREEN"], 50, 100)
        uiItems.append(self.progress)

        #Game loop
        while True:
            # update visual elements and redraw them
            self.draw_game(mainWindowSurface, self.screenInfo, self.colors, self.res)
            for item in uiItems:
                item.draw(mainWindowSurface)
            pygame.display.update()

            # old_position = player_position

            # handle pending user/system events
            for event in pygame.event.get():
                for item in uiItems:
                    item.click(event)

                if event.type == KEYDOWN:
                    print("KEYDOWN")
                    # if K_UP == event.key:
                    #     player_position.move_ip(0, -movement_speed)
                    # elif K_DOWN == event.key:
                    #     player_position.centery += movement_speed
                    # elif K_RIGHT == event.key:
                    #     player_position.centerx += movement_speed
                    # elif K_LEFT == event.key:
                    #     player_position.centerx -= movement_speed
                    # elif K_SPACE == event.key:
                    #     movement_speed = 5
                    # elif K_z == event.key or K_x == event.key:
                    #     old_size = player.get_rect()
                    #     now_position = player_position
                    #     if K_z == event.key:
                    #         zoom_step = 5
                    #     else:
                    #         zoom_step = -5
                    #     player = pygame.transform.scale(player_original, (old_size.w + zoom_step, old_size.h + zoom_step))
                    #     player_position = player.get_rect()
                    #     player_position.centerx = now_position.centerx
                    #     player_position.centery = now_position.centery
                elif event.type == KEYUP:
                    print("KEYUP")
                    # if K_SPACE == event.key:
                    #     movement_speed = 2
                elif event.type == MOUSEBUTTONDOWN:
                    print(event.pos)
                    # player_position.centerx = event.pos[0]
                    # player_position.centery = event.pos[1]
                elif event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            # if old_position == player_position:
            #     player_position.move_ip(0, -movement_speed)

            # if (player_position.centery + (player_position.h / 2)) < 0:
            #     player_position.y = H

            pygameClock.tick(FPS)



game = Tamagochi()
game.start()