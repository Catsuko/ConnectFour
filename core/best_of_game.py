import math

class BestOfGame:

    def __init__(self, game, limit):
        self.game = game
        self.limit = limit

    def play(self, player1, player2, view):
        results = []
        players = [player1, player2]
        limit_half = self.limit / 2.0
        while len(results) < self.limit and all(limit_half >= results.count(player) for player in players):
            plays = len(results)
            first_player = players[plays % len(players)]
            second_player = players[(plays + 1) % len(players)]
            results.append(self.game.play(first_player, second_player, view))        # TODO: This breaks when a player is playing themselves, how to fix??
        player1_wins = results.count(player1)
        player2_wins = results.count(player2)
        # TODO: Lots of duplication and mess below, improve!!
        # TODO: Some kind of score\outcome object is needed!
        outcome = "Draw" if player1_wins == player2_wins else "%s wins!" % (player1 if player1_wins > player2_wins else player2)
        view.print_result("%s (%d-%d)" % (outcome, player1_wins, player2_wins))  
        if player1_wins == player2_wins:
            return [player1, player2]
        else:
            return player2 if player1_wins < player2_wins else player1

    def __str__(self):
        return "Best of %d" % self.limit
