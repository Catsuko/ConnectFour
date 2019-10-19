class ConnectFourGame:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Determine the winner between player1 & player2
    # Return an array of the players, ordered from winner to loser?
    #
    # View is an optional parameter that allows the game to print\log
    # significant events such as the start, end and board after each turn
    def play(self, player1, player2, view=None):
        raise NotImplementedError("IMPLEMENT ME!")
        
