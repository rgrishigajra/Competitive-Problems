# Given an array arr of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. Write a function to return the count of such triplets.
def triplet_with_smaller_sum(arr, target):
    arr.sort()
    count = 0
    for first in range(len(arr)-2):
        left, right = first + 1, len(arr) - 1
        while (left < right):
            if arr[left] + arr[right]+arr[first] < target:
                count += right - left
                left += 1
            else:
                right -= 1
    return count


def main():
    print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
    print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))

main()
