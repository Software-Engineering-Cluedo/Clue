import pygame

from src.board import Board

class Game():
    board = Board()
    tile_map = []
    player_map = []


    def __init__(self):
        self.board = Board()
        self.refresh_tile_maps()

        # Test to se if map has been imported
        print(*self.tile_map, sep='\n')
        print()
        print(*self.player_map, sep='\n')

        pygame.init()
        window = pygame.display.set_mode((100,100))
        running = True
        while running:
            for eve in pygame.event.get():
                if eve.type == pygame.QUIT:
                    pygame.quit()
                    running = False
        

    def refresh_tile_maps(self):
        self.tile_map = self.board.tile_map
        self.player_map = self.board.player_map

    """
    First opening the game:
        Menu:
            Choose how many players, which ones are AI
                Opens a new pop-up
            Start
        
        Board:
            
    """