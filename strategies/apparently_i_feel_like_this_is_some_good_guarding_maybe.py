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
    
    #if the top row is not full the column is not full
    def _is_column_full(self, column_index):
        return self.current_board[0][column_index] != 0
    
    #if adds to 2d tuples (1,2) + (3,4) = (4,6)
    def _add_2d_tup(self,a,b):
        return (a[0]+b[0], a[1]+b[1])
    
    #aabb checking with early exits
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
    
    #marchs from the starting position, moving by step amount until the stop_condition is met
    def _march(self, start, step, stop_condition):
        pos = self._add_2d_tup(start, step) #move to our first position
        locations = []
        while self._is_in_bounds(pos): #while out position is inside the bounds of the board
            current_token = self.current_board[pos[1]][pos[0]] #get the token at out position
            if stop_condition(current_token): #if our stop condition is met, return early
                return locations
            locations.append(pos) #add our position to the locations we've deemed as "found" in our search
            pos = self._add_2d_tup(pos, step)   #move to our next position
        return locations #we've moved as far as we're allowed so we will return what we've found

    def find_horizontal_continous(self, start, stop_condition):
        results = []
        results.append(self._march(start, (1,0), stop_condition))
        results.append(self._march(start, (-1,0), stop_condition))
        return results
    
    def find_vertical_continous(self, start,stop_condition):
        results = []
        results.append(self._march(start, (0,1), stop_condition))
        results.append(self._march(start, (0,-1), stop_condition))
        return results
    
    # diagonal up is like this:
    # 001
    # 010
    # 100
    def find_diagonal_up_continous(self, start, stop_condition):
        results = []
        results.append(self._march(start, (1,-1), stop_condition))
        results.append(self._march(start, (-1,1), stop_condition))
        return results
    
    # diagonal down is like this:
    # 100
    # 010
    # 001
    def find_diagonal_down_continous(self, start, stop_condition):
        results = []
        results.append(self._march(start, (1,1), stop_condition))
        results.append(self._march(start, (-1,-1), stop_condition))
        return results
    
    #search all directions for continous tokens
    def _does_space_have_potential(self, position, end_condition):
        if self._is_in_bounds(position) == False:
            return False
        
        if self.current_board[position[1]][position[0]] != 0:
            return False        
        
        count_positions = lambda pos_list: sum(len(x) for x in pos_list)

        verticals_conts = self.find_vertical_continous(position, end_condition)
        if count_positions(verticals_conts) > 2:
            return True

        horizontal_conts = self.find_horizontal_continous(position, end_condition)
        if count_positions(horizontal_conts) > 2:
            return True
        
        diag_up_conts = self.find_diagonal_up_continous(position, end_condition)
        if count_positions(diag_up_conts) > 2:
            return True

        diag_down_conts = self.find_diagonal_down_continous(position, end_condition)
        if count_positions(diag_down_conts) > 2:
            return True
    
    #search all possible connection directions for enemy token
    def _is_space_vulnerable(self, position):
        stop_condition = lambda token, our_token=self.token: token == 0 or token == our_token
        return self._does_space_have_potential(position, stop_condition)
    
    #search all possible connection directions for our token
    def _is_space_an_opportunity(self, position):
        stop_condition = lambda token, our_token=self.token: token == 0 or token != our_token
        return self._does_space_have_potential(position, stop_condition)
        

    def _do_i_feel_like_i_should_guard(self):        
        for y in range(0, self.height()):
            for x in range(0, self.width()):
                if self._is_space_vulnerable((x,y)):
                    return (True, x)
        return (False, -1)
    
    def _do_i_feel_like_i_should_seize_the_win(self):        
        for y in range(0, self.height()):
            for x in range(0, self.width()):
                if self._is_space_an_opportunity((x,y)):
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
        
        i_feel_like_winning = self._do_i_feel_like_i_should_seize_the_win()
        if i_feel_like_winning[0] == True:            
            return i_feel_like_winning[1]
        
        return self.flood()

def export_strategy():
    return ApparentlyIFeelLikeThisIsSomeGoodGuardingMaybe()