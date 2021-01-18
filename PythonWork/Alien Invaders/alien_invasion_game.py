# Alien Invaders!!!
## Under Construction

# This project was completed with the help of PYTHON CRASH COURSE
# Hands on project based introduction to programming by ERIC MATTHES

# Import Python dependencies
import sys
import pygame

# Import modules 
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Create an overall class to manage game assets and actions."""

    def __init__(self):
        """Initialize the game and create resources."""
        pygame.init()
        #Import screen settings from settings.py module
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        # Set caption    
        pygame.display.set_caption("Alien Invasion")

        # Import ship from ship.bmp in images folder
        self.ship = Ship(self)

    def run_game(self):
        """Start main loop for the game."""
        while True:
            # Adding helper methods 
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move the ship to the right
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False


    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        # Color chosen in settings.py
        self.screen.fill(self.settings.bg_color)
        # Ship paramters made in ship.py
        self.ship.blitme()

        # Make the most recently drawn screen visible and hide old
        pygame.display.flip()

if __name__ == '__main__':

    # Make a game instance and run a game
    ai = AlienInvasion()
    ai.run_game() 

