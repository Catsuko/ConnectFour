from core.strategy import Strategy

class DefsBeatable(Strategy):
    blocked = [0] * 7
    priority = [4,3,0,5,2,1,6]
    middle_taken = 0

    c = 1

    def place_token(self, token, board):

        self.check_new_game(token, board)

        if self.middle_taken==1:
            self.middle_taken = 2
            print(self.middle_taken)
            return 3
        elif self.middle_taken==2:
            self.middle_taken = 3
            print(self.middle_taken)
            return 5
        elif self.middle_taken == 3:
            self.middle_taken = 0
            print(self.middle_taken)
            return 1
        
        row_to_check = board[4]
        top_row = board[0]
        
        #block
        for x in range(len(row_to_check)):
            if row_to_check[x] != 0 and self.blocked[x] == 0:
                self.blocked[x] = 1
                return x

        if self.c<16:
            self.c += 1
            rotation = self.c % 4 + 1
            if top_row[rotation] == 0:
                return rotation

        for x in self.priority:
            if board[0][x] == 0:
                return x

    def check_new_game(self, token, board):
        if board[-1].count(0) > 5 and board[-2].count(0) == 7:
            self.blocked = [0] * 7
            self.c=1
            if board[-1][3] != 0 and board[-1][3] != token:
                self.c += 1
                self.middle_taken = 1



def export_strategy():
    return DefsBeatable()
