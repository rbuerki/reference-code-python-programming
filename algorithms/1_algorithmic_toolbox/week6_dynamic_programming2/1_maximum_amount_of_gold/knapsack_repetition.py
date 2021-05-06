def knapsack(W: int, w: list, v: list):
    """W is the total capacity, w an array of 'weights', v the
    corresponding list of 'values'. Repetitions allowed.
    """
    # Initialize the look-up list
    dp = [0] * (W + 1)
    for item, item_weight in enumerate(w):
        if item_weight <= W:
            dp[item_weight] = v[item]

    for capacity in range(W + 1):
        for _, item_weight in enumerate(w):
            if capacity >= item_weight:
                dp[capacity] = max(
                    dp[capacity], dp[item_weight] + dp[capacity - item_weight]
                )
    return dp[W]


if __name__ == "__main__":
    w = [1, 2, 3]
    v = [60, 100, 120]
    W = 4
    print(knapsack(W, w, v))
