# Settings

""" A class to store all setttings for Alien Invasion"""
class Settings:

    """ Initialize game settings and stastics settings"""
    def __init__(self):

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        # bg_color (Red, Green, Blue) Values from 0-255
        self.bg_color = (180,230,230)
        #self.fullscreen = False

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (230, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        
        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.2
        self.bullet_speed = 1.8
        self.alien_speed = 0.5

        # Fleet_direction of 1 reresents 1 right; -1 represents 1 left
        self.fleet_direction = 1
    
        # Scoring
        self.alien_points = 50

    def increase_speed (self):
        """Increase speed setings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale