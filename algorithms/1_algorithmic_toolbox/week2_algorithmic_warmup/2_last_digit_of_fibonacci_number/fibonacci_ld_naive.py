# python3


def calc_fib_last_digit(n):
    """Naive calculation."""
    if n <= 1:
        return n

    else:
        previous = 0
        current = 1

        for _ in range(n - 1):
            previous, current = current, previous + current

        return current % 10


if __name__ == "__main__":
    n = int(input())
    print(calc_fib_last_digit(n))
