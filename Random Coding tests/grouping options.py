# Python3 implementation to count the
# number of ways to divide N in
# groups such that each group
# has K number of elements

# DP Table
dp = [[[-1 for i in range(201)] for j in range(201)]for j in range(201)]

# Function to count the number
# of ways to divide the number N
# in groups such that each group
# has K number of elements


def calculate(pos, prev, left, k):

    # Base Case
    if (pos == k):
        if (left == 0):
            return 1
        else:
            return 0

    # if N is divides completely
    # into less than k groups
    if (left == 0):
        return 0

    # If the subproblem has been
    # solved, use the value
    if (dp[pos][prev][left] != -1):
        return dp[pos][prev][left]

    answer = 0

    # put all possible values
    # greater equal to prev
    for i in range(prev, left+1):
        answer += calculate(pos + 1, i,
                            left - i, k)
    dp[pos][prev][left] = answer
    return dp[pos][prev][left]

# Function to count the number of
# ways to divide the number N in groups


def countWaystoDivide(n, k):

    # Intialize DP Table as -1
    for i in range(500):
        for j in range(500):
            for l in range(500):
                dp[i][j][l] = -1

    return calculate(0, 1, n, k)


def test(n,k):
    # dp = [[[-1 for i in range(201)] for j in range(201)]for j in range(201)]
    dp = [[0 for _ in range(k+1)]for _ in range(n+1)]
    dp[0][0]=1
    for i in range(1,n+1):
        for j in range(1,min(i,k)+1):
            dp[i][j]=dp[i - j][j] + dp[i - 1][j - 1]
    return dp[n][k]

# Driver Code
if __name__ == '__main__':
    N = 200
    K = 10

    print(test(N, K))

# This code is contributed by Rajput-Ji


