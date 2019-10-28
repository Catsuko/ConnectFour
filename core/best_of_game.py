import math

class BestOfGame:

    def __init__(self, game, limit):
        self.game = game
        self.limit = limit

    def play(self, player1, player2, view):
        results = []
        players = [player1, player2]
        limit_half = math.ceil(self.limit / 2)
        while results.count(player1) < limit_half and results.count(player2) < limit_half:
            plays = len(results)
            first_player = players[plays % len(players)]
            second_player = players[(plays + 1) % len(players)]
            results.append(self.game.play(first_player, second_player, view))
        print(results)
        return player2 if results.count(player1) < limit_half else player1

    def __str__(self):
        return "Best of " + self.limit + " " + self.game
