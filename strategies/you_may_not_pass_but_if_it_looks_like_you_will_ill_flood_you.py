from core.strategy import Strategy

class YouMayNotPassButIfItLooksLikeYouMightIllFloodYou(Strategy):
    def __init__(self):
        super().__init__()
        self.position = 0
        self.NUM_OF_POSITIONS = 3
        self.increments = 1
        self.switched_to_flood = False
    
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
    
    def _find_rows_with_vulnerable_3(self, our_token):
        rows = self.board
        
        vulnerable_rows = []

        for row in rows:
            amount_continuous = 0
            for col, space in enumerate(row):
                if space != our_token:
                    if space != 0:
                        amount_continuous += 1
                    elif amount_continuous == 3:
                        vulnerable_rows.append(col)
                        break
                else:
                    amount_continuous = 0
        
        return vulnerable_rows
    
    def _flood(self):
        reversed_board = self.board.copy()
        reversed_board.reverse

        for row in reversed_board:
            for index, token in enumerate(row):
                if token == 0:
                    return index
    
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
        
        vertical_vulnerabilities = self._find_columns_with_vulnerable_3(token)
        horizontal_vulnerabilities = self._find_rows_with_vulnerable_3(token)
        vulnerabilities = (len(vertical_vulnerabilities) > 0) or (len(horizontal_vulnerabilities) > 0)
        if vulnerabilities:
            if(len(vertical_vulnerabilities) > 0):
                column = vertical_vulnerabilities[0]
            elif (len(horizontal_vulnerabilities) > 0):
                column = horizontal_vulnerabilities[0]
        else:
            if self.switched_to_flood:
                column = self._flood()
            else:
                column = self._you_shall_not_pass()
                col_counter = 0
                while(self._is_column_full(column)):
                    column = self._you_shall_not_pass()
                    col_counter += 1
                    if(col_counter > self.NUM_OF_POSITIONS):
                        self.switched_to_flood = True
                        column = self._flood()
        return column

def export_strategy():
    return YouMayNotPassButIfItLooksLikeYouMightIllFloodYou()