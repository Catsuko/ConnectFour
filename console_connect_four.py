from core.connect_four_game import ConnectFourGame
from core.board import Board
from core.player import Player
from core.strategy_loader import StrategyLoader
from tournaments.round_robin_tournament import RoundRobinTournament
from views.zelle_graphics_game_view import ZelleGraphicsGameView
from views.console_game_view import ConsoleGameView
from core.best_of_game import BestOfGame
from strategies.random_strategy import RandomStrategy
from strategies.left_to_right_strategy import LeftToRightStrategy

strategy_loader = StrategyLoader(strategies_dir="strategies")
tournament = RoundRobinTournament(strategy_loader, ConsoleGameView())
results = tournament.run()
print(results)
