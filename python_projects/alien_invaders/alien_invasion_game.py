# Alien Invaders!!!

# CLick start to start. SPACE to shoot and  arrows to move left and right
# Lives left displayed at top left corner
# q, esc, or (x) in corner to quit game
# Levels increase in both difficulity and point value as game continues

# This project was completed with the help of PYTHON CRASH COURSE
# Hands on project based introduction to programming by ERIC MATTHES

# Import Python dependencies
import sys
from time import sleep
import pygame

# Import modules 
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button

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

        # Create an instance to store game statistics
        #   and create scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        # Import ship, bullets and alien attributes
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Make the Play button
        self.play_button = Button(self, "Play")

        
    def run_game(self):
        """Start main loop for the game."""
        while True:
            # Adding helper methods 
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)


    def _check_play_button(self, mouse_pos):
        """Start a new game when the payer clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        # To disactivate invisable play button when game active
        if button_clicked and not self.stats.game_active:
            # Reset the settings and statistics
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            # Get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()
            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
            # Hide the mouse while in play
            pygame.mouse.set_visible(False)


    def _check_keydown_events(self, event):
        """Respond to keypress."""
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        #elif event.key == pygame.K_p:
        #    start_game()

        ## Woring on makinf 'f' button fullscreen mode
        ## Refrence to fullscreen needed prior?...
        # elif event.key == pygame.K_f:
        #     self.fullscreen = False
        #     if fullscreen == False:
        #         print("Changing to FULLSCREEN")
        #         screen_backup = screen.copy()
        #         screen = pygame.display.set_mode(
        #         SCREENRECT.size, winstyle | pygame.FULLSCREEN, bestdepth
        #         )
        #         screen.blit(screen_backup, (0, 0))
        #     else:
        #         print("Changing to windowed mode")
        #         screen_backup = screen.copy()
        #         screen = pygame.display.set_mode(
        #             SCREENRECT.size, winstyle, bestdepth)
        #         screen.blit(screen_backup, (0, 0))
        #     pygame.display.flip()
        #     fullscreen = not fullscreen


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

        # Check for any bullets that have hit aliens
        self._check_bullet_alien_collisions()


    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""    
        # Remove andy bullets and alien collisions
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Increase level
            self.stats.level += 1
            self.sb.prep_level()


    def _update_aliens(self):
        """
        Check if the fleet is at an edge,
            then update the positions of all aliens in the fleet.
        """
        self._check_fleet_edges()
        self.aliens.update()

        # Look for  alien-ship collision
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens that hit the bottom of the screen
        self._check_aliens_bottom()


    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat it the sameas if the shit itself was hit
                self._ship_hit()
                break


    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            #Decrement ship_left and update scoreboard
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Pause to allower player to adjust
            sleep(1.0)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)


    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Crete an alien and find the number of aliens in a row
        # Spacing between each alien is equal to one alien width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        # Determine the number of rows that can fit on the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - 
                            (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Creae the full fleet of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)


    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

        # # To make just one alien for first test
        # alien = Alien(self)
        # self.aliens.add(alien)


    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break


    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleets direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


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
        #Draw the score information
        self.sb.show_score()
        # Draw the play button if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()
        # Make the most recently drawn screen visible and hide old
        pygame.display.flip()


if __name__ == '__main__':

    # Make a game instance and run a game
    ai = AlienInvasion()
    ai.run_game() 

