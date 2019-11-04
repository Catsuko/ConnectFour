from core.strategy import Strategy

class ProbablyBeatable(Strategy):
    blocked = [0] * 7
    # pos = 3
    priority = [3,4,5,2,1,6,0]

    def place_token(self, token, board):
        row_to_check = board[3]
        top_row = board[0]
        # print(self.blocked)
        # print(row_to_check)
        for x in range(len(row_to_check)):
            # print(row_to_check[x])
            if row_to_check[x] != 0 and self.blocked[x] == 0:
                self.blocked[x] = 1
                return x
        # print(board[0][self.pos])
        
        # if board[0][self.pos] == 0:
        for x in self.priority:
            if board[0][x] == 0:
                # self.pos = x
                return x
            

def export_strategy():
    return ProbablyBeatable()
