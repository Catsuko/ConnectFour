from core.connect_four_game import ConnectFourGame
from core.board import Board
from core.player import Player
from core.strategy_loader import StrategyLoader
from tournaments.round_robin_tournament import RoundRobinTournament
from views.zelle_graphics_game_view import ZelleGraphicsGameView
from views.console_game_view import ConsoleGameView
from strategies.stdin_strategy import StdInStrategy

game = ConnectFourGame(Board(7,6))
view = ZelleGraphicsGameView(delay=0)
game.play(Player("Me", StdInStrategy()), Player("You", StdInStrategy()), view)

