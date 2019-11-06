import argparse
from core.connect_four_game import ConnectFourGame
from core.board import Board
from core.registered_player import RegisteredPlayer
from views.zelle_graphics_game_view import ZelleGraphicsGameView
from core.best_of_game import BestOfGame
from core.strategy_loader import StrategyLoader

parser = argparse.ArgumentParser()
parser.add_argument("-n", type=int, help="number of games to play")
args = parser.parse_args()
number_of_games = args.n if args.n and args.n > 0 else 1
game = BestOfGame(ConnectFourGame(Board(7,6)), number_of_games)
view = ZelleGraphicsGameView(delay=0.25)
strategies = StrategyLoader(strategies_dir="strategies")
game.play(RegisteredPlayer(strategies), RegisteredPlayer(strategies), view)

