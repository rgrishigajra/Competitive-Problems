def can_partition(num):
    total_sum = sum(num) / 2
    if total_sum //1 != total_sum:
        return False
    else:
        total_sum = int(total_sum)
    if int(total_sum) != total_sum:
        return False
    dp = [[0 for c in range(total_sum + 1)] for i in range(len(num))]
    for c in range(total_sum + 1):
        if num[0] == c:
            dp[0][c] = 1
    for i in range(1, len(num)):
        for c in range(1, total_sum + 1):
            if dp[i - 1][c]:
                dp[i][c] = dp[i - 1][c]
            elif c >= num[i]:
                dp[i][c] = dp[i-1][c - num[i]]
    return bool(dp[len(num)-1][total_sum])
def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()
