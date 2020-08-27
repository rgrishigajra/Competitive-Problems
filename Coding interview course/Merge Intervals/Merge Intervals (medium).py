# Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.
from __future__ import print_function


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def takestart(interval):
    return interval.start


def merge(intervals):
    merged = []
    iterator = 0
    intervals.sort(key=takestart)
    while True:
        inserted = 0
        if iterator >= len(intervals):
            break
        for interval in range(len(merged)):
            if intervals[iterator].start >= merged[interval].start and intervals[iterator].start <= merged[interval].end:
                inserted = 1
                if intervals[iterator].end > merged[interval].end:
                    merged[interval].end = intervals[iterator].end
                    break
        if not inserted:
            merged.append(intervals[iterator])
        iterator += 1
    return merged


def main():
    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        i.print_interval()
    print()


main()
