# Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.


def max_sub_array_of_size_k(k, arr):
    maxSum = -1
    currentSum = 0
    windowStart = 0
    for windowEnd in range(len(arr)):
        currentSum += arr[windowEnd]
        if windowEnd >= k:
            currentSum -= arr[windowStart]
            windowStart += 1
        maxSum = max(maxSum, currentSum)
    return maxSum


def main():
    print("Maximum sum of a subarray of size K: " +
          str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " +
          str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))


main()
