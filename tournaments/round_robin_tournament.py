from core.score import Score
from itertools import permutations
from functools import reduce

class RoundRobinTournament:
    def __init__(self, game):
        self.game = game
        self.matches = []
        self.results = {}
    
    def _calc_match_permutations(self, players):
        num_players = len(players)        
        for player in range(num_players):
            other_players = list(range(num_players))
            other_players.remove(player)
            [self.matches.append([player, opponent]) for opponent in other_players if not self._match_exists(player, opponent)]        
    
    def _match_exists(self, player1_index, player2_index):
        for match in self.matches:
            if player1_index in match and player2_index in match:
                return True
        return False
    
    def _clear_results(self, players):
        self.results.clear()
        for player in players:
            self.results[player] = Score(0,0,0)

    def _run_off_matches(self, players, view):
        self._clear_results(players)
        for match in self.matches:
            player1 = players[match[0]]
            player2 = players[match[1]]
            outcome = self.game.play(player1, player2, view)
            self.results[player1] = self.results[player1].join(outcome[1] if outcome[0] == player1 else outcome[1].invert())
            self.results[player2] = self.results[player2].join(outcome[1] if outcome[0] == player2 else outcome[1].invert())

    def _get_ranking(self):
        ranks = []
        sorted_results = sorted(self.results.items(), key=lambda x: x[1], reverse=True)
        [ranks.append("%s: %s" % (key, value)) for key, value in sorted_results]
        return ranks

    def run(self, players, view):
        self._calc_match_permutations(players)
        self._run_off_matches(players, view)
        return self._get_ranking()
