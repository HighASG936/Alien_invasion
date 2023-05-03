class ButtonsStyle:
    """ """

    def __init__(self, ai_game):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.style={
            'easy': {
              'color': (0, 255, 0),
              'x': 200,
              'y': 500,
              'msg': 'EASY',
              },
             'middle':{
                 'color': (180,180,0),
                 'x': 500,
                 'y':500,
                 'msg': 'MIDDLE',
                 },
             'hard':{
                 'color': (255, 180, 0),
                 'x': 800,
                 'y':500,
                 'msg': 'HARD',
                 },
             'help':{
                 'color': (30, 30, 30),
                 'x': 500,
                 'y':600,
                 'msg': 'HELP',
                 },
            
            } 
    