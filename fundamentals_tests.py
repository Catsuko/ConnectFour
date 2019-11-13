from core.board import Board
import argparse

def format_result(description, order, passed):
    return " [%s]  %d.  %s" % ("+" if passed else " ", order + 1, description)

def format_pass(name, order):
    return format_result("Passed %s" % name, order, True)

def format_fail(name, cause, order):
    return format_result("Failed %s %s" % (name.ljust(40, '.'), cause), order, False)

def test_placement(name, expected, strategy, current_moves, results):
    order = len(results)
    chosen_placement = -1
    try:
        board = Board(7, 6, current_moves)
        token = (len(current_moves) % 2) + 1
        chosen_placement = strategy.place_token(token, board.to_array())
        assert(chosen_placement == expected)
        results.append(format_pass(name, order))
    except AssertionError as error:
        cause = "placed token at %d, expected %d" % (chosen_placement, expected)
        results.append(format_fail(name, cause, order))
    except Exception as exception:
        results.append(format_fail(name, "failed due to %s" % exception, order))

parser = argparse.ArgumentParser(description="Use these tests to gauge your strategy's fundamentals.")
parser.add_argument('s', type=str, help="Name of strategy module to load.")
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
   ("V Win from Middle", 3, [3, 0, 3, 6, 3, 0]),
   ("V Win from Left Edge", 0, [0, 1, 0, 4, 0, 6]),
   ("V Win from Right Edge", 6, [6, 1, 6, 4, 6, 0]),
   ("V Win from Top", 3, [3, 6, 3, 3, 0, 3, 6, 3, 1]),
   ("V Block from Middle", 3, [3, 0, 3, 6, 3]),
   ("V Block from Left Edge", 0, [0, 1, 0, 4, 0]),
   ("V Block from Right Edge", 6, [6, 1, 6, 4, 6]),
   ("V Block from Top", 3, [3, 6, 3, 3, 0, 3, 6, 3])
]

results = []
[test_placement(t[0], t[1], strat_module.export_strategy(), t[2], results) for t in tests]
print("Fundamentals for %s\n\n%s" % (strat_module.export_strategy(), "\n".join(results)))
