from core.strategy import Strategy

class SomewhatBeatable(Strategy):
    blocked = [0] * 7
    # pos = 3
    priority = [1,6,3,4,2,5,0]
    # fence = 0

    c = 0


    def place_token(self, token, board):

        #new game
        if board[-1].count(0) > 5 and board[-2].count(0) == 7:
            self.blocked = [0] * 7
            self.fence=0
            self.c=0
            if board[-1][3] != 0 and board[-1][3] != token:
                self.c = 2
                # return 2

        # if self.fence != 0:
        #     self.fence = 0
        #     return 5

        row_to_check = board[3]
        top_row = board[0]

        for x in range(len(row_to_check)):
            # print(row_to_check[x])
            if row_to_check[x] != 0 and self.blocked[x] == 0:
                self.blocked[x] = 1
                return x

        if self.c<16:
            self.c += 1
            rotation = self.c % 4 + 2
            if top_row[rotation] == 0:
                return rotation
            # if self.place < 5:
            #     self.place += 1
            # else:
            #     self.place 2
            # return self.place
        

        # print(self.blocked)
        # print(row_to_check)
        
        # print(board[0][self.pos])
        
        # if board[0][self.pos] == 0:
        for x in self.priority:
            if board[0][x] == 0:
                # self.pos = x
                return x

    # def new_game(board):
    #     if board[-1].count(0) > 5:
    #         self.blocked = [0] * 7

    def can_i_win(token):
        column = 0
        for row in board:
            if row[column] == 0:
                i = 0
                vertical = [0,0,0]
                while column+i+1<6 and row[column+i+1] == token:
                    vertical[i] = 1
                    i = i+1
                    if i > 3:
                        return column


    def is_there_threat():
        return 0
            

def export_strategy():
    return SomewhatBeatable()
