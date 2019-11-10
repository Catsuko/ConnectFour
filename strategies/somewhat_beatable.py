from core.strategy import Strategy

class SomewhatBeatable(Strategy):
    blocked = [0] * 7
    priority = [2,3,6,1,4,5,0]

    c = 0


    def place_token(self, token, board):

        #new game
        if board[-1].count(0) > 5 and board[-2].count(0) == 7:
            self.blocked = [0] * 7
            self.fence=0
            self.c=0
            if board[-1][3] != 0 and board[-1][3] != token:
                self.c = 2

        row_to_check = board[4]
        top_row = board[0]
        

        for x in range(len(row_to_check)):
            if row_to_check[x] != 0 and self.blocked[x] == 0:
                self.blocked[x] = 1
                return x

        if self.c<16:
            self.c += 1
            rotation = self.c % 4 + 2
            if top_row[rotation] == 0:
                return rotation


        for x in self.priority:
            if board[0][x] == 0:
                # self.pos = x
                return x

def export_strategy():
    return SomewhatBeatable()
