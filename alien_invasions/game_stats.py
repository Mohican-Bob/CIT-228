class GameStats:
    """track statistics for alien invasion"""

    def __init__(self, ai_game):
        """initialize stats"""
        self.settings = ai_game.settings
        self.reset_stats()
        #high score should never be reset
        self.high_score = 0
        

        #start game in an invactive state
        self.game_active = False

    def reset_stats(self):
        """initialize stats that can change dduring the game"""
        self.ships_left= self.settings.ship_limit
        self.score = 0
        self.level = 1
        