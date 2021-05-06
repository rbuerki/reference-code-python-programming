# Uses python3
import sys


def binary_search_recursive(a: list, x: int, i_mod: int = 0) -> int:
    """Return the index of the search item x, or -1 if not found.
    No guarantees as to *which* index of the search item is returned,
    if multiple exist.

    Attention: In the recursive implementation, we have to keep track
    of the orginial indices everytime we discard from the left.
    Else we could not return the final original index of x!
    """

    while len(a) > 0:

        i_mid = len(a) // 2

        if a[i_mid] == x:
            return i_mid + i_mod

        if a[i_mid] < x:
            # Need to modify i_mod because discarding elements from left
            return binary_search_recursive(a[i_mid + 1 :], x, i_mod + i_mid + 1)
        elif a[i_mid] > x:
            return binary_search_recursive(a[:i_mid], x, i_mod)

    # If x is not found
    return -1


def binary_search_iterative(a: list, x: int) -> int:
    """Return the index of the search item x, or -1 if not found.
    No guarantees as to *which* index of the search item is returned,
    if multiple exist.
    """
    i_low, i_high = 0, len(a) - 1

    while i_low <= i_high:
        i_mid = i_low + (i_high - i_low) // 2  # can't overflow
        # i_mid = (i_low + i_high) // 2  # may overflow

        if a[i_mid] == x:
            return i_mid
        elif x < a[i_mid]:
            i_high = i_mid - 1
        else:
            i_low = i_mid + 1

    # If x is not found
    return -1


def linear_search(a, x):
    """If the item is not found, return -1."""
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == "__main__":
    input = sys.stdin.read()
    # input = "5 1 5 8 12 13 5 8 1 23 1 11"
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2 :]:
        print(binary_search_iterative(a, x), end=" ")
