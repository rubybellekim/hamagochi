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
