from heapq import *


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not len(intervals):
            return 0
        intervals.sort()
        ongoing_meetings = [[intervals[0][1], intervals[0][0]], ]
        max_concurrent_meetings = 1
        for start, end in intervals[1:]:
            if start >= ongoing_meetings[0][0]:
                heapreplace(ongoing_meetings, [end, start])
            else:
                heappush(ongoing_meetings, [end, start])
            max_concurrent_meetings = max(
                max_concurrent_meetings, len(ongoing_meetings))
        return max_concurrent_meetings
