from core.strategy import Strategy

class YouShallNotPass(Strategy):
    def __init__(self):
        super().__init__()
        self.position = 0
        self.NUM_OF_POSITIONS = 3
        self.increments = 1
    
    def _measure_board(self):
        self.board_height = len(self.board)
        self.board_width = len(self.board[0])
    
    def _get_column(self, column_index):
        column = []
        [column.append(row[column_index]) for row in self.board]
        column.reverse()
        return column
    
    def _is_dimension_empty(self, row_or_column):
        return True if sum(row_or_column) == 0 else False
    
    def _is_dimension_full(self, row_or_column, dimension_length):
        occupied_spaces = list(filter(lambda a: a != 0, row_or_column))
        return True if len(occupied_spaces) == dimension_length else False
    
    def _is_row_empty(self, row):
        return self._is_dimension_empty(row)
    
    def _is_row_full(self, row):
        return self._is_dimension_full(row, self.board_width)

    def _is_column_empty(self, column_index):
        return self._is_dimension_empty(self._get_column(column_index))
    
    def _is_column_full(self, column_index):
        return self._is_dimension_full(self._get_column(column_index), self.board_height)
    
    def _is_board_empty(self):
        for row in self.board:
            if not self._is_row_empty(row):
                return False
        return True
    
    def _find_columns_with_vulnerable_3(self, our_token):
        columns = []
        [columns.append({"index":index, "column": self._get_column(index)}) for index in range(0, self.board_width)]
        
        vulnerable_columns = []

        for column in columns:
            amount_stacked = 0
            vulnerable = False
            for space in column["column"]:
                if space != our_token:
                    if space != 0:
                        amount_stacked += 1
                    elif amount_stacked == 3:
                        vulnerable = True
                else:
                    amount_stacked = 0
                
            if vulnerable:
                vulnerable_columns.append(column["index"])
        
        return vulnerable_columns
    
    def _you_shall_not_pass(self):
      column = int(self.position * self.increments)
      self.position += 1
      if self.position >= self.NUM_OF_POSITIONS:
          self.position = 0
      return column

    def place_token(self, token, board):
        self.board = board
        self._measure_board()
        self.increments = self.board_width/self.NUM_OF_POSITIONS
        column = 0
        
        vulnerabilities = self._find_columns_with_vulnerable_3(token)
        if len(vulnerabilities) > 0:
            column = vulnerabilities[0]
        else:
            column = self._you_shall_not_pass()
            while(self._is_column_full(column)):
              column = self._you_shall_not_pass()
        return column

def export_strategy():
    return YouShallNotPass()