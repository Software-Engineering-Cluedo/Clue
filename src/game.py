import pygame

class Game():
    def __init__(self):
        pygame.init()
        window = pygame.display.set_mode((100,100))
        running = True
        while running:
            for eve in pygame.event.get():
                if eve.type == pygame.QUIT:
                    pygame.quit()
                    running = False
        
    """
    First opening the game:
        Menu:
            Choose how many players, which ones are AI
                Opens a new pop-up
            Start
        
        Board:
            
    """