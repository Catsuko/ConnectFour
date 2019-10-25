from .graphics import *
import time

class ZelleGraphicsGameView:

    def __init__(self, delay=0.2):
        self.window = None
        self.delay = delay
        self.circles = []
        self.colors = ["gainsboro", "yellow", "red"]
    
    def print_start(self, player1, player2):
        Text(Point(350, 100), "%s vs %s" %(player1,player2,)).draw(self.cached_window())

    def print_board(self, board):
        window = self.cached_window()
        board_width = len(board[0])
        for y in range(len(board)):
            for x in range(board_width):
                index = x + (y * board_width)
                if(len(self.circles) <= index):
                    self.circles.append(Circle(Point(x * 50 + 200, y * 50 + 175), 8))
                    self.circles[index].draw(window)
                self.circles[index].setFill(self.colors[board[y][x]])

        window.redraw()
        time.sleep(self.delay)

    def print_end(self, board, winner):
        self.print_board(board)
        window = self.cached_window()
        Text(Point(350, 500), "%s won\nPress any key to continue..." % winner).draw(window)
        window.getKey()

    def cached_window(self):
        if self.window is None:
            self.window = GraphWin("Connect Four", 700, 600)
        return self.window
        
