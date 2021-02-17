"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        if not schedule:
            return []
        res = []
        heap = []
        for idx, intervals in enumerate(schedule):
            heapq.heappush(heap, (intervals[0].start, idx, 0))
        _, prev_idx, prev_interval_idx = heap[0]
        prev = schedule[prev_idx][prev_interval_idx]
        while heap:
            curr_start, idx, interval_idx = heapq.heappop(heap)
            curr = schedule[idx][interval_idx]
            if curr.start > prev.end:
                res.append(Interval(prev.end, curr.start))
                prev = curr
            else:
                if curr.end > prev.end:
                    prev.end = curr.end
            if len(schedule[idx])-1 > interval_idx:
                heapq.heappush(
                    heap, (schedule[idx][interval_idx+1].start, idx, interval_idx+1))
        return res
