import time
from .tracked_grid import TrackedGrid

class TrackedPlayer:

    def __init__(self, player, delay=1):
        self.player = player
        self.delay = delay

    def __str__(self):
        return "%s (Tracked)"  % self.player

    def place_token(self, token, board):
        tracked_board = TrackedGrid(board)
        chosen_column = self.player.place_token(token, tracked_board)

        positions = tracked_board.read_all()
        for pos in positions:
            grid = ''
            for y in range(len(board)):
                for x in range(len(board[y])):
                    grid = grid + ('X' if x == pos[0] and y == pos[1] else '_')
                grid = grid + '\n'
            print('%s\r' % grid)
            time.sleep(self.delay)
        print()

        return chosen_column
                    
