class ConnectFourGame:
    
    def __init__(self, board):
        self.board = board

    # TODO: Refine the return result into something more useful
    def play(self, player1, player2, view):
        turn = 0
        players = [player1, player2]
        board = self.board.fresh()
        board_array = board.to_array()
        view.print_start(player1, player2)    
        # TODO: Catch errors that occur during a turn and auto lose the player that made the error
        while not board.is_full():
            # TODO: Token object? token.other and token.value would be useful methods
            current_token = (turn % 2) + 1
            current_player = players[current_token - 1]
            # TODO: Pass board to player and provide helpful methods instead of 2d array
            desired_column = current_player.place_token(current_token, board.to_array())
            try:
                board = board.place_token(desired_column)
            except Exception:
                winner = players[((turn+1) % 2)]
                view.print_end(board_array, winner)
                return winner
            board_array = board.to_array()
            # TODO: Add print method to board and then we can remove the to_array method.
            view.print_board(board_array)

            # TODO: Move this into Board
            for y in range(len(board_array)):
                for x in range(len(board_array[y])):
                    if self.check_for_four(x, y, board_array):
                        view.print_end(board_array, current_player)
                        return current_player
            
            turn = turn + 1
        view.print_end(board_array, 0)
        return 0

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
