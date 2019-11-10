from core.connect_four_game import ConnectFourGame
from core.board import Board
from core.registered_player import RegisteredPlayer
from views.zelle_graphics_game_view import ZelleGraphicsGameView
from core.strategy_loader import StrategyLoader
from views.tracked_player import TrackedPlayer
from views.array_access_view import ArrayAccessView
from strategies.stdin_strategy import StdInStrategy
from core.player import Player

game = ConnectFourGame(Board(7,6))
view = ZelleGraphicsGameView(delay=0.25)
strategies = StrategyLoader(strategies_dir="strategies")
bot = TrackedPlayer(RegisteredPlayer(strategies, name="Bot"), ArrayAccessView())
player = Player("Player", StdInStrategy())
game.play(player, bot, view)

