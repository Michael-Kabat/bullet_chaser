import pygame
from pygame import Vector2 

class Player:
    def __init__(self, screen, radius, ) -> None:
        self.screen = screen
        self.pos : Vector2
        self.velocity : Vector2
        self.color = "dark green"
        self.radius = radius
    
    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.pos, self.radius)