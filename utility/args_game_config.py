class ArgsGameConfig:

    def __init__(self, parser, default_number_of_games=1, default_delay=0.2):
        self.default_number_of_games = default_number_of_games
        self.default_delay = default_delay
        # TODO: Don't do work in the ctor, how can this be improved?
        parser.add_argument('-n', type=int, help="number of games to play")
        parser.add_argument('-d', type=float, help="delay in seconds between turns")
        self.args = parser.parse_args()
        
    def number_of_games(self):
        return self.args.n if self.args.n and self.args.n > 0 else self.default_number_of_games

    def turn_delay(self):
        return self.args.d if self.args.d and self.args.d > 0 else self.default_delay
