# Crap Player has the genius idea of just picking the first unfilled column
class CrapPlayer:

    def __init__(self, name):
        self.name = name

    # Return the index of the column that the player wants to use
    def place_token(self, token, board):
        top_row = board[0]
        for x in range(len(top_row)):
            if top_row[x] == 0:
                return x
        return -1
