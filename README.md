# ConnectFour

ConnectFour is a simple game that involves two players taking turns to place tokens in a grid. When one player assembles a line of four tokens, they win! Compete with friends and see who can write the best ConnectFour algorithm.

## Usage

The only pre-requisite needed to run ConnectFour is [python3](https://www.python.org/downloads/).

### Playing a Game

Once installed, navigate to the project directory and run a ConnectFour match by entering the following in the command line:

```
python connect_four_match.py
```

Next register the first player's name and you will be asked to select a strategy. Each strategy presented is loaded from a strategy subclass in the `/strategies` directory. Strategies and how to implement them will be expanded upon further on but they are how a player determines which move they should make. 

Repeat the process for the second player and the match should begin!

### Controlling a player with user input

Select the `StdInStrategy` when presented with the strategy list and that player will be driven by user input via the command line. This can be useful when testing strategies you are implementing. A human vs human match can be set up by having both players select the `StdInStrategy`.

### Running a Tournament

Once multiple strategies have been implemented, you can run a round robin tournament to determine rankings by using the following command:

```
python connect_four_tournament.py
```

A tournament will play matches for each pair of players and then use the accumulated scores to determine a ranking. You can change the number of players by tweaking the `number_of_players` variable in `/connect_four_tournament.py`.

### Writing your own Strategy

To write a new strategy, add a new subclass of the `core.Strategy` class. It has a single responsibility, to determine which column the player should place their token in.
```python
class Strategy:

    def place_token(self, token, board):
        raise NotImplementedError("Implement this method in your subclass.")
```
The token argument specifies which token the player is placing, either a `1` or a `2`. Use this to identify which tokens in the board are yours and plan accordingly.

The board argument is a 2D array that represents the current state of the game. Here is an example of how the board might be filled:
```python
board = [
	[0, 0, 0, 0, 0, 0, 0]
	[0, 0, 0, 0, 0, 0, 0]
	[0, 0, 0, 0, 0, 0, 0]
	[0, 0, 0, 0, 0, 0, 0]
	[0, 0, 0, 0, 0, 0, 0]
	[0, 0, 1, 0, 0, 2, 0]
]
```
A `0` represents an empty spot, a `1` represents a token placed by the first player and a `2` represents a token placed by the second player. When a player chooses a column, their token will then be placed in the lowest empty spot for that column.

The output of the `place_token` method should be the index of the column that you want to place your token in. Placing a token in a out-of-bounds index or into a column that is full will mean that you lose the game, so choose carefully!

### Exporting your Strategy

To export your strategy there are two requirements:
	1. Place your strategy in the `/strategies` directory
	2. Add a `export_strategy` function to your python script

Here is an example implementation of a Strategy with the `export_strategy` function included:

```python
class MyStrategy(Strategy):

	# ...Implementation
	
def export_strategy():
    return MyStrategy()
```

This function will return an instance of your strategy when needed. It is used when registering a player and selecting which strategy the player should use.

### Testing your Strategy

Once it is ready to be exported, test your strategy by selecting it at the start of a match. Try testing it against other algorithms to see how it fares and what its weaknesses are. Also try test it against yourself using the `StdInStrategy`.

### Example Implementation: LeftToRightStrategy

For an easy example, try reading through `/strategies/left_to_right_strategy.py`
```python
from .strategy import Strategy

class LeftToRightStrategy(Strategy):

    def place_token(self, token, board):
        top_row = board[0]
        for x in range(len(top_row)):
            if top_row[x] == 0:
                return x
        return -1

def export_strategy():
    return LeftToRightStrategy()
```

If none of the top rows are empty then returning -1 essentially means giving up because it is not a valid column index.



