# Uses python3
# import sys


def lcm_fast(x, y):
    """My own semy-fast solution ... did past the tests."""
    a = max(x, y)
    b = min(x, y)
    for n in range(1, b + 1):
        multiple = n * a
        if (n * a) % b == 0:
            return multiple


def lcm_faster(x, y):
    """Much more effective way to get the least common multiple of
    two numbers is to multiply them and divide the result by their
    greatest common divisor. The greatest common divisor may be
    computed by the Euclidean algorithm, which is very fast, because
    it does not require factorization of the given numbers.
    """
    return int(x * y / _calc_gcd(x, y))


def _calc_gcd(x, y):
    """Implementation from last exercice. Called within lcm_faster."""
    # current_gcd = 1
    a = max(x, y)
    b = min(x, y)
    # Everything divides zero
    if b == 0:
        return a

    else:
        a_prime = a % b
        return _calc_gcd(b, a_prime)


if __name__ == "__main__":
    # input = sys.stdin.read()
    x, y = map(int, input().split())
    print(lcm_faster(x, y))
