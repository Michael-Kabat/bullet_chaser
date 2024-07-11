import random

class Apple:
    def __init__(self, pygame, screen, width, height, radius) -> None:
        self.pygame = pygame
        self.screen = screen
        self.pos = pygame.Vector2(random.randrange(width), random.randrange(height))
        self.radius = radius
        self.color = "dark red"
        self.state = True
        
    
    def draw_apple(self):
        self.pygame.draw.circle(self.screen, self.color, self.pos, self.radius)