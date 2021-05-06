import os
import sys

# Get number of tests and parameter(s) for the tests from the cli
tests = int(sys.argv[1])
n = int(sys.argv[2])

for i in range(tests):
    print("Test #", str(i))

    # Run the generator gen_tests.py with parameter n and seed i
    os.system(f"python gen_tests.py {str(n)} {str(i)} > z_input.txt")
    # Run the model solution (Note: must not necessarily be in Python)
    os.system("python solution_alt.py < z_input.txt > z_alt.txt")
    # Run the main solution
    os.system("python solution_main.py < z_input.txt > z_main.txt")

    # Read the output of the model solution:
    with open("z_alt.txt") as f:
        alt = f.read()
    print(f" Alt Solution:  {alt}", end=" ")
    # Read the output of the main solution:
    with open("z_main.txt") as f:
        main = f.read()
    print(f"Main Solution: {main}")

    if alt != main:
        break
