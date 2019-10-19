from colorama import Back, Style

class ConsoleGameView:

    def __init__(self, scale=1):
        self.tile = ' ' * scale
        self.colors = [Back.BLACK, Back.RED, Back.YELLOW]

    def print_start(self, player1, player2):
        print()
        print("%s vs %s" %(player1,player2,))
        print()

    def print_board(self, board):
        print()
        for x in range(len(board)):
            print(Back.BLUE + self.tile, end='')
            for y in range(len(board[x])):
                print(self.colors[board[x][y]] + self.tile, end='')
            print(Back.BLUE + self.tile, end='')
            print(Style.RESET_ALL)
        for x in range(len(board) + 3):
            print(Back.BLUE + self.tile, end='')
        print(Style.RESET_ALL, flush=True)


    def print_end(self, winner):
        print()
        print("%s won!" % winner)
        print()