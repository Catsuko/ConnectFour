class Player:

    def __init__(self, name, strategy):
        self.name = name
        self.strategy = strategy

    # To define a new strategy, create a new strategy subclass and
    # implement the place token method.
    def place_token(self, token, board):
        return self.strategy.place_token(token, board)

    def __str__(self):
        return self.name + " (" + self.strategy.__class__.__name__ + ")"
