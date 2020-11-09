class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        if not intervals:
            return []
        start, end = intervals[0]
        ans = []
        for interval_start, interval_end in intervals[1:]:
            if end >= interval_start:
                end = max(interval_end, end)
            else:
                ans.append([start, end])
                start = interval_start
                end = interval_end
        ans.append([start, end])
        return ans
