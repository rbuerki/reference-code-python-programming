# Uses python3
# import sys


def get_change(m):
    """My implementation. But there is also a one-liner for this:
    return (m / 10) + ((m % 10) / 5) + (m % 5)
    """
    coins = [10, 5, 1]
    change = 0
    remainder = m
    for c in coins:
        change += remainder // c
        remainder = remainder % c

    assert remainder == 0
    return change


if __name__ == "__main__":
    # m = int(sys.stdin.read())
    m = int(input())
    print(get_change(m))
