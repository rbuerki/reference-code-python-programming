# Uses python3
import sys
from typing import List, Union


def get_optimal_value(
    capacity: Union[float, int],
    weights: List[Union[float, int]],
    values: List[Union[float, int]],
):
    """Fractional knappsack solution."""

    # Initialize start value and calc the relative
    # value per weight for every item
    value = 0
    rel_values: List[Union[float, int]] = [
        v / w for v, w in zip(values, weights)
    ]

    # Sort rel_values, weights and values by rel_values reverse
    rel_values, values, weights = [
        list(li)
        for li in zip(*sorted(zip(rel_values, values, weights), reverse=True))
    ]

    # Iterate through the items from best to worst
    for i in range(len(weights)):
        if capacity == 0:
            return value
        else:
            fitting_weight = min([weights[i], capacity])
            value += fitting_weight * rel_values[i]
            capacity -= fitting_weight
            weights[i] -= fitting_weight

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    # data = list(map(int, input().split()))
    n, capacity = data[0:2]
    values = data[2 : (2 * n + 2) : 2]
    weights = data[3 : (2 * n + 2) : 2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
