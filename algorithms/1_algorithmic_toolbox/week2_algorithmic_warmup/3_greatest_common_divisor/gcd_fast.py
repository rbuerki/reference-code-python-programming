# Uses python3


def calc_gcd(x, y):
    """Calculate the greatest common divisor."""
    # Make sure a is bigger than b
    a = max(x, y)
    b = min(x, y)
    # Everything divides zero, so break the recursion and return the result
    if b == 0:
        return a

    else:
        a_prime = a % b
        return calc_gcd(b, a_prime)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(calc_gcd(a, b))
