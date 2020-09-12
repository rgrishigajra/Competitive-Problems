#  Design a class to calculate the median of a number stream. The class should have the following two methods:
import heapq


class MedianOfAStream:
    maxHeap = []
    minHeap = []

    def insert_num(self, num):
        if len(self.minHeap) == 0 or self.minHeap[0] >= num:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)
        if len(self.minHeap)-len(self.maxHeap) > 1:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        elif len(self.minHeap)-len(self.maxHeap) < 0:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        return

    def find_median(self):
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0])/2
        return self.minHeap[0]


def main():
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(1)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(5)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(4)
    print("The median is: " + str(medianOfAStream.find_median()))


main()
