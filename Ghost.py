from pygame import *

class Ghost:

    def __init__(self, pygame, screen, radius, color, speed) -> None:
        self.pygame = pygame
        self.screen = screen
        self.pos : Vector2 = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
        self.radius = radius
        self.color = color
        self.speed = speed
        self.state = False

    def chase(self, player_pos:Vector2, framerate):
        dx = (self.pos.x - player_pos.x) / framerate
        dy = (self.pos.y - player_pos.y) / framerate
        self.pos.x -= dx
        self.pos.y -= dy   
        # new_vector = self.pygame.Vector2(self.pos.x - dx, self.pos.y - dy)
        

    def draw_ghost(self):
        self.pygame.draw.circle(self.screen, self.color, self.pos, self.radius)
    
