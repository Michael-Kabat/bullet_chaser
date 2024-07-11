import random

class Apple:
    def __init__(self, width, height) -> None:
        self.pos_x = random.randrange(width)
        self.pos_y = random.randrange(height)
        self.color = "red"
    
    def spawn_apple(self):
        print(f"x = {self.pos_x} y = {self.pos_y}")