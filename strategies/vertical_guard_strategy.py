from core.strategy import Strategy
from .flood_strategy import FloodStrategy

class VerticalGuardStrategy(Strategy):

    def __init__(self, guarded_strategy):
        self.guarded_strategy = guarded_strategy

    def place_token(self, token, board):
        board_height = len(board)
        for x in range(len(board[0])):
            for y in range(0, board_height - 2):
                if board[y][x] > 0:
                    if all(board[y][x] == t for t in (board[y+1][x], board[y+2][x])):
                        return x
                    break      
        return self.guarded_strategy.place_token(token, board)

# TODO: Exporting is awkward for a decorator.
#       I'd like to have a way of doing this without hard-coding the decorated strategy.
def export_strategy():
    return VerticalGuardStrategy(FloodStrategy())
