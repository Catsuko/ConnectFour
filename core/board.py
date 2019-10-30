from .errors import TokenPlacementError

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
