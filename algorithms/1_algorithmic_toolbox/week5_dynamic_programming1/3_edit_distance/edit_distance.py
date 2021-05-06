# Uses python3
def edit_distance(s, t):
    # Initialize a 2d lookup-matrix
    dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]

    for i in range(len(s) + 1):
        for j in range(len(t) + 1):
            # Fill first row
            if i == 0:
                dp[i][j] = j
            # Fill first column
            elif j == 0:
                dp[i][j] = i
            # Fill rest: if values are the same
            elif s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            # Fill rest: if values differ
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1
                )
    return dp[len(s)][len(t)]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
    # print(edit_distance("editing", "distance"))
