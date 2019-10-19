import time
from console_game_view import ConsoleGameView

# Pretend we are playing the game to test the view.

board = [[0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0 ,0]]

game_scale = 2
game_view = ConsoleGameView(game_scale)
game_view.print_start("Robot", "Ninja")

board_height = len(board)
for i in range(board_height):
    board[board_height - i - 1][3] = 1 if i % 2 == 0 else 2
    game_view.print_board(board)
    time.sleep(0.2)
game_view.print_end("Robot")
