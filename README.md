# ConnectFour

Write your own strategy and compete against other players in a game of ConnectFour

## Usage

Run the game with:
```python
python console_connect_four.py
```

Making some simple tweaks to `console_connect_four.py` can give neat results!

You can pit the bot against itself for a uneventful showdown:
```python
player_bot = Player(name="Bot", strategy=LeftToRightStrategy())
game.play(player_bot, player_bot, game_view)
```

Or play against a friend by having a player with the `StdInStrategy` play themselves:
```python
player_person = Player(name="Player", strategy=StdInStrategy())
game.play(player_person, player_person, game_view)
```

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

### Testing your Strategy

To test your strategy, import it into the `console_connect_four.py` file. If you had added `/core/example_strategy.py` then you would import it by adding the following line to the top of `console_connect_four.py`:
```python
from core.example_strategy import ExampleStrategy
```

From here, pass an instance of your strategy to one of the players and then run the file.
```python
#player1 = Player(name="Bot", strategy=LeftToRightStrategy())
player1 = Player(name="Example Bot", strategy=ExampleStrategy())
player2 = Player(name="Player", strategy=StdInStrategy())
game.play(player1, player2, game_view)
```

See if it can beat `LeftToRightStrategy` and experiment with letting it go first and second.

### Example Implementation: LeftToRightStrategy

For an easy example, try reading through `/core/left_to_right_strategy.py`
```python
from .strategy import Strategy

class LeftToRightStrategy(Strategy):

    def place_token(self, token, board):
        top_row = board[0]
        for x in range(len(top_row)):
            if top_row[x] == 0:
                return x
        return -1

```

If none of the top rows are empty then returning -1 essentially means giving up because it is not a valid column index.



