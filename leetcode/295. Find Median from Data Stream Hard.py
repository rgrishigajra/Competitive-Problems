class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap = []  # has all numbers that are greater side
        self.maxHeap = []  # has all numbers that are smaller side

    def addNum(self, num: int) -> None:
        if not self.minHeap or self.minHeap[0] <= num:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)
        if len(self.maxHeap) > len(self.minHeap):
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        elif -len(self.maxHeap)+len(self.minHeap) > 1:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0]-self.maxHeap[0])/2
        return self.minHeap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
