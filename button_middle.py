from buttons_style import ButtonsStyle
import pygame.font

class ButtonMiddle:
    """ """
    
    def __init__(self, ai_game):
        """ """
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        
        #Load style settings to easy button
        self.buttons = ButtonsStyle(ai_game)
        self.style = self.buttons.style['middle']
        
        #Set the dimensions and properties of the button.
        self.width, self.height = 200, 50        
        self.button_color = self.style['color']
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        #Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x, self.rect.y = self.style['x'], self.style['y']
        
        #The button message needs to be prepped only once.
        self._prep_msg(self.style['msg'])
    
    def _prep_msg(self, msg):
        """Turn msg into a rendered image ans center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        #Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)        

