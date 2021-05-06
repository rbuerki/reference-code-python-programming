import sys
from typing import List


def _evalt(a: int, b: int, op: str) -> int:
    """Small helper function for translating the operand
    string into an actual operand operation.
    """
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    else:
        raise AssertionError("Invalid operand")


def _max_and_min(max_table, min_table, i: int, j: int, operands: List[str]):
    """Recurrence relation for our problem. Solved by looking up the
    results from previous (smaller) subexpressions and finding the min
    and max values from all possible combinations with the actual
    operand.
    """
    min_value = float("inf")
    max_value = float("inf") * -1

    # We just go through all possibilities of splitting our subexpression (i, j)
    # into two sub subexpressions from i to k and from k plus 1 to j.
    for k in range(i, j):
        a = _evalt(max_table[i][k], max_table[k + 1][j], operands[k])
        b = _evalt(max_table[i][k], min_table[k + 1][j], operands[k])
        c = _evalt(min_table[i][k], max_table[k + 1][j], operands[k])
        d = _evalt(min_table[i][k], min_table[k + 1][j], operands[k])
        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)

    return max_value, min_value


def get_maximum_value(dataset: List[str]) -> int:
    """Main function."""
    digits: List[int] = [int(x) for x in dataset[::2]]
    operands: List[str] = dataset[1::2]

    # Initialize the 2 lookup tables with value zero
    min_table = [[0 for _ in range(len(digits))] for _ in range(len(digits))]
    max_table = [[0 for _ in range(len(digits))] for _ in range(len(digits))]

    # Fill the n=0-diagonal with the respective digits
    for i in range(len(digits)):
        min_table[i][i] = digits[i]
        max_table[i][i] = digits[i]

    # Outer loop by increasing size of operation (size = n of operands)
    for size in range(1, len(digits)):
        # Inner loop to go through all possible players i, j such that j - i = size
        for i in range(0, len(digits) - size):
            j = i + size
            max_value, min_value = _max_and_min(
                max_table, min_table, i, j, operands[: i + size]
            )
            max_table[i][j] = max_value
            min_table[i][j] = min_value

    return max_table[0][len(digits) - 1]


if __name__ == "__main__":
    input = sys.stdin.read()
    # input = "5-8+7*4-8+9"
    dataset = list(input)
    print(get_maximum_value(dataset))
