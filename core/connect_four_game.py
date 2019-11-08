from .score import Score

class ConnectFourGame:
    
    def __init__(self, board, win_threshold=4):
        self.board = board
        self.win_threshold = win_threshold

    def play(self, player1, player2, view):
        turn = 0
        players = [player1, player2]
        board = self.board.fresh()
        view.print_start(player1, player2)
        view.print_board(board.to_array())
        while not board.is_full():
            # TODO: Token object? token.other and token.value would be useful methods
            current_token = (turn % 2) + 1
            current_player = players[current_token - 1]
            desired_column = current_player.place_token(current_token, board.to_array())
            try:
                board = board.place_token(desired_column)
                board_array = board.to_array()
                view.print_board(board_array)
                turn = turn + 1
            except Exception as error:
                winner = players[((turn+1) % 2)]
                view.print_result("%s won! %s caused a %s" % (winner, current_player, error.__class__.__name__))
                return (winner, Score(1, 0, 0))
            if board.longest_line_length() >= self.win_threshold:
                view.print_result("%s got %s!" % (current_player, self.win_threshold))
                return (current_player, Score(1, 0, 0))       
        view.print_result("Nobody won!")
        return (None, Score(0, 1, 0))
