import sys  # needed to exit system

import pygame  # library that contains useful classes and functions
from setting import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()  # Creates an instance
        self.settings = Settings()  # Creates an instance of setting

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))  # sets the display for the window and returns an
        # object 'surface'

        pygame.display.set_caption("Alien Invasion")  # names the window at the top

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""

        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """Respond to key presses and mouse events."""
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():  # retrieves all the events that are occurring
            if event.type == pygame.QUIT:  # pygame.QUIT is when user clicks the X button
                sys.exit()  # closes the program
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #  Move the ship to the right
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False


    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)  # self.screen is an object which is created in __init__
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':

    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
