from core.connect_four_game import ConnectFourGame
from core.crap_player import CrapPlayer
from core.stdin_player import StdInPlayer
from views.console_game_view import ConsoleGameView

game = ConnectFourGame(width=7,height=6)
game_view = ConsoleGameView(scale=2)
player1 = CrapPlayer(name='Bot')
player2 = StdInPlayer(name='Player')
game.play(player1, player2, game_view)
