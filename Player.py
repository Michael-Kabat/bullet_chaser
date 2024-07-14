import pygame
from pygame import Vector2 
from pygame import display

class Player:
    def __init__(self, screen, radius, speed) -> None:
        self.screen : display  = screen
        self.pos : Vector2 = Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
        self.color = "dark green"
        self.radius = radius
        self.speed : float|int = speed
    
    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.pos, self.radius)

    def check_collisions(self, other):
        if self.pos.distance_to(other.pos) < self.radius + other.radius:
            return True
        return False
    
    def move(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.pos.y -= self.speed * dt
        if keys[pygame.K_s]:
            self.pos.y += self.speed * dt
        if keys[pygame.K_a]:
            self.pos.x -= self.speed * dt
        if keys[pygame.K_d]:
            self.pos.x += self.speed * dt