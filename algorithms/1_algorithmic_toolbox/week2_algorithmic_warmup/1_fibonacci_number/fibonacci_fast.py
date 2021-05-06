# python3


def calc_fib(n):
    """Calculate with lookup list."""
    if n <= 1:
        return n

    else:
        fibs = [0, 1]
        for _ in range(2, n):
            fibs.append(fibs[-1] + fibs[-2])
        return fibs[-1] + fibs[-2]


if __name__ == "__main__":
    n = int(input())
    print(calc_fib(n))
