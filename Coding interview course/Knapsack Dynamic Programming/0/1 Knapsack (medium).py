from __future__ import print_function


def solve_knapsack(profits, weights, capacity):
    # basic checks
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0

    dp = [[0 for x in range(capacity+1)] for y in range(n)]
    for c in range(0, capacity+1):
        if weights[0] <= c:
            dp[0][c] = profits[0]
    for i in range(1, n):
        for c in range(1, capacity+1):
            i_profit = 0
            if c >= weights[i]:
                i_profit = dp[i - 1][c-weights[i]]+profits[i]
            not_i_profit = dp[i-1][c]
            dp[i][c] = max(i_profit, not_i_profit)
    print_selected_elements(dp, weights, profits, capacity)
    return dp[n - 1][capacity]


def print_selected_elements(dp, weights, profits, capacity):
    selected_list = []
    n = len(profits)
    c = capacity
    total_profit = dp[n-1][capacity]
    for i in range(n-1, 0, -1):
        if dp[i][c] != dp[i-1][c]:
            selected_list.append([i, weights[i], profits[i]])
            total_profit -= profits[i]
            c = c - weights[i]
    # since we cant have -1 line for first column to check and compare
    if total_profit != dp[n-1][capacity]:
        selected_list.append([0, weights[0], profits[0]])
    print(selected_list)


def solve_knapsack_N_complexity(profits, weights, capacity):
    n = len(profits)
    dp = [0 for i in range(capacity +1)]
    for i in range(n):
        for c in range(capacity, -1, -1):
            i_profit = 0
            if weights[i] <= c:
                i_profit = dp[c-weights[i]]+profits[i]
            dp[c]=max(dp[c],i_profit)
    
    return dp[capacity]

def main():
    print("Total knapsack profit: " +
          str(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7)))
    print("Total knapsack profit: " +
          str(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6)))


main()
