"""Alternative solution."""

if __name__ == "__main__":
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]

    print(" ".join([str(i * 2) for i in range(input_n)]))
