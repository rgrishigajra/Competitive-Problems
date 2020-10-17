from heapq import *


def find_sum_of_elementsnlogn(nums, k1, k2):
    min_heap = []
    for num in nums:
        heappush(min_heap, num)
    result_sum = 0
    while k1 > 0:
        heappop(min_heap)
        k1 -= 1
        k2 -= 1
    while k2 > 1:
        result_sum += heappop(min_heap)
        k2 -= 1
    return result_sum


def find_sum_of_elements(nums, k1, k2):
    result_sum = 0
    max_heap = []
    for num in nums:
        heappush(max_heap, -num)
        if len(max_heap) >= k2:
            heappop(max_heap)
    result_sum = 0
    for i in range(k2-k1-1):
        result_sum -= heappop(max_heap)
    return result_sum


def main():

    print("Sum of all numbers between k1 and k2 smallest numbers: " +
          str(find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6)))
    print("Sum of all numbers between k1 and k2 smallest numbers: " +
          str(find_sum_of_elements([3, 5, 8, 7], 1, 4)))


main()
