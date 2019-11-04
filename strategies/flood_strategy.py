from core.strategy import Strategy

class FloodStrategy(Strategy):

    def place_token(self, token, board):
        board_height = len(board)
        for y in range(board_height):
            for x in range(len(board[y])):
                if board[(board_height - 1) - y][x] == 0:
                    return x
        return -1

def export_strategy():
    return FloodStrategy()
