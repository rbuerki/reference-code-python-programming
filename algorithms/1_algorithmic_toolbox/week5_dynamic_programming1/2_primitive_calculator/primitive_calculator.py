# Uses python3
import sys


def calculator_dp(n: int):
    """The special thing about this implementation is the desired
    output. The int sequence with the shortest path has to be
    backtracked from the dp look-up table.
    """
    # Instantiate list of len + 1, filled with float inf
    sol = [float("inf")] * (n + 1)

    # Base Case: Set sol[1] to one
    sol[1] = 0

    for i in range(2, n + 1):
        n_operations = float("inf")
        if i % 2 == 0:
            n_operations = min(n_operations, sol[i // 2] + 1)
        if i % 3 == 0:
            n_operations = min(n_operations, sol[i // 3] + 1)
        n_operations = min(n_operations, sol[i - 1] + 1)
        sol[i] = n_operations

    # Instantiate the sequence to return, it has length sol[n] + 1
    sequence = [n]

    while n > 1:
        min_operations = sol[n - 1]
        if n % 2 == 0:
            min_operations = min(min_operations, sol[n // 2])
        if n % 3 == 0:
            min_operations = min(min_operations, sol[n // 3])

        if min_operations == sol[n // 3]:
            n = n // 3
        elif min_operations == sol[n // 2]:
            n = n // 2
        else:
            n = n - 1
        sequence.append(n)

    return list(reversed(sequence))


def calculator_greedy(n: int):
    """This is a greed implemenation that is not safe
    and leads to wrong results. Just for info, was provided
    as starter solution.
    """
    sol = []
    while n >= 1:
        sol.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sol)


if __name__ == "__main__":
    input = sys.stdin.read()
    n = int(input)
    # n = int(sys.argv[1])
    # n = 96234
    # print(calculator_dp(n))
    sequence = calculator_dp(n)
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=" ")
