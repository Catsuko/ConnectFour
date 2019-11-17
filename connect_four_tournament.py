import argparse
from utility.args_game_config import ArgsGameConfig
from core.connect_four_game import ConnectFourGame
from core.board import Board
from core.best_of_game import BestOfGame
from core.strategy_loader import StrategyLoader
from core.registered_player import RegisteredPlayer
from tournaments.round_robin_tournament import RoundRobinTournament
from views.zelle_graphics_game_view import ZelleGraphicsGameView

config = ArgsGameConfig(argparse.ArgumentParser())
game = BestOfGame(ConnectFourGame(Board(7,6)), config.number_of_games())
tournament = RoundRobinTournament(game)
strategies = StrategyLoader(strategies_dir="strategies")
players = [RegisteredPlayer(strategies) for i in range(config.number_of_players())] 
results = tournament.run(players, ZelleGraphicsGameView(config.turn_delay()))
print('\n'.join(results))
