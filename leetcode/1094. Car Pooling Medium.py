from heapq import *


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        current_trip = [[trips[0][2], trips[0][1], trips[0][0]], ]
        passengers_traveling = trips[0][0]
        for passengers, start, end in trips[1:]:
            while len(current_trip) and current_trip[0][0] <= start:
                [old_end, old_start, old_passenegers] = heappop(current_trip)
                passengers_traveling -= old_passenegers
            heappush(current_trip, [end, start, passengers])
            passengers_traveling += passengers
            if passengers_traveling > capacity:
                return False
        return True


