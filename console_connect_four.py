from core.connect_four_game import ConnectFourGame
from core.left_to_right_strategy import LeftToRightStrategy
from core.stdin_strategy import StdInStrategy
from core.player import Player
from views.console_game_view import ConsoleGameView

game = ConnectFourGame(width=7,height=6)
game_view = ConsoleGameView(scale=2)
player1 = Player(name="Bot", strategy=LeftToRightStrategy())
player2 = Player(name="Player", strategy=StdInStrategy())
game.play(player1, player2, game_view)
