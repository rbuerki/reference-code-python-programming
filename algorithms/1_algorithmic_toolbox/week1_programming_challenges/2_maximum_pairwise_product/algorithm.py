# python3


def max_pairwise_product_naive(numbers):
    numbers = [int(x) for x in numbers.split()]
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product, numbers[first] * numbers[second])

    return max_product


def max_pairwise_product_fast(numbers):
    numbers = [int(x) for x in numbers.split()]
    n = len(numbers)
    index_1 = 0
    for index in range(n):
        if numbers[index] > numbers[index_1]:
            index_1 = index

    if index_1 == 0:
        index_2 = 1
    else:
        index_2 = 0

    for index in range(n):
        if index != index_1:
            if numbers[index] > numbers[index_2]:
                index_2 = index

    max_product = numbers[index_1] * numbers[index_2]

    return max_product


if __name__ == "__main__":
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
