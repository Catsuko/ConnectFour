from core.board import Board
import argparse

def format_result(description, order, passed):
    return " [%s] %3d.  %s" % ("+" if passed else " ", order + 1, description)

def format_pass(name, order):
    return format_result("Passed %s" % name, order, True)

def format_fail(name, cause, order):
    return format_result("Failed %s %s" % (name.ljust(40, '.'), cause), order, False)

def test_placement(name, expected, strategy, current_moves, results, printBoard):
    order = len(results)
    chosen_placement = -1
    try:
        board = Board(7, 6, current_moves)
        token = (len(current_moves) % 2) + 1
        chosen_placement = strategy.place_token(token, board.to_array())
        if printBoard:
            print("")
            print("%s (Placing %s)" % (name, token))
            print("\n".join([str(row) for row in board.to_array()]))
            print("")
        assert(any(x == chosen_placement for x in expected))
        results.append(format_pass(name, order))
    except AssertionError as error:
        cause = "placed token at %d, expected %s" % (chosen_placement, " or ".join([str(x) for x in expected]))
        results.append(format_fail(name, cause, order))
    except Exception as exception:
        results.append(format_fail(name, "failed due to %s" % exception, order))

parser = argparse.ArgumentParser(description="Use these tests to gauge your strategy's fundamentals.")
parser.add_argument('s', type=str, help="Name of strategy module to load.")
parser.add_argument('--visuals', const=True, nargs='?', help="Print the board as each test is run.")
args = parser.parse_args()
print("")
try:
    strat_module = __import__('strategies.%s' % args.s, fromlist=[''])
except ImportError as error:
    print("No module found matching '%s'" % args.s)
    print("Ensure the file exists in the strategies directory and the module name is correct.")
    print("For example: the module name for 'example_strategy.py' would be 'example_strategy'")
    exit()

# Add tests by providing a description, the expected column placement and the previous moves
tests = [
    # Vertical Attacking
   ("V Win from Middle", [3], [3, 0, 3, 6, 3, 0]),
   ("V Win from Left Edge", [0], [0, 1, 0, 4, 0, 6]),
   ("V Win from Right Edge", [6], [6, 1, 6, 4, 6, 0]),
   ("V Win from Top", [3], [3, 6, 3, 3, 0, 3, 6, 3, 0]),
   ("V Win with Equal Stacks", [4], [4, 3, 4, 3, 4, 3]),
   # Vertical Defending
   ("V Block from Middle", [3], [3, 0, 3, 6, 3]),
   ("V Block from Left Edge", [0], [0, 1, 0, 4, 0]),
   ("V Block from Right Edge", [6], [6, 1, 6, 4, 6]),
   ("V Block from Top", [3], [3, 6, 3, 3, 0, 3, 6, 3]),
   # Horizontal Attacking
   ("H Win from Left Edge", [3], [0, 0, 1, 1, 2, 0]),
   ("H Win from Right Edge", [3], [6, 6, 5, 5, 4, 6]),
   ("H Win from Middle", [1, 5], [3, 0, 2, 6, 4, 0]),
   ("H Win from Second Row", [6], [5, 5, 3, 3, 0, 4, 5, 4, 0, 6, 4]),
   # Horizontal Defending
   ("H Block from Left Edge", [3], [0, 0, 1, 1, 2]),
   ("H Block from Right Edge", [3], [6, 6, 5, 5, 4]),
   ("H Block at Left Edge", [0], [1, 6, 2, 4, 3]),
   ("H Block at Right Edge", [6], [3, 2, 4, 0, 5]),
   ("H Block in Middle", [2], [3, 5, 1, 0, 4]),
   # Prevention
   ("H Prevention from Left Middle", [0, 1, 2, 4, 5, 6], [0, 1, 0, 0, 1, 2, 2]),
   ("D Prevention from Left Edge", [0, 1, 3, 4, 5, 6], [3, 0, 3, 0, 2, 1, 0, 1, 3, 3])
]

results = []
[test_placement(t[0], t[1], strat_module.export_strategy(), t[2], results, args.visuals) for t in tests]
print("Fundamentals for %s\n\n%s" % (strat_module.export_strategy(), "\n".join(results)))
