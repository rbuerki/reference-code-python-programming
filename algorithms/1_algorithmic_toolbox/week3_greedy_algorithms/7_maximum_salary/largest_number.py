# Uses python3
import sys
from typing import List


def largest_number(a: List[int]):
    """My implementation."""
    result = []
    digits_list = [list(map(int, str(x))) for x in a]
    while len(digits_list) > 0:
        max_digit = [-1]
        for x in digits_list:
            if _check_if_x_first(x, max_digit) is True:
                max_digit = x
        digits_list.remove(max_digit)
        result.append(max_digit)

    result = "".join([str(item) for sublist in result for item in sublist])
    return result


def _check_if_x_first(x: List[int], max_digit: List[int]):
    """Return True if x is to be placed before max_digit.
    ("Larger" or equal to max_digit.)
    """
    if x == max_digit:
        return True
    # if len x is longer and their overlapping section is the same: handle
    elif len(x) > len(max_digit) and x[: len(max_digit)] == max_digit:
        if min(x[len(max_digit) :]) >= min(max_digit):
            return True
        else:
            return False
    # if len x is longer or the same, but their overlapping section differs
    elif len(max_digit) <= len(x):
        for i in range(len(max_digit)):
            if x[i] < max_digit[i]:
                return False
            else:
                return True
    else:
        # if len x is shorter
        for i in range(len(x)):
            if x[i] < max_digit[i]:
                return False
            else:
                return True


# if __name__ == "__main__":
#     a = list(map(int, input().split()))
#     print(check_if_x_first(a))


if __name__ == "__main__":
    # input = sys.stdin.read()  # TODO
    input = "x 2 8 2 3 6 4 1 1 10 6 3 100 3 6 1 3 8 4 6 1 10 8 4 10 4 1 3 2 3 2 6 1 5 2 9 8 5 10 8 7 9 6 4 2 6 3 8 8 9 8 2 9 10 3 10 7 5 7 1 7 5 1 4 7 6 1 10 5 4 8 4 2 7 8 1 1 7 4 1 1 9 8 6 5 9 9 3 7 6 3 10 8 10 7 2 5 1 1 9 9 5"
    # input = " x 23 23 1 455 45 128 "
    # input = "2 21 2"
    data = input.split()
    # data = input().split()
    a = list(map(int, data[1:]))
    print(largest_number(a))
