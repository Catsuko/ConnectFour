from core.connect_four_game import ConnectFourGame
from core.board import Board
from core.best_of_game import BestOfGame
from core.strategy_loader import StrategyLoader
from core.registered_player import RegisteredPlayer
from tournaments.round_robin_tournament import RoundRobinTournament
from views.zelle_graphics_game_view import ZelleGraphicsGameView

game = BestOfGame(ConnectFourGame(Board(7,6)), 2)
tournament = RoundRobinTournament(game)
strategies = StrategyLoader(strategies_dir="strategies")
players = [RegisteredPlayer(strategies) for i in range(3)] 
print(tournament.run(players, ZelleGraphicsGameView(0.5)))
