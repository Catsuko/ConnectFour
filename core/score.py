class Score:

    def __init__(self, wins, draws, losses):
        self.wins = wins
        self.draws = draws
        self.losses = losses

    def __lt__(self, other):
        return self.__cmp__(other) < 0

    def __gt__(self, other):
        return self.__cmp__(other) > 0
    
    def __cmp__(self, other):
        return other.compare_to(self.wins, self.draws, self.losses) * -1

    def __str__(self):
        return "%d-%d-%d" % (self.wins, self.draws, self.losses)

    def compare_to(self, wins, draws, losses):
        own_score = self.calculate(self.wins, self.draws)
        other_score = self.calculate(wins, draws)
        return (own_score > other_score) - (own_score < other_score)

    def calculate(self, wins, draws):
        return (wins * 2) + draws

    def invert(self):
        return Score(self.losses, self.draws, self.wins)

    def join(self, other):
        return other.add(self.wins, self.draws, self.losses)

    def add(self, wins, draws, losses):
        return Score(self.wins + wins, self.draws + draws, self.losses + losses)

    def total_games(self):
        return self.wins + self.draws + self.losses

    def is_determined(self, remaining_games):
        return remaining_games <= 0 or abs(self.wins - self.losses) > remaining_games
        
