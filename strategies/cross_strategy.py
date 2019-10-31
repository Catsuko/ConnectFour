from core.strategy import Strategy

class CrossStrategy(Strategy):
    blocked = [0] * 1

    def place_token(self, token, board):
        row_to_check = board[3]
        for x in row_to_check:
            if row_to_check[x] != 0 and self.blocked[x] == 0:
                self.blocked[x] = 1
                return x
        return 4

def export_strategy():
    return CrossStrategy()
