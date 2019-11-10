from .tracked_grid import TrackedGrid

class TrackedPlayer:

    def __init__(self, player, view):
        self.player = player
        self.view = view

    def __str__(self):
        return "%s (Tracked)"  % self.player

    def place_token(self, token, board):
        tracked_board = TrackedGrid(board)
        chosen_column = self.player.place_token(token, tracked_board)
        positions = tracked_board.read_all()
        for pos in positions:
            self.view.print_access(pos, board)
        return chosen_column
                    
