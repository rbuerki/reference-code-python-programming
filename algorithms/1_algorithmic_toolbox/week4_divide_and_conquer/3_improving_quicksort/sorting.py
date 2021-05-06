# Uses python3
import sys
import random


def randomized_quick_sort(a):
    if len(a) < 2:
        return a

    low, same, high = [], [], []
    pivot = a[random.randint(0, len(a) - 1)]

    for x in a:
        if x < pivot:
            low.append(x)
        elif x == pivot:
            same.append(x)
        else:
            high.append(x)

    return randomized_quick_sort(low) + same + randomized_quick_sort(high)


if __name__ == "__main__":
    input = sys.stdin.read()
    # input = "5 3 6 3 3 0"
    n, *a = list(map(int, input.split()))
    result = randomized_quick_sort(a)
    for x in result:
        print(x, end=" ")


# def partition3(a, l, r):
#     # write your code here
#     pass


# def partition2(a, l, r):
#     x = a[l]
#     j = l
#     for i in range(l + 1, r + 1):
#         if a[i] <= x:
#             j += 1
#             a[i], a[j] = a[j], a[i]
#     a[l], a[j] = a[j], a[l]
#     return j


# def randomized_quick_sort(a, l, r):
#     if l >= r:
#         return
#     k = random.randint(l, r)
#     a[l], a[k] = a[k], a[l]
#     # use partition3
#     m = partition2(a, l, r)
#     randomized_quick_sort(a, l, m - 1)
#     randomized_quick_sort(a, m + 1, r)


# if __name__ == "__main__":
#     input = sys.stdin.read()
#     n, *a = list(map(int, input.split()))
#     randomized_quick_sort(a, 0, n - 1)
#     for x in a:
#         print(x, end=" ")
