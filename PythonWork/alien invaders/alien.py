# Create alien class

import pygame
from pygame.sprite import Sprite

# Choose an alien to fight.
penguin = 'images/alien1.bmp'
flying_saucer = 'images/alien.bmp'

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    
    def __init__(self, ai_game):
        """Initalize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image and set its sect attribute
        self.image = pygame.image.load(penguin)
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store aliens exact horizontal location
        self.x = float(self.rect.x)
