class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort()
        start, end = intervals[0]
        for idx in range(1, len(intervals)):
            if end > intervals[idx][0]:
                return False
            else:
                start, end = intervals[idx]
        return True
