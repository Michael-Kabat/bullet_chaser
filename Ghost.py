from pygame import *
import random

class Ghost:

    def __init__(self, pygame, screen, radius, color, speed) -> None:
        self.pygame = pygame
        self.screen = screen
        
        self.radius = radius
        self.color = color
        self.speed = speed
        self.state = False
        self.velocity = Vector2(random.randrange(-10, 10), random.randrange(-10, 10))

        self.pos : Vector2 = Vector2(random.randint(0, self.screen.get_width() - self.radius * 2), 
                                     random.randint(0, self.screen.get_height() - self.radius * 2))


    def chase(self, player_pos:Vector2, framerate):
        dx = (self.pos.x - player_pos.x) / framerate
        dy = (self.pos.y - player_pos.y) / framerate
        self.pos -= self.pygame.Vector2(dx, dy).normalize() * self.speed

    def ghost_boundries(self):

        if self.pos.x < self.radius or self.pos.x > self.screen.get_width() - self.radius:
            self.velocity.x *= -1
        if self.pos.y < self.radius or self.pos.y > self.screen.get_height() - self.radius:
            self.velocity.y *= -1


    def move(self):
        self.pos += self.velocity


    def draw_ghost(self):
        self.pygame.draw.circle(self.screen, self.color, self.pos, self.radius)

