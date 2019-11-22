from core.score import Score

class BracketTournament:

    def __init__(self, game):
        self.game = game

    def run(self, players, view):
        if len(players) < 2:
            raise "Not enough players to run a tournament."
        outcomes = []
        player_count = len(players)
        for i in range(0, player_count, 2):
            if i == player_count - 1:
                outcomes.insert(0, (players[i], Score(0,0,0)))
            else:
                outcomes.append(self.determine_outcome(players[i], players[i+1], view))
        return outcomes[0] if player_count == 2 else self.run([outcome[0] for outcome in outcomes], view)

    def determine_outcome(self, player1, player2, view):
        outcome = self.game.play(player1, player2, view)
        if outcome[0] is None:
            raise "Draws cannot occurr in a bracket tournament."
        return outcome
                              
