# Alien Invaders!!!
## Under Construction

#This project was completed with the help of PYTHON CRASH COURSE
#Hands on project based introduction to programming by ERIC MATTHES

# Import dependencies
import sys
import pygame
from settings import Settings

"""Create an overall class to manage game assets and actions"""
class AlienInvasion:

    """ Initialize the game and create resources"""
    def __init__(self):
        pygame.init()
        #Import screen settings from settings.py module
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        # Set caption    
        pygame.display.set_caption("Alien Invasion")

        

    """Start main loop for the game"""
    def run_game(self):
        while True:
            
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Redraw the screen during each pass through the loop (.fill)
            # Color chosen in settings.py
            self.screen.fill(self.settings.bg_color)

            # Make the most recently drawn screen visible and hide old
            pygame.display.flip()

if __name__ == '__main__':

    # Make a game instance and run a game
    ai = AlienInvasion()
    ai.run_game() 

