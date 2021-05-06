# Uses python3
import sys

# def get_majority_element(a, left, right):
#     if left == right:
#         return -1
#     if left + 1 == right:
#         return a[left]
#     #write your code here
#     return -1


# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n, *a = list(map(int, input.split()))
#     if get_majority_element(a, 0, n) != -1:
#         print(1)
#     else:
#         print(0)


def get_majority_element_raph(a: list):
    """My implementation using a hash-map.
    Time complexity = O(1), Space complexcity = O(n).
    """
    hash = {}
    for key in a:
        if key in hash:
            hash[key] += 1
        else:
            hash[key] = 1
    for key in hash:
        if hash[key] > len(a) / 2:
            return 1
    return 0


if __name__ == "__main__":
    input = sys.stdin.read()
    # input = "5 1 2 1 2 1 3"
    n, *a = list(map(int, input.split()))
    print(get_majority_element_raph(a))
