import pygame

class Button:
    def __init__(self, screen, center, width, height, font, color) -> None:
        self.screen = screen
        self.center : tuple = center
        self.width = width
        self.height = height
        self.color = color
        self.font = font

    def draw(self) -> str:
        pygame.draw.rect(self.screen, self.color, [self.center[0], self.center[1], self.width, self.height])

    def click(self) -> bool:
        mouse = pygame.mouse.get_pos()
        if (mouse[0] < self.center[0] + (self.width / 2)) and (mouse[0] > self.center[0] - (self.width / 2)):
            if (mouse[1] < self.center[1] + (self.height / 2)) and (mouse[1] > self.center[1] - (self.width / 2)):
                return True
