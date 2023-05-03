import pygame.font

class GamePause:
    """ """
    
    def __init__(self, ai_game):
        """ """
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        
        self.pause_str = "PAUSE"
        self.text_color = (200, 200, 200)
        self.bg_color = (76, 40, 130)
        self.font = pygame.font.SysFont(None, 80)        

        self.prep_pause()    
            
    def prep_pause(self):
        """ """        
        self.pause_image = self.font.render(self.pause_str, True, self.text_color,
                                            self.bg_color)
        self.pause_rect = self.pause_image.get_rect()
        self.pause_rect.center = self.screen_rect.center
    
    def draw_pause(self):
        """ """
        self.screen.blit(self.pause_image, self.pause_rect)
        

    
