# Uses python3
# import sys


def fibonacci_sum_fast(n):
    """Not yet implemented. See algo book for a solution."""
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current
        print(sum % 10)  # TODO

    # return sum % 10


if __name__ == "__main__":
    # input = sys.stdin.read()
    n = int(input())
    print(fibonacci_sum_fast(n))
