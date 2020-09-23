import pygame


class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        #  Load the ship image and get its rect.

        self.image = pygame.image.load('images/rocket_ship.bmp')
        self.image = pygame.transform.scale(self.image, (50, 50)) #  resizes the ship image
        self.rect = self.image.get_rect()


        #  Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

