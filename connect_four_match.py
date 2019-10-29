from core.connect_four_game import ConnectFourGame
from core.board import Board
from core.player import Player
from strategies.left_to_right_strategy import LeftToRightStrategy
from strategies.stdin_strategy import StdInStrategy
from views.zelle_graphics_game_view import ZelleGraphicsGameView
from core.best_of_game import BestOfGame

game = BestOfGame(ConnectFourGame(Board(7,6)), 3)
view = ZelleGraphicsGameView(delay=0.1)
player1 = Player("Mario", StdInStrategy())
player2 = Player("Luigi", LeftToRightStrategy())
game.play(player1, player2, view)

