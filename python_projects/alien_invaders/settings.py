# Settings

""" A class to store all setttings for Alien Invasion"""
class Settings:

    """ Initialize game settings"""
    def __init__(self):

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        # bg_color (Red, Green, Blue) Values from 0-255
        self.bg_color = (180,230,230)

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (230, 60, 60)
        self.bullets_allowed = 4