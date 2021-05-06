# python3
import sys
from typing import List


def compute_min_refills(distance: int, tank: int, stops: List[int]):
    """Calculate the min number of refills to reach 'distance'.
    You start with a full tank.
   """
    location: int = 0
    n_stops = 0
    last_stop = 0
    max_drive = location + tank

    while max_drive < distance:
        counter = 0

        # Handle the case that stops are depleted before we reach distance
        if len(stops) == 0:
            return -1
        for s in stops:
            if s <= max_drive:
                counter += 1
                last_stop = s
        max_drive = last_stop + tank

        # Handle the case that wi did not reach the next stop
        if counter == 0:
            return -1
        else:
            del stops[0:counter]
            n_stops += 1

    return n_stops


if __name__ == "__main__":
    d, m, _, *stops = map(int, sys.stdin.read().split())
    # data = list(map(int, input().split()))
    # data = [950, 400, 4, 200, 375, 550, 740]
    # data = [500, 200, 4, 100, 200, 300, 400]
    # data = [600, 200, 4, 100, 200, 300, 400]
    # data = [200, 250, 2, 100, 150]
    # data = [10, 3, 4, 1, 2, 5, 9]
    # d, m, n = data[0:3]
    # stops = data[3 : n + 3]
    print(compute_min_refills(d, m, stops))
