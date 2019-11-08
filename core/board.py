from .errors import TokenPlacementError
import math

class Board:
    
    def __init__(self, width, height, moves=[]):
        self.width = width
        self.height = height
        self.moves = moves

    def place_token(self, column):
        if column < 0 or column >= self.width:
            raise TokenPlacementError("%s is outside the range of columns." % column)
        if self.moves.count(column) >= self.height:
            raise TokenPlacementError("Column %s is full." % column)  
        new_moves = self.moves[:]
        new_moves.append(column)
        return Board(self.width, self.height, new_moves)

    def fresh(self):
        return Board(self.width, self.height, [])

    def is_full(self):
        return len(self.moves) == self.width * self.height

    # TODO: Remove this method once we have refactored it out of connect_four_game
    def to_array(self):
        arr = [[0] * self.width for i in range(self.height)]   
        for i in range(len(self.moves)):
            for y in range(len(arr)-1, -1, -1):
                if arr[y][self.moves[i]] == 0:
                    arr[y][self.moves[i]] = (i % 2) + 1
                    break
        return arr

    def longest_line_length(self):
        grid = self.to_array()
        series = []
        series.extend(grid)
        for x in range(self.width):
            series.append([grid[y][x] for y in range(self.height)])
            series.append([grid[pos[1]][pos[0]] for pos in self.line(x, 0, 1, 1)])
            series.append([grid[pos[1]][pos[0]] for pos in self.line(x, self.height - 1, 1, -1)])
        for y in range(1, self.height):
            series.append([grid[pos[1]][pos[0]] for pos in self.line(0, y, 1, 1)])
            series.append([grid[pos[1]][pos[0]] for pos in self.line(0, self.height - y, 1, -1)])
            
        return max([self.longest_run_length(s) for s in series])

    def line(self, x, y, xDir, yDir):
        line = []
        while 0 <= x < self.width and 0 <= y < self.height:
            line.append((x,y))
            x = x + xDir
            y = y + yDir
        return line
        
    
    def longest_run_length(self, series):
        lines = [[]]
        for i in range(len(series)):
            if i == 0 or series[i] != series[i-1]:
                lines.append([])
            lines[-1].append(series[i])
        return len(sorted(list(filter(lambda n: len(n) == 0 or n[0] > 0, lines)), key=lambda l: -len(l))[0])
            
        
            
            
            
