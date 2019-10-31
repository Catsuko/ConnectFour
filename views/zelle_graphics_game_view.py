from .graphics import *
import time

class ZelleGraphicsGameView:

    def __init__(self, delay=0.2):
        self.window = None
        self.top_label = None
        self.bottom_label = None
        self.delay = delay
        self.circles = []
        self.colors = ["gainsboro", "yellow", "red"]
    
    def print_start(self, player1, player2):
        window = self.cached_window()
        self.printToTop("%s vs %s" %(player1,player2,), window)
        self.printToBottom("", window)

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

    def print_result(self, result):
        window = self.cached_window()
        self.printToBottom("%s\nPress any key to continue..." % result, window)
        window.getKey()

    def cached_window(self):
        if self.window is None:
            self.window = GraphWin("Connect Four", 700, 600)
        return self.window

    def printToTop(self, text, window):
        if self.top_label == None:
            self.top_label = Text(Point(350, 100), "")
            self.top_label.draw(window)
        self.top_label.setText(text)
        window.redraw()

    def printToBottom(self, text, window):
        if self.bottom_label == None:
            self.bottom_label = Text(Point(350, 500), "")
            self.bottom_label.draw(window)
        self.bottom_label.setText(text)
        window.redraw()
        
        
        
