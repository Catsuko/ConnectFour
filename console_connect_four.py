from core.connect_four_game import ConnectFourGame
from core.board import Board
from core.left_to_right_strategy import LeftToRightStrategy
from core.stdin_strategy import StdInStrategy
from core.player import Player
from views.zelle_graphics_game_view import ZelleGraphicsGameView

game = ConnectFourGame(Board(width=7, height=6))
game_view = ZelleGraphicsGameView()
player1 = Player(name="Bot", strategy=LeftToRightStrategy())
player2 = Player(name="Player", strategy=StdInStrategy())
game.play(player1, player2, game_view)
