from core.strategy import Strategy
import random

class RandomStrategy(Strategy):

    def place_token(self, token, board):
      column = -1
      while column < 0:
        random_int = random.randint(0,6)
        column = random_int if board[0][random_int] == 0 else -1
      return column

def export_strategy():
    return RandomStrategy()