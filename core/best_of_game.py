import math
from .score import Score

class BestOfGame:

    def __init__(self, game, limit):
        self.game = game
        self.limit = limit

    def play(self, player1, player2, view):
        score = Score(0, 0, 0)
        players = [player1, player2]
        while not(score.is_determined(self.limit - score.total_games())):
            plays = score.total_games()
            first_player = players[plays % len(players)]
            second_player = players[(plays + 1) % len(players)]
            result = self.game.play(first_player, second_player, view)
            score = score.join(result[1] if result[0] == player1 else result[1].invert())
        outcomes = [None, player1, player2]
        other_score = score.invert()
        winner = outcomes[(score > other_score) - (score < other_score)]
        winners_score = score if winner == player1 else other_score
        view.print_result("%s wins! (%s)" % (winner, winners_score))  
        return (winner, winners_score)

    def __str__(self):
        return "Best of %d" % self.limit
