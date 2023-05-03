import pygame.font

class GameOver:
    """ """
    
    def __init__(self, ai_game):
        """ """
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        
        self.game_over_str = "GAME OVER"
        self.text_color = (200, 200, 200)
        self.bg_color = (225, 50, 50)
        self.font = pygame.font.SysFont(None, 80)        

        self.prep_game_over()    
            
    def prep_game_over(self):
        """ """        
        self.game_over_image = self.font.render(self.game_over_str, True, self.text_color,
                                            self.bg_color)
        self.game_over_rect = self.game_over_image.get_rect()
        self.game_over_rect.center = self.screen_rect.center
    
    def draw_game_over(self):
        """ """
        self.screen.blit(self.game_over_image, self.game_over_rect)
        

    