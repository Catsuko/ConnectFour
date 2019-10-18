# ConnectFour
Write your own strategy and compete against other players in a game of ConnectFour

> Below are the basic concepts in my eyes, add comments or other ideas below!
~ Lewis

## Game

- Matches two players against each other and determines the winner

### Rules

- 7x6 grid
- Players take turns placing tokens into a column of the grid
- Tokens fall and occupy the bottom-most vacant slot of the column
- A player is declared the winner if four of their tokens form a straight line. The line can be vertical, horizontal or diagonal
- A player is declared the winner if their opponent makes an error while selecting a column or selects an invalid column

### Extensions

 - A BestOf Game Decorator would be useful, this would play multiple games to determine the winner in a BestOf(N) format.
 - Game Decorators that randomize or alternate who goes first would be handy down the line, otherwise we might find going first is a huge advantage or disadvantage

## Game View

- Display information about the start of the game ("Game 1 Robot vs Ninja")
- Display the board after each turn
- Display information about the end of the game ("Robot wins!", "Ninja made a mistake and lost!")

### Extensions

 - I would like a TextFileGameView that would write each turn into a text file so I can review why my algorithm got its ass kicked and make improvements.

## Player

 - Name for ID and display
 - Select which column they wish to place a token in
 
 ### Extensions
 
 - Even though the aim is to pit algorithms against each other, we could construct a player that listens to input and then have a functioning ConnectFour game!

## PlayerRepository

 - Get player with given name
 - Get all available players
