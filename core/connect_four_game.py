class ConnectFourGame:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # TODO: Handle Draw results
    # TODO: Refine the return result into something more useful
    def play(self, player1, player2, view=None):
        turn = 0
        players = [player1, player2]
        board = [[0] * self.width for i in range(self.height)]
        
        # TODO: Replace with !grid.Full()?
        # TODO: Catch errors that occur during a turn and auto lose the player that made the error
        while True:
            current_token = (turn % 2) + 1
            current_player = players[current_token - 1]
            desired_column = current_player.place_token(current_token, board)
            
            if desired_column < 0:
                break

            # TODO: Refactor this into a Grid object?
            #       Would be nice to do grid.place(token, column) and have it sort out the rest
            for y in range(len(board)-1, -1, -1):
                if board[y][desired_column] == 0:
                    board[y][desired_column] = current_token
                    break
            
            # TODO: Add Null Check when a view isn't supplied or removed optional view parameter
            view.print_board(board)

            # TODO: Optimize this garb, maybe better as a responsibility of the grid?
            for y in range(len(board)):
                for x in range(len(board[y])):
                    if self.check_for_four(x, y, board):
                        view.print_end(current_player)
                        return current_player
            
            turn = turn + 1

    # TODO: Clean this up!
    def check_for_four(self, x, y, board):
        token = board[y][x]
        if token > 0:
            if x >= 3 and all(token == t for t in (board[y][x-1], board[y][x-2], board[y][x-3])):
                return True
            if y >= 3 and all(token == t for t in (board[y-1][x], board[y-2][x], board[y-3][x])):
                return True
            if x >=3 and y >= 3 and all(token == t for t in (board[y-1][x-1], board[y-2][x-2], board[y-3][x-3])):
                return True
            if x <= len(board[y]) - 4 and y >= 3 and all(token == t for t in (board[y-1][x+1], board[y-2][x+2], board[y-3][x+3])):
                return True
        return False
            
        
        
