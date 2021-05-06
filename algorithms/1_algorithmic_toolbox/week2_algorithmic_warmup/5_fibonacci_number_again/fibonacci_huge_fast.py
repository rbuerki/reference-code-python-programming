# Uses python3
# import sys


def get_fibonacci_huge_fast(n, m):
    """My own implementation.
    NOTE: 3000 in the range is by trial and error ...
    """
    if n <= 1:
        return n

    else:
        fibs = [0, 1]
        for _ in range(2, 3000):
            fibs.append((fibs[-1] + fibs[-2]) % m)
            if len(fibs) > 3 and fibs[-3:] == [0, 1, 1]:
                break
        # print(fibs)  # TODO
        period_length = len(fibs) - 3
        # print(period_length)  # TODO
        remainder = n % period_length

        fib = _calc_fib(remainder)
        return fib % m


def _calc_fib(n):
    """Calculate with lookup list. Earlier implementation.
    Called within get_fibonacci_huge_fast.
    """
    if n <= 1:
        return n

    else:
        fibs = [0, 1]
        for _ in range(2, n):
            fibs.append(fibs[-1] + fibs[-2])
        return fibs[-1] + fibs[-2]


if __name__ == "__main__":
    # input = sys.stdin.read()
    n, m = map(int, input().split())
    print(get_fibonacci_huge_fast(n, m))
