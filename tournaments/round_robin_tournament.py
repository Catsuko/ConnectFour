from core.connect_four_game import ConnectFourGame
from core.board import Board
from itertools import permutations
from functools import reduce

class RoundRobinTournament:
    def __init__(self, players, view):
        self.players = players
        self.matches = []
        self.results = {}
        self.view = view
    
    def _calc_match_permutations(self):
        num_players = len(self.players)        
        for player in range(num_players):
            other_players = list(range(num_players))
            other_players.remove(player)
            [self.matches.append([player, opponent]) for opponent in other_players if not self._match_exists(player, opponent)]        
    
    def _match_exists(self, player1_index, player2_index):
        for match in self.matches:
            if player1_index in match and player2_index in match:
                return True
        return False
    
    def _clear_results(self):
        self.results.clear()
        for player in self.players:
            self.results[player] = []

    def _run_off_matches(self):
        self._clear_results()
        for match in self.matches:
            game = ConnectFourGame(Board(width=7, height=6))
            player1 = self.players[match[0]]
            player2 = self.players[match[1]]
            winner = game.play(player1, player2, self.view)
            loser = player2 if self.players[match[0]] == winner else player1
            self.results[winner].append(loser)


    def _get_ranking(self):
        ranks = []
        [ranks.append((type(key).__name__, len(value))) for key, value in self.results.items()]
        ranks.sort(key=lambda rank_tup: -rank_tup[1])
        return ranks

    def run(self):
        self._calc_match_permutations()
        self._run_off_matches()
        return self._get_ranking()