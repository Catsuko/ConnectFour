from core.strategy import Strategy

class LeftToRightStrategy(Strategy):

    def place_token(self, token, board):
        top_row = board[0]
        for x in range(len(top_row)):
            if top_row[x] == 0:
                return x
        return -1

def export_strategy():
    return LeftToRightStrategy()
