import pygame
from pygame import Vector2
import random

class Ghost:

    def __init__(self, screen, radius, color, speed) -> None:
        
        self.screen = screen
        
        self.radius = radius
        self.color = color
        self.state = False
        self.velocity = Vector2(random.randint(-speed, speed), random.randint(-speed, speed))
        self.pos : Vector2 = pygame.Vector2(random.randint(0, self.screen.get_width()), random.randint(0, self.screen.get_height()))


    # def chase(self, player_pos:Vector2, framerate):
    #     dx = (self.pos.x - player_pos.x) / framerate
    #     dy = (self.pos.y - player_pos.y) / framerate
    #     self.pos -= self.pygame.Vector2(dx, dy).normalize() * self.speed

    def ghost_boundries(self):

        if self.pos.x < self.radius or self.pos.x > self.screen.get_width() - self.radius:
            self.velocity.x *= -1
        if self.pos.y < self.radius or self.pos.y > self.screen.get_height() - self.radius:
            self.velocity.y *= -1


    def move(self, dt):
        if dt == 0:
            return
        self.pos += self.velocity * dt


    def draw_ghost(self):
        pygame.draw.circle(self.screen, self.color, self.pos, self.radius)
        

