import pygame
from Apple import Apple
from Ghost import Ghost
from Player import Player
from Button import Button

STATE = 'MENU'
SCORE = 0

class Game:
    
    # pygame setup
    def __init__(self):
        pass
    
    def reset_game_state(self):
        # ghost_list = []
        # apple_list = []
        # SCORE = 0
        # player.pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        # mouse_down = False
        pass
    
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    apple_list: list[Apple] = []
    ghost_list : list[Ghost] = []

    apple_dict : dict[int, Apple] = dict()
    
    easy_color = "dark red"
    medium_color = "dark red"
    hard_color = "dark red"
    diff_color = "grey"
    
    radius = 35
    difficulty = 200
    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    font = pygame.font.Font('freesansbold.ttf', 28)

    player = Player(screen, radius, 375)
    

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        mouse_down = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True

        screen.fill("dark grey")

        if STATE == "OPTIONS":
            pygame.mouse.set_visible(True)
            mouse = pygame.mouse.get_pos()

            # EASY

            
            easy_button = Button(screen, (screen.get_width() / 2, screen.get_height() / 2 - 50), 140, 40, font, easy_color)
            easy_button.draw("EASY")
            if easy_button.click():
                easy_color = "red"
                if mouse_down:
                    STATE = "RUNNING"
                    ghost_list = []
                    apple_list = []
                    SCORE = 0
                    player.pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
                    mouse_down = False
                    difficulty = 200
            else:
                easy_color = "dark red"
                    

            # MEDIUM
            medium_button = Button(screen, (screen.get_width() / 2, screen.get_height() / 2), 140, 40, font, medium_color)
            medium_button.draw("MEDIUM")
            if medium_button.click():
                medium_color = "red"
                if mouse_down:
                    STATE = "RUNNING"
                    ghost_list = []
                    apple_list = []
                    SCORE = 0
                    player.pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
                    mouse_down = False
                    difficulty = 300
                    
            else:
                medium_color = "dark red"
            # HARD
            hard_button = Button(screen, (screen.get_width() / 2, screen.get_height() / 2 + 50), 140, 40, font, hard_color)
            hard_button.draw("HARD")
            if hard_button.click():
                hard_color = "red"
                if mouse_down:
                    STATE = "RUNNING"
                    ghost_list = []
                    apple_list = []
                    SCORE = 0
                    player.pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
                    mouse_down = False
                    difficulty = 400
            else:
                hard_color = "dark red"

        if STATE == "MENU":
            pygame.mouse.set_visible(True)
            mouse = pygame.mouse.get_pos()
            color = "grey"
            
            if (mouse[0] > screen.get_width() / 2 - 70) and mouse[0] < screen.get_width() / 2 + 70:
                if mouse[1] > screen.get_height() / 2 and mouse[1] < screen.get_height() / 2 + 40:
                    color = "light grey"
                
                    if mouse_down:
                        STATE = 'OPTIONS'                        

            retry_button = pygame.draw.rect(screen, color, [screen.get_width()/2 - 70,screen.get_height()/2,140,40])
            text = font.render("Play", True, (0, 0, 0))
            textRect = text.get_rect()
            
            textRect.center = (screen.get_width()/2,screen.get_height()/2 + 20)
            screen.blit(text, textRect)

        if STATE == 'RUNNING':
        # fill the screen with a color to wipe away anything from last frame
            
            # hide the mouse
            pygame.mouse.set_visible(False)
            
            # player control 

            player.move(dt)

            # spawning ghosts
                            
            for ghost in ghost_list:
                ghost.state = player.check_collisions(ghost)
                ghost.draw_ghost()
                ghost.move(dt)

                # player movement  
                player.draw()

                ghost.ghost_boundries()
                #print(str(ghost.pos) + str(ghost.w) + str(ghost.h) + " Width: " + str(screen.get_width()) + " Height: "+ str(screen.get_height()))

                if ghost.state:
                    STATE = 'GAME OVER'
            

            # spawning apples
            
            if len(apple_list) < 5:
                apple_list.append(Apple(pygame, screen, screen.get_width(), screen.get_height(), 15))

            for apple in apple_list:
                    apple.draw_apple()
                    apple.state = player.check_collisions(apple)
                    if apple.state:
                        apple_list.remove(apple)
                        SCORE += 1
            
        

            # Spawning ghosts 
            
            if len(ghost_list) <= SCORE / 5:
                # TODO make bubble around player so they dont get instantly killed

                ghost_list.append(Ghost(screen, 20, "blue", difficulty))

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

            
            # limits FPS to 60
            # dt is delta time in seconds since last frame, used for framerate-
            # independent physics.
            dt = clock.tick(60) / 1000

        if STATE == "GAME OVER":
            pygame.mouse.set_visible(True)
            mouse = pygame.mouse.get_pos()
            color = "grey"
            

            if (mouse[0] > screen.get_width() / 2 - 70) and mouse[0] < screen.get_width() / 2 + 70:
                if mouse[1] > screen.get_height() / 2 and mouse[1] < screen.get_height() / 2 + 40:
                    color = "light grey"
                
                    if mouse_down:
                        STATE = 'RUNNING'
                        ghost_list = []
                        apple_list = []
                        SCORE = 0
                        player.pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
                        mouse_down = False
                        

            retry_button = pygame.draw.rect(screen, color, [screen.get_width()/2 - 70,screen.get_height()/2,140,40])
            text = font.render("Retry", True, (0, 0, 0))
            textRect = text.get_rect()
            
            textRect.center = (screen.get_width()/2,screen.get_height()/2 + 20)
            screen.blit(text, textRect)

            change_difficulty_button = Button(screen, (screen.get_width() / 2, screen.get_height() / 2 - 25), 140, 40, font, diff_color)
            change_difficulty_button.draw("Difficulty")
            if change_difficulty_button.click():
                diff_color = "light grey"
                if mouse_down:
                    STATE = "OPTIONS"
            else:
                diff_color = "grey"

        # flip() the display to put your work on screen  
        #  
        pygame.display.flip()

    pygame.quit()


