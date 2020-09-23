import heapq


class SlidingWindowMedian:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def insert(self, num):
        if len(self.min_heap) == 0 or self.min_heap[0] <= num:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)
        while True:
            if len(self.min_heap)-len(self.max_heap) > 1:
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
            elif len(self.min_heap)-len(self.max_heap) < 0:
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
            else:
                break

    def find_median(self):
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0]-self.max_heap[0])/2.
        return self.min_heap[0]/1.0

    def delete(self, num):
        if self.min_heap[0] <= num:
            ind = self.min_heap.index(num)
            self.min_heap[ind] = self.min_heap[-1]
            del self.min_heap[-1]
            # we can use heapify to readjust the elements but that would be O(N),
            # instead, we will adjust only one element which will O(logN)
            if ind < len(self.min_heap):
                heapq._siftup(self.min_heap, ind)
                heapq._siftdown(self.min_heap, 0, ind)
        else:
            ind = self.max_heap.index(-num)
            self.max_heap[ind] = self.max_heap[-1]
            del self.max_heap[-1]
            # we can use heapify to readjust the elements but that would be O(N),
            # instead, we will adjust only one element which will O(logN)
            if ind < len(self.max_heap):
                heapq._siftup(self.max_heap, ind)
                heapq._siftdown(self.max_heap, 0, ind)

    def find_sliding_window_median(self, nums, k):
        result = []
        itr = 0
        while itr < k-1:
            self.insert(nums[itr])
            itr += 1
        while itr < len(nums):
            self.insert(nums[itr])
            result.append(self.find_median())
            self.delete(nums[itr-k+1])
            itr += 1

        return result


def main():

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 2)
    print("Sliding window medians are: " + str(result))

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 3)
    print("Sliding window medians are: " + str(result))


main()
