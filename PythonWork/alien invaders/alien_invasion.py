# Alien Invaders!!!
## Under Construction

#This project was completed with the help of PYTHON CRASH COURSE
#Hands on project based introduction to programming by ERIC MATTHES

# Import dependencies
import sys
import pygame

# Create an overall class to manage game assets and actions
class AlienInvasion:

    # Initialize the game and create resources
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        # Set background color
        self.bg_color = (230, 230, 230)

    # Start main loop for the game
    def run_game(self):
        while True:
            
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Redraw the screen during each pass through the loop
            self.screen.fill(self.bg_color)

            # Make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':

    # Make a game instance and run a game
    ai = AlienInvasion()
    ai.run_game() 



print('end')