from core.connect_four_game import ConnectFourGame
from core.board import Board
from core.left_to_right_strategy import LeftToRightStrategy
from core.stdin_strategy import StdInStrategy
from core.player import Player
from core.strategy_loader import StrategyLoader
from views.console_game_view import ConsoleGameView

game = ConnectFourGame(Board(width=7, height=6))
game_view = ConsoleGameView(scale=2)

strategy_loader = StrategyLoader("strategies")
strategy_loader.find_and_load()
if len(strategy_loader) < 2:
    exit()

player1 = Player(name="Bot", strategy=strategy_loader[0])
player2 = Player(name="Player", strategy=strategy_loader[1])
game.play(player1, player2, game_view)
