import pygame

class Button:
    """Create a button, then blit the surface in the while loop"""
    def __init__(self, text, pos, size, img, callback):
        self.x, self.y = pos
        self.text = text
        self.callback = callback
        # self.img = pygame.image.load('./res/background.png')
        # self.rect = pygame.Rect(self.x, self.y, self.img.get_rect().width, self.img.get_rect().height)
        self.rect = pygame.Rect(self.x, self.y, size[0], size[1])
 

    def draw(self, surface):
        # This creates a new object on which you can call the render method.
        myfont = pygame.font.SysFont('Comic Sans MS', 16)
        
        # This creates a new surface with text already drawn onto it. At the end you can just blit the text surface onto your main screen.
        textsurface = myfont.render(self.text, True, (0, 0, 0))
        text_size = textsurface.get_size()
        text_pos = (self.x + (self.rect.width - text_size[0]) / 2, (self.y + (self.rect.height - text_size[1]) / 2))

        # surface.blit(self.img, (self.x, self.y))
        pygame.draw.rect(surface, (0, 255, 0), self.rect)
        surface.blit(textsurface, text_pos)
 

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.callback()


class Label:
    def __init__(self, text, position, fontsize):
        self.text = text
        self.position = position
        self.fontsize = fontsize


    def draw(self, surface):
        # This creates a new object on which you can call the render method.
        myfont = pygame.font.SysFont('Comic Sans MS', self.fontsize)

        # This creates a new surface with text already drawn onto it. At the end you can just blit the text surface onto your main screen.
        textsurface = myfont.render(self.text, True, (0, 0, 0))
        surface.blit(textsurface, self.position)

    def click(self, event):
        # do nothing
        print()


class ProgressBar:
    def __init__(self, position, size, color1, color2, current_value, max_value):
        self.position = position
        self.size = size
        self.color1 = color1
        self.color2 = color2
        self.current_value = current_value
        self.max_value = max_value
        self.rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])

    def draw(self, surface):
        offset = 5
        innerRect = pygame.Rect(self.position[0]+offset,
                                self.position[1]+offset,
                                (self.size[0] - 2*offset) * self.current_value / self.max_value,
                                self.size[1] - 2*offset)
        pygame.draw.rect(surface, self.color1, self.rect)
        pygame.draw.rect(surface, self.color2, innerRect)

    def click(self, event):
        # do nothing
        print()
