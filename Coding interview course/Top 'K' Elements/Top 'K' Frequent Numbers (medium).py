from collections import defaultdict
from heapq import *


def find_k_frequent_numbers(nums, k):
    topNumbers = []
    freq = defaultdict(int)
    for num in nums:
        freq[num] += 1
    for itr in freq.keys():
        heappush(topNumbers, (freq[itr], itr))
        if len(topNumbers) > k:
            heappop(topNumbers)
    ans = [*map(lambda x: x[1], topNumbers)]
    return ans


def main():

    print("Here are the K frequent numbers: " +
          str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

    print("Here are the K frequent numbers: " +
          str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()
