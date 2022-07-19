import pygame

class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings


        #Load the ship imageand get its rect.
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()
        self.rect_width = 10
        self.rect_height = 20

        #Start each new ship at the bottom of the center screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store decimal valuefor the ship's horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #Movement flag.
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """Update the shipsposition based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed


        # Update rect object from self
        self.rect.x = self.x


    def blitme(self):
        """Draw the ship in its current location"""
        self.screen.blit(self.image, self.rect)
