from core.connect_four_game import ConnectFourGame
from core.board import Board
from core.player import Player
from core.strategy_loader import StrategyLoader
from tournaments.round_robin_tournament import RoundRobinTournament
from views.zelle_graphics_game_view import ZelleGraphicsGameView

strategy_loader = StrategyLoader(strategies_dir="strategies")
tournament = RoundRobinTournament(strategy_loader)
results = tournament.run()
print(results)

'''
player1 = Player(name="Bot", strategy=strategy_loader[0])
player2 = Player(name="Player", strategy=strategy_loader[1])
game = ConnectFourGame(Board(width=7, height=6))
game.play(player1, player2, ZelleGraphicsGameView())
'''

