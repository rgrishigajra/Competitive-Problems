from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        self.ongoing_travels = defaultdict(lambda: ('', 0))
        self.journey_details = defaultdict(lambda: [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.ongoing_travels[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        (start_station, starting_time) = self.ongoing_travels.pop(id)
        self.journey_details[(start_station, stationName)
                             ][0] += t-starting_time
        self.journey_details[(start_station, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, no_trips = self.journey_details[(startStation, endStation)]
        return total/no_trips


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
