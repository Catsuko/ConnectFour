class RegisteredPlayer:

    def __init__(self, strategies):
        self.strategies = strategies
        self.strategy_index = None
        self.name = None

    def place_token(self, token, board):
        return self.selected_strategy().place_token(token, board)

    def selected_strategy(self):
        if self.strategy_index is None:
            print()
            print("Which strategy would you like to use?")
            i = 0
            for strategy in self.strategies:
                i += 1
                print("%d: %s" % (i, strategy))
            self.strategy_index = int(input()) - 1
            print()
        return self.strategies[self.strategy_index]

    def selected_name(self):
        if self.name is None:
            print("What is your name?")
            self.name = str(input())
            print()
        return self.name
    
    def __str__(self):
        return "%s (%s)" % (self.selected_name(), self.selected_strategy())

    
