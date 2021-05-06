# Uses python3
import sys


def optimal_weight(W: int, w: list):
    """Find the optimal gold bars to fill a knapsack fully. (This is
    the no-rep knapsack problem, here without a value component.)
    """
    # Initialize look-up table
    n_items = len(w)
    dp = [[0 for _ in range(W + 1)] for _ in range(n_items + 1)]

    for capacity in range(1, W + 1):
        for item in range(1, n + 1):
            item_weight = w[item - 1]
            if item_weight <= capacity:
                dp[item][capacity] = max(
                    dp[item - 1][capacity - item_weight] + w[item - 1],
                    dp[item - 1][capacity],
                )
            else:
                dp[item][capacity] = dp[item - 1][capacity]
    return dp[n][W]


if __name__ == "__main__":
    input = sys.stdin.read()
    # input = "10 3 1 4 8"
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
