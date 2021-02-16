class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = 0, 1
        merged = []
        idx = 0
        while len(intervals) > idx and intervals[idx][end] < newInterval[start]:
            merged.append(intervals[idx])
            idx += 1
        while idx < len(intervals) and intervals[idx][start] <= newInterval[end]:
            if intervals[idx][start] < newInterval[start]:
                newInterval[start] = intervals[idx][start]
            if intervals[idx][end] > newInterval[end]:
                newInterval[end] = intervals[idx][end]
            idx += 1
        merged.append(newInterval)
        while idx < len(intervals):
            merged.append(intervals[idx])
            idx += 1
        return merged
