from core.strategy import Strategy
import math

class MagicPowersStrategy(Strategy):

    def __init__(self):
        self.v_weight = lambda n: 3**n - 1
        self.h_weight = lambda n: 4.1**n - 1
        self.d_weight = lambda n: 3.05**n - 1
        self.p_weight = lambda n: 2.95**n - 1

    def place_token(self, token, board):
        width = len(board[0])
        height = len(board)
        column_priority = [0] * width
        for x in range(width):
            stack = []
            for y in range(height - 1, -1, -1):
                if board[y][x] == 0:
                    v_weight = self.v_weight(self.max_by_v(x,y,board))
                    h_weight = self.h_weight(self.max_by_h(x,y,board))
                    d_weight = self.d_weight(max(self.max_by_d_up(x,y,board), self.max_by_d_down(x,y,board)))
                    p_weight = self.p_weight(max(self.max_by_v(x, y-1, board), self.max_by_h(x, y-1, board), self.max_by_d_up(x, y-1, board), self.max_by_d_down(x, y-1, board)))
                    column_priority[x] = column_priority[x] + h_weight + v_weight + d_weight - p_weight
                    break
                elif y == 0:
                    column_priority[x] = -999
        return self.index_of_max(column_priority)

    def longest_line_from(self, x, y, board, step):
        line = []
        height = len(board)
        width = len(board[0])
        pos = step(x,y)
        while True:
            outside_board = pos[0] < 0 or pos[0] >= width or pos[1] < 0 or pos[1] >= height
            token = 0 if outside_board else board[pos[1]][pos[0]]
            if token == 0 or (len(line) > 0 and line[0] != token):
                break
            line.append(token)
            pos = step(pos[0], pos[1])
        return line

    def longest_line_size(self, x, y, board, a_step, b_step):
        a_line = self.longest_line_from(x, y, board, a_step)
        b_line = self.longest_line_from(x, y, board, b_step)
        a_size = len(a_line)
        b_size = len(b_line)
        matching_lines = a_size > 0 and b_size > 0 and a_line[0] == b_line[0]
        return a_size + b_size if matching_lines else max(a_size, b_size)
        
    def max_by_h(self, x, y, board):
        return self.longest_line_size(x, y, board, lambda sx,sy: (sx-1,sy), lambda sx,sy: (sx+1, sy))

    def max_by_v(self, x, y, board):
        return self.longest_line_size(x, y, board, lambda sx,sy: (sx, sy+1), lambda sx,sy: (sx, sy-1))

    def max_by_d_up(self, x, y, board):
        return self.longest_line_size(x, y, board, lambda sx,sy: (sx-1, sy-1), lambda sx,sy: (sx+1, sy+1))

    def max_by_d_down(self, x, y, board):
        return self.longest_line_size(x, y, board, lambda sx,sy: (sx-1, sy+1), lambda sx,sy: (sx+1, sy-1))
            
    def index_of_max(self, li):
        return sorted(enumerate(li), key=lambda kv: -kv[1])[0][0]

def export_strategy():
    return MagicPowersStrategy()
