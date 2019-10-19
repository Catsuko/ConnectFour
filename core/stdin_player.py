class StdInPlayer:

    def __init__(self, name):
        self.name = name

    def place_token(self, token, board):
        print()        
        key = input(self.name + ": Select a column and press enter (%s-%s)\n" % (1,len(board[0])))
        print()
        return int(key) - 1

    def __str__(self):
        return self.name
