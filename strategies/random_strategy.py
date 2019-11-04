from core.strategy import Strategy
import random

class RandomStrategy(Strategy):

    def _board_width(self):
      self.width = len(self.board[0])

    def place_token(self, token, board):
      self.board = board
      self._board_width()
      for x in range(1):
        return random.randint(0,7)


def export_strategy():
    return RandomStrategy()
