class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = [[0, i] for i in range(300)]

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        idx = timestamp % 300-1
        if self.arr[idx][1] != timestamp:
            self.arr[idx][1] = timestamp
            self.arr[idx][0] = 1
        else:
            self.arr[idx][0] += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        count = 0
        for val, ts in self.arr:
            if timestamp - ts < 300:
                count += val
        return count

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
