from heapq import *


class KthLargestNumberInStream:
    def __init__(self, nums, k):
        # TODO: Write your code here
        self.k = k
        self.min_heap = []
        for num in range(k):
            heappush(self.min_heap, nums[num])
        for num in range(k, len(nums)):
            if self.min_heap[0] < nums[num]:
                heappushpop(self.min_heap, nums[num])

    def add(self, num):
        if self.min_heap[0] < num:
            heappushpop(self.min_heap, num)
        return self.min_heap[0]


def main():

    kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
    print("4th largest number is: " + str(kthLargestNumber.add(6)))
    print("4th largest number is: " + str(kthLargestNumber.add(13)))
    print("4th largest number is: " + str(kthLargestNumber.add(4)))


main()
