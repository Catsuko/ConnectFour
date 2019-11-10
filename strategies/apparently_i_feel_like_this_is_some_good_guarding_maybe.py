from core.strategy import Strategy
from .flood_strategy import FloodStrategy

class ApparentlyIFeelLikeThisIsSomeGoodGuardingMaybe(Strategy):

    def __init__(self):
        self.turn_count = 0;
        self.current_board = None
        self.previous_board = None
        self.token = None
    
    def _init_turn(self, token, board):
        self.previous_board = self.current_board
        self.current_board = board
        self.token = token
        self.turn_count =  0 if self._is_board_empty() else self.turn_count + 1    
    
    def _is_board_empty(self):
        summed_rows = []
        [summed_rows.append(sum(row)) for row in self.current_board]
        return sum(summed_rows) == 0
    
    def height(self):
        return len(self.current_board)
    
    def width(self):
        return len(self.current_board[0])
    
    def _is_column_full(self, column_index):
        return self.current_board[0][column_index] != 0
    
    def _add_2d_tup(self,a,b):
        return (a[0]+b[0], a[1]+b[1])
    
    def _is_in_bounds(self, pos):
        if pos[0] < 0:
            return False
        if pos[1] < 0:
            return False
        if pos[1] >= self.height():
            return False
        if pos[0] >= self.width():
            return False
        return True
    
    def _march(self, start, step, stop_condition):
        pos = self._add_2d_tup(start, step)   
        locations = []
        while self._is_in_bounds(pos):                     
            current_token = self.current_board[pos[1]][pos[0]]
            if stop_condition(current_token):
                return locations
            locations.append(pos)
            pos = self._add_2d_tup(pos, step)   
        return locations

    def find_horizontal_continous(self, start, stop_condition):
        results = []
        results.append(self._march(start,(1,0), stop_condition))
        results.append(self._march(start, (-1,0), stop_condition))
        return results
    
    def find_vertical_continous(self, start,stop_condition):
        results = []
        results.append(self._march(start,(0,1), stop_condition))
        results.append(self._march(start, (0,-1), stop_condition))
        return results
    
    # diagonal up is like this:
    # 001
    # 010
    # 100
    def find_diagonal_up_continous(self, start, stop_condition):
        results = []
        results.append(self._march(start,(1,-1), stop_condition))
        results.append(self._march(start, (-1,1), stop_condition))
        return results
    
    # diagonal down is like this:
    # 100
    # 010
    # 001
    def find_diagonal_down_continous(self, start, stop_condition):
        results = []
        results.append(self._march(start,(1,1), stop_condition))
        results.append(self._march(start, (-1,-1), stop_condition))
        return results
    
    def _is_space_vulnerable(self, position):
        if self._is_in_bounds(position) == False:
            return False
        
        if self.current_board[position[1]][position[0]] != 0:
            return False
        
        stop_condition = lambda token, our_token=self.token: token == 0 or token == our_token
        count_positions = lambda pos_list: sum(len(x) for x in pos_list)

        verticals_conts = self.find_vertical_continous(position, stop_condition)
        if count_positions(verticals_conts) > 2:
            return True

        horizontal_conts = self.find_horizontal_continous(position, stop_condition)
        if count_positions(horizontal_conts) > 2:
            return True
        
        diag_up_conts = self.find_diagonal_up_continous(position, stop_condition)
        if count_positions(diag_up_conts) > 2:
            return True

        diag_down_conts = self.find_diagonal_down_continous(position, stop_condition)
        if count_positions(diag_down_conts) > 2:
            return True

    def _do_i_feel_like_i_should_guard(self):        
        for y in range(0, self.height()):
            for x in range(0, self.width()):
                if self._is_space_vulnerable((x,y)):
                    return (True, x)
        return (False, -1)
    
    def flood(self):
        board = self.current_board.copy()
        board.reverse
        for y in range(0, self.height()):
            for x in range(0, self.width()):
                if board[y][x] == 0:
                    return x

    def place_token(self, token, board):
        self._init_turn(token, board)
        i_feel_like_guarding = self._do_i_feel_like_i_should_guard()
        if i_feel_like_guarding[0] == True:
            return i_feel_like_guarding[1]
        
        return self.flood()

def export_strategy():
    return ApparentlyIFeelLikeThisIsSomeGoodGuardingMaybe()