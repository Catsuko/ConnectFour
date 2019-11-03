from core.connect_four_game import ConnectFourGame
from core.board import Board
from core.player import Player
from core.strategy_loader import StrategyLoader
from tournaments.round_robin_tournament import RoundRobinTournament
from views.zelle_graphics_game_view import ZelleGraphicsGameView
from views.console_game_view import ConsoleGameView

strategy_loader = StrategyLoader(strategies_dir="strategies")
tournament = RoundRobinTournament(strategy_loader, ConsoleGameView())
results = tournament.run()
print('\n'.join(results))

