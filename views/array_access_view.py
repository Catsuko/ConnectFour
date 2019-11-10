from .graphics import *
import time

class ArrayAccessView:

    def __init__(self, delay=0.05):
        self.window = None
        self.delay = delay
        self.squares = []

    def print_access(self, position, arr):
        window = self.cached_window()
        for y in range(len(arr)):
            for x in range(len(arr[y])):
                i = x + (y * len(arr[y]))
                if len(self.squares) <= i:
                    r = Rectangle(Point(x*50+10, y*50+10), Point(x*50+60,y*50+60))
                    self.squares.append(r)
                    self.squares[i].draw(window)
                chosen_color = "gainsboro"
                if position[1] == y:
                    chosen_color = "red" if position[0] == x else "yellow"
                self.squares[i].setFill(chosen_color)
        window.redraw()
        time.sleep(self.delay)
        
    def cached_window(self):
        if self.window is None:
            self.window = GraphWin("Array Access", 370, 320)
        return self.window
