from core.strategy import Strategy
from .vertical_guard_strategy import VerticalGuardStrategy
import math

class SmotherStrategy(Strategy):

    def __init__(self):
        self.desired_row = -1
    
    def place_token(self, token, board):
        board_height = len(board)
        board_width = len(board[0])
        row_middle = math.floor(board_width / 2)
        # Sorting determines column priority for desirable moves, start at the middle and work outwards
        columns = sorted(range(board_width), key=lambda x: abs(row_middle - x))
        turns_taken = board_height * board_width - sum(x.count(0) for x in board)
        if turns_taken < 2:
            self.clear(board)
        desired_moves = []

        # This strategy can be beaten pretty easily if it doesn't go first, this move prevents the opponent from making an easy 4.
        if turns_taken == 1 and board[board_height-1][row_middle] == 1:
            return row_middle + 1

        # This strategy revolves around aiming for a particular row and claiming all spots in the row when they become available.
        while self.desired_row >= 0:
            desired_row = board[self.desired_row]
            left_wall = -1
            right_wall = board_width
            desired_moves = []
            for x in columns:
                if x > left_wall and x < right_wall and desired_row[x] == 0:
                    desired_moves.append(x)
                if desired_row[x] != token and desired_row[x] != 0:
                    if x <= row_middle:
                        left_wall = x
                    if x >= row_middle:
                        right_wall = x
            # If the current desired row does not have enough room to connect four then move to the next row.
            if len(desired_moves) == 0 or right_wall - (left_wall + 1) < 4:
                self.desired_row = self.desired_row - 1
            else:
                break
        
        # Desired moves are only selected when the space below the desired move is filled.
        for x in desired_moves:
            if self.desired_row == board_height - 1 or board[self.desired_row + 1][x] != 0:
                return x

        # If we are still waiting for the opponent to fill the spaces below the desired moves
        # just copy the opponents moves to disrupt their plans.
        for y in range(board_height - 1):
            for x in range(board_width):
                if board[y][x] == 0 and board[y+1][x] != token and board[y+1][x] != 0:
                    return x

        # Otherwise just take the first available column starting from the edge and moving in.
        for x in columns[::-1]:
            if board[0][x] == 0:
                return x
        
        return -1

    def clear(self, board):
        self.desired_row = len(board) - 1

def export_strategy():
    return VerticalGuardStrategy(SmotherStrategy())
    
