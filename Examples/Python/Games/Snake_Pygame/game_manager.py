class GameManager:
    """ Manages general settings and states of the game. """

    def __init__(self, clock):
        self.window_width = 400
        self.window_height = 400
        self.game_speed = 10 
        self.segment_size = 20       

        self.game_running = True
        self.in_main_menu = True
        self.playing_game = False
        self.game_over_screen = False

        self.clock = clock

