import time
from console_game_view import ConsoleGameView

# Pretend we are playing the game to test the view.

board = [[0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0 ,0]]

gameScale = 2
gameView = ConsoleGameView(gameScale)
gameView.print_start("Robot", "Ninja")

boardHeight = len(board)
for i in range(boardHeight):
    board[boardHeight - i - 1][3] = 1 if i % 2 == 0 else 2
    gameView.print_board(board)
    time.sleep(0.2)
gameView.print_end("Robot")