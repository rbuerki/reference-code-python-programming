# Uses python3
import sys
from typing import Tuple


def get_change(money: int, coins: Tuple = (1, 3, 4)) -> int:
    """Calculate minimal number of coins for a given amount 'money'.
    Default coin denominations are 1, 3, 4.
    """
    # Instantiate list of len money + 1, filled with float inf
    sol = [float("inf")] * (money + 1)
    # Base Case: Set state zero to zero
    sol[0] = 0

    # Iterate over all amounts < money, calculating 'min' solution
    # using the previous optimal states for the given coins
    for amount in range(1, money + 1):
        for coin in coins:
            if coin <= amount:
                if (coin <= amount) and (sol[amount - coin] < sol[amount]):
                    sol[amount] = sol[amount - coin] + 1

    return int(sol[money]) if sol[money] != float("inf") else int(-1)


if __name__ == "__main__":
    m = int(sys.stdin.read())
    print(get_change(m))
