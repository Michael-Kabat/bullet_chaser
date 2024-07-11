from pygame import *

class Ghost:

    def __init__(self, pygame, screen, radius, color, speed) -> None:
        self.pygame = pygame
        self.screen = screen
        self.pos : Vector2 = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
        self.radius = radius
        self.color = color
        self.speed = speed

    def chase(self, player_pos:Vector2):
        pass
        
    def draw_ghost(self):
        self.pygame.draw.circle(self.screen, self.color, self.pos, self.radius)