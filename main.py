# Example file showing a circle moving on screen
import pygame
from Apple import Apple
from Ghost import Ghost
from Player import Player



class Game:
    
    # pygame setup
    def __init__(self):
        pass

    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    apple_list: list[Apple] = []
    ghost_list : list[Ghost] = []

    SCORE = 0
    
    radius = 40

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    font = pygame.font.Font('freesansbold.ttf', 28)

    player = Player(screen, radius, 375)

    STATE = 'RUNNING'

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        mouse_down = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True
                
        if STATE == 'RUNNING':
        # fill the screen with a color to wipe away anything from last frame
            screen.fill("dark grey")

            # hide the mouse
            pygame.mouse.set_visible(False)
            
            
            # player movement  
            player.draw()
            player.move(dt)
            

            # spawning ghosts
            
            if len(ghost_list) <= SCORE / 5:
                ghost_list.append(Ghost(pygame, screen, 20, "blue", 2))
                

            for ghost in ghost_list:
                ghost.draw_ghost()
                # ghost.chase(player_pos, 60)
                ghost.move()
                ghost.state = player.check_collisions(ghost)
                if ghost.state:
                    STATE = 'GAME OVER'
            
            # ghost wall boundries 
            for ghost in ghost_list:
                ghost.ghost_boundries()
            
            # spawning apples
            if len(apple_list) < 5:
                apple_list.append(Apple(pygame, screen, screen.get_width(), screen.get_height(), 15))

            for apple in apple_list:
                    apple.draw_apple()
                    apple.state = player.check_collisions(apple)
                    
        
            for apple in apple_list:
                if apple.state:
                    apple_list.remove(apple)
                    SCORE += 1

            

            # display score 

            score_text = font.render(str(SCORE), True, (0, 0, 0))
            score_rect = score_text.get_rect()
            score_rect.center = (screen.get_width() / 2, 28)
            screen.blit(score_text, score_rect)

            # display FPS 
            
            text = font.render("FPS: " + str(int(clock.get_fps())), True, (0, 0, 0))
            textRect = text.get_rect()
            
            textRect.center = (screen.get_width() - textRect.left - textRect.right / 2, 20)
            screen.blit(text, textRect)

            # flip() the display to put your work on screen

            

            # limits FPS to 60
            # dt is delta time in seconds since last frame, used for framerate-
            # independent physics.
            dt = clock.tick(60) / 1000

        if STATE == "GAME OVER":
            pygame.mouse.set_visible(True)
            mouse = pygame.mouse.get_pos()
            color = "black"
            

            if (mouse[0] > screen.get_width() / 2 - 70) and mouse[0] < screen.get_width() / 2 + 70:
                if mouse[1] > screen.get_height() / 2 and mouse[1] < screen.get_height() / 2 + 40:
                    color = "light grey"
                
                    if mouse_down:
                        print("uo?")
                        STATE = 'RUNNING'
                        ghost_list = []
                        apple_list = []
                        SCORE = 0
                        player.pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
                        mouse_down = False
                        

            retry_button = pygame.draw.rect(screen, color, [screen.get_width()/2 - 70,screen.get_height()/2,140,40])

            text = font.render("Continue", True, (0, 0, 0))
            textRect = text.get_rect()
            
            textRect.center = (screen.get_width()/2,screen.get_height()/2 + 20)
            screen.blit(text, textRect)
            
        pygame.display.flip()

    pygame.quit()


