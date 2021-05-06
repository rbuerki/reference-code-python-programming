import random
import sys

import algorithm as algo

# Get number of tests and test parameter(s) from the cli
n_tests = int(sys.argv[1])
n_ints = int(sys.argv[2])
max_int = int(sys.argv[3])


def generate_tests(myseed: int, *args):
    """Test generator that accepts test params and a seed. Retruns
    random test cases as input for the algorithm functions.
    """
    random.seed(myseed)

    # TODO Adapt to algorithm
    n_ints, max_int = args
    n = n_ints
    numbers = " ".join([str(random.randint(1, max_int)) for i in range(n_ints)])

    print(n)
    print(numbers)
    return n, numbers


def run_tests(n_tests: int, *args):

    for i in range(n_tests):
        print("Test #", str(i))
        myseed = i

        # TODO: Adapt to test input
        n, numbers = generate_tests(myseed, *args)
        alt = algo.max_pairwise_product_naive(numbers)
        main = algo.max_pairwise_product_fast(numbers)

        print(f" Alt Solution:  {alt}")  # , end=" ") TODO
        print(f"Main Solution: {main}")

        if alt != main:
            AssertionError("ATTENTION: Test not passed!")

    print("\nCongrats, all tests passed!")


if __name__ == "__main__":

    # Get number of tests and test parameter(s) from the cli
    n_tests = int(sys.argv[1])
    n_ints = int(sys.argv[2])
    max_int = int(sys.argv[3])

    run_tests(n_tests, n_ints, max_int)
