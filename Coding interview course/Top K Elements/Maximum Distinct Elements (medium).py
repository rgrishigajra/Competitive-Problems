from collections import defaultdict
from heapq import *

def find_maximum_distinct_elements(nums, k):
    count = 0
    min_freq_heap = []
    freq_list = defaultdict(int)
    for num in nums:
        freq_list[num] += 1
    for key in freq_list.keys():
        if freq_list[key]==1:
            count+=1
        else:
            heappush(min_freq_heap,[freq_list[key],key])
    while len(min_freq_heap)>0 and k >0:
        min_freq_heap[0][0]-=1
        k-=1
        if min_freq_heap[0][0]==1:
            count+=1
            heappop(min_freq_heap)
    return count - k


def main():

    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2)))
    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([3, 5, 12, 11, 12], 3)))
    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2)))


main()
