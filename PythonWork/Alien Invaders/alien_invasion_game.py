# Alien Invaders!!!
## Under Construction
# Can run and get ship that moves with the screen as its constraints


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
        
        # # If full screen mode is desired can run below code in place of 2line above
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

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
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypress"""
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event): 
        """Respond to keypress"""       
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

