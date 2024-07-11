# Example file showing a circle moving on screen
import pygame
from Apple import Apple

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

radius = 40
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
font = pygame.font.Font('freesansbold.ttf', 28)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("dark grey")

    pygame.draw.circle(screen, "yellow", player_pos, radius)

    # player movement  
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    
    # spawning apples d
    if pygame.key.get_pressed()[pygame.K_SPACE]:

        Apple.spawn_apple(screen.get_width(), screen.get_height())
    # display FPS 
    text = font.render(str(int(clock.get_fps())), True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (screen.get_width() - 20, 20)
    screen.blit(text, textRect)

    # flip() the display to put your work on screen

    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()


