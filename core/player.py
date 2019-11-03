class Player:

    def __init__(self, name, strategy):
        self.name = name
        self.strategy = strategy

    def place_token(self, token, board):
        return self.strategy.place_token(token, board)

    def __str__(self):
        return "%s (%s)" % (self.name, self.strategy)
