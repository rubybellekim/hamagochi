import pygame, sys
import math
from pygame.locals import *
import ui

# 2022/03/06
# Class : Added View
# Question : How to change actionBtn text?
# Todo : Sprite - next class / Main screen(new,continue,setting,exit) / UI

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
        res['background'] = pygame.image.load('./tutoring/hamagochi/res/background.png')
        # TODO: load other resources
        return res


    def on_btnAction(self):
        print(f"click: ACTION: {self.btnAction.text}")
        self.currentView = "settings"
        # TODO


    def on_btnLeft(self):
        # self.btnAction.text = "Bathroom"
        # self.progress.current_value -= 5
        # if self.currentViewIndex >= 2:
        print("click: LEFT")

        if self.currentViewIndex == 0:
            self.currentViewIndex = len(self.switchableViews)
            self.currentViewIndex -= 1
        else:
            self.currentViewIndex -= 1

        self.currentView = self.switchableViews[self.currentViewIndex]
        self.views[self.currentView].element("btn").text = self.switchableViews[self.currentViewIndex]
        # TODO


    def on_btnRight(self):
        print("click: RIGHT")
        # self.btnAction.text = "Bedroom"
        # self.progress.current_value += 5
        self.currentViewIndex += 1
        if self.currentViewIndex >= len(self.switchableViews):
            self.currentViewIndex = 0
        self.currentView = self.switchableViews[self.currentViewIndex]
        self.views[self.currentView].element("btn").text = self.switchableViews[self.currentViewIndex]
        # TODO

    def on_settingsBack(self):
        print("click: SETTINGS: BACK")
        self.currentView = "main"

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
        self.btnAction = ui.Button("main", (((self.screenInfo['gameAreaWidth'] - 90) / 2),
                                   (self.screenInfo['gameAreaHeight'] - 10 - 25)), (90, 25), "", self.on_btnAction)

        btnLeft = ui.Button("<", (self.btnAction.rect.x - 20 - 5, self.btnAction.rect.y), (20, 25), "", self.on_btnLeft)
        btnRight = ui.Button(">", (self.btnAction.rect.right + 5, self.btnAction.rect.y), (20, 25), "", self.on_btnRight)
        self.progress = ui.ProgressBar((30, 80), (100, 20), self.colors["BLACK"], self.colors["GREEN"], 50, 100)
        self.character = ui.Character((100, 100), (20, 20), self.colors["RED"])

        viewRect = (self.screenInfo['gameAreaPadding'], self.screenInfo['gameAreaPadding'], self.screenInfo['gameAreaWidth'], self.screenInfo['gameAreaHeight'])
        self.views = {"main": ui.View(viewRect),
                      "settings": ui.View(viewRect),
                      "kitchen": ui.View(viewRect),
                      "bank": ui.View(viewRect),
                      "restaurant": ui.View(viewRect)}
        self.currentView = "main"
        self.switchableViews = ["main", "kitchen", "bank", "restaurant"]
        self.currentViewIndex = 0

        # self.currentViewIndex = 0
        # switchableViews[currentViewIndex]
        # self.currentViewIndex += 1 // -= 1
        # if currentViewIndex >= len(switchableViews) ---> currentViewIndex=0
        # if currentViewIndex < 0 ---> currentViewIndex = len(switchableViews) - 1

        # characterItem = ui.Label("CHAR", (0, 40), 15)

        self.views["main"].addElement("btn", self.btnAction)
        self.views["main"].addElement("leftBtn", btnLeft)
        self.views["main"].addElement("rightBtn", btnRight)
        self.views["main"].addElement("character", self.character)
        self.views["main"].addElement("ageLabel", ui.Label("age: 2", (30, 30), 15))
        self.views["main"].addElement("moneyLabel", ui.Label("money: $55", (30, 45), 15))
        self.views["main"].addElement("progress", self.progress)
        # self.views["main"].addElement("char", characterItem)
        self.views["main"].addElement("testLabel1", ui.Label("TEST", (0, 0), 18))
        # self.views["main"].element("testLabel").text = "OK"

        self.views["settings"].addElement("settingLabel", ui.Label("Settings", (40, 30), 18))
        self.views["settings"].addElement("backBtn", ui.Button("back", (80, 130), (50, 25), "", self.on_settingsBack))
        # self.views["settings"].addElement("char", characterItem)

        self.views["kitchen"].addElement("btn", self.btnAction)
        self.views["kitchen"].addElement("leftBtn", btnLeft)
        self.views["kitchen"].addElement("rightBtn", btnRight)
        self.views["kitchen"].addElement("testLabel2", ui.Label("kitchen", (0, 0), 18))

        self.views["bank"].addElement("btn", self.btnAction)
        self.views["bank"].addElement("leftBtn", btnLeft)
        self.views["bank"].addElement("rightBtn", btnRight)
        self.views["bank"].addElement("testLabel3", ui.Label("bank", (0, 0), 18))

        self.views["restaurant"].addElement("btn", self.btnAction)
        self.views["restaurant"].addElement("leftBtn", btnLeft)
        self.views["restaurant"].addElement("rightBtn", btnRight)
        self.views["restaurant"].addElement("testLabel4", ui.Label("restaurant", (0, 0), 18))
        

        # self.views["main"].element("char").text = "666"
        # self.views["settings"].element("char").text = "777"

        #Game loop
        while True:
            # update visual elements and redraw them
            self.draw_game(mainWindowSurface, self.screenInfo, self.colors, self.res)
            # draw all elements from current view

            # draw elem 1 (btnLeft.draw())
            # draw elem 2 (btnRight.draw())
            # draw elem 3 (label.draw())
            # ...
            # draw elem N (progress.draw())
            self.views[self.currentView].draw(mainWindowSurface)
            pygame.display.update()

            # old_position = player_position

            # handle pending user/system events
            for event in pygame.event.get():
                # handle events for UI items
                self.views[self.currentView].click(event)

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