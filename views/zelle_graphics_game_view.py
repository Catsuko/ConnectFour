from .graphics import *
import time

class ZelleGraphicsGameView:

    def __init__(self, delay=0.2):
        self.window = None
        self.delay = delay
        self.circles = []
        self.colors = ["gainsboro", "yellow", "red"]
    
    def print_start(self, player1, player2):
        print()
        print("%s vs %s" %(player1,player2,))
        print()

    def print_board(self, board):

        if self.window is None:
            self.window = GraphWin("Connect Four", 700, 600)
        board_width = len(board[0])
        for y in range(len(board)):
            for x in range(board_width):
                index = x + (y * board_width)
                if(len(self.circles) <= index):
                    self.circles.append(Circle(Point(x * 50 + 100, y * 50 + 100), 8))
                    self.circles[index].draw(self.window)
                self.circles[index].setFill(self.colors[board[y][x]])

        self.window.redraw()
        time.sleep(self.delay)

    def print_end(self, winner):
        print()
        print("%s won!" % winner)
        print()
