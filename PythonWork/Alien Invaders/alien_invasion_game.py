# Alien Invaders!!!
## Under Construction
# Can run and get a shooting ship that moves with the screen as its constraints


# This project was completed with the help of PYTHON CRASH COURSE
# Hands on project based introduction to programming by ERIC MATTHES

# Import Python dependencies
import sys
import pygame

# Import modules 
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Create an overall class to manage game assets and actions."""

    def __init__(self):
        """Initialize the game and create resources."""
        pygame.init()
        #Import screen settings from settings.py module
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        
        # # If full screen mode is desired can run below code 
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        # Set caption   
        pygame.display.set_caption("Alien Invasion")

        # Import ship, bullets and alien attributes
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        
    def run_game(self):
        """Start main loop for the game."""
        while True:
            # Adding helper methods 
            self._check_events()
            self.ship.update()
            self._update_bullets()
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
        """Respond to keypress."""
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event): 
        """Respond to keypress."""       
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create new bullets and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            # .add is similar to .append but specific for pygame
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions
        self.bullets.update()            
        # Get rid of bullets that have dissappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:     
                self.bullets.remove(bullet)
        # Used print statement to verrify bullets were removed    
        #print(len(self.bullets))

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Make an alien
        alien = Alien(self)
        self.aliens.add(alien)

    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        # Color chosen in settings.py
        self.screen.fill(self.settings.bg_color)
        # Ship paramters made in ship.py
        self.ship.blitme()
        # Bullet parameters made in bullet.py
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Alien parameters in alien.py
        self.aliens.draw(self.screen)
        # Make the most recently drawn screen visible and hide old
        pygame.display.flip()

if __name__ == '__main__':

    # Make a game instance and run a game
    ai = AlienInvasion()
    ai.run_game() 

