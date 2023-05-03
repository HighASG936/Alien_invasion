
import platform

class Settings:
    """A class to store all settings for Alien Invasion"""
    
    def __init__(self):
        """Initialize the game's settings"""
        #System On Run
        self.system = platform.system()        
        
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (10, 73, 123)       
        
        #Ship settings                
        self.ship_speed = 3.0
        self.ship_limit = 3
        
        #Bullet settings        
        self.bullet_speed = 15
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 60)
        self.bullets_allowed = 10
            
        #Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 5.0
        
        #How quickly the game speeds up
        self.speedup_scale = 1.1
        
        self.initialize_dynamic_settings()
        
        #Scoring
        self.alien_points = 50
        
        #How quickly the alien point values increase
        self.score_scale = 1.5
        
    def initialize_dynamic_settings(self):
        """Initialize settings that throughout the game."""                
        # fleet_direction os 1 represent right; -1 represents left.
        self.fleet_direction = 1
    
    def increase_speed(self):
        """Increase speed settings and alien points."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        

        
        
        