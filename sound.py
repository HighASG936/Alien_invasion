import pygame.mixer as pm


class Sound:
    """ """
    
    def __init__(self):
        
        #Paths of each sound and music
        self.backgound_music = 'sounds/background.mp3'
        self.shoot_sound = 'sounds/shoot.mp3'
        self.level_up_sound = 'sounds/level_up.mp3'
        self.button_sound = 'sounds/button.mp3'
        self.ship_hit_sound = 'sounds/ship_hit.mp3'
        self.game_over_sound = 'sounds/game_over.mp3'
        self.pause_sound = 'sounds/pause.mp3'
        
        #Volume of each sounds
        self.shoot_volume = 0.1
        self.level_up_volume = 0.8
        self.button_volume = 0.7
        self.ship_hit_volume = 2.0
        self.game_over_volume = 1.0
        self.pause_volume = 2.0        
        
        #Set up mixer        
        pm.set_num_channels(16)        
        
        #Declare background music
        pm.music.load(self.backgound_music, namehint="mp3")
        
        #Declare each sound FX
        self.shoot_fx = pm.Sound(self.shoot_sound)
        self.level_up_fx = pm.Sound(self.level_up_sound)
        self.button_fx = pm.Sound(self.button_sound)
        self.ship_hit_fx = pm.Sound(self.ship_hit_sound)
        self.game_over_fx = pm.Sound(self.game_over_sound)
        self.pause_sound_fx = pm.Sound(self.pause_sound)
        
    def play_background_song(self):
        """play background song"""
        pm.music.play(loops=20, fade_ms=50)
        
    def stop_background_song(self):
        pm.music.stop()
    
    def pause_background_song(self):
        pm.music.pause()

    def resume_background_song(self):
        """ """
        pm.music.unpause()
        
    def rewind_background_song(self):
        """Resets playback of bakcground music to the beginning"""
        pm.music.rewind()
        
    def play_shooting_sound(self):
        """play sound FX of shoot"""
        pm.Sound.play(self.shoot_fx).set_volume(self.shoot_volume)
    
    def play_level_up_sound(self):
        """play sound FX of level up"""
        pm.Sound.play(self.level_up_fx).set_volume(self.level_up_volume)
    
    def play_button_sound(self):
        """play sound FX of button"""
        pm.Sound.play(self.button_fx).set_volume(self.button_volume)

    def play_ship_hit_sound(self):
       """play ship hit FX sound """
       pm.Sound.play(self.ship_hit_fx).set_volume(self.ship_hit_volume)
       
    def play_game_over(self):
        pm.Sound.play(self.game_over_fx).set_volume(self.game_over_volume)

    def play_pause_sound(self):
        pm.Sound.play(self.pause_sound_fx).set_volume(self.pause_volume)    

    def is_busy(self):
        return pm.get_busy()
        