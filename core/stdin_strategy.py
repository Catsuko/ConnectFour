from .strategy import Strategy

class StdInStrategy(Strategy):

    def place_token(self, token, board):
        print()        
        key = input("Select a column and press enter (%s-%s)\n" % (1,len(board[0])))
        print()
        return int(key) - 1
