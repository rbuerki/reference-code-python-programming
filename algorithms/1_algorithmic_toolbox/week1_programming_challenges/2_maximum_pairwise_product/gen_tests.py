"""Test generator that accepts a seed as a command line parameter."""

import random
import sys

n_ints = int(sys.argv[1])
max_int = int(sys.argv[2])
myseed = int(sys.argv[3])
random.seed(myseed)

print(n_ints)
print(" ".join([str(random.randint(1, max_int)) for i in range(n_ints)]))
