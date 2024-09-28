import sys
import pygame
class AlienInvasion:
    """Overall class to manage game assets and behaviors."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()


        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        # Set Background color.
        self.bg_color = (230, 230, 230)
        self.screen


    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Watch the keyboard qnd the mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    # Make a gain instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()