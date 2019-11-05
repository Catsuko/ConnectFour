from core.strategy import Strategy
from .vertical_guard_strategy import VerticalGuardStrategy
import math

class FullBloomStrategy(Strategy):

    def __init__(self):
        self.desired_row = -1
    
    def place_token(self, token, board):
        board_height = len(board)
        board_width = len(board[0])
        turns_taken = board_height * board_width - sum(x.count(0) for x in board)
        if turns_taken < 2:
            self.clear(board)

        while self.desired_row >= 0:
            desired_row = board[self.desired_row]      
            row_middle = math.floor(board_width / 2)
            columns = sorted(range(board_width), key=lambda x: abs(row_middle - x))
            left_wall = -1
            right_wall = board_width
            for x in columns:
                if x > left_wall and x < right_wall and desired_row[x] == 0:
                    return x
                if desired_row[x] != token:
                    if x <= row_middle:
                        left_wall = x
                    if x >= row_middle:
                        right_wall = x
            self.desired_row = self.desired_row - 1
        return -1

    def clear(self, board):
        self.desired_row = len(board) - 1

def export_strategy():
    return VerticalGuardStrategy(FullBloomStrategy())
    
