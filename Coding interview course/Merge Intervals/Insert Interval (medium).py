# Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the correct position and merge all necessary intervals to produce a list that has only mutually exclusive intervals.


def insert(intervals, new_interval):
    merged = []
    i, start, end = 0, 0, 1
    while i < len(intervals) and intervals[i][end] < new_interval[start]:
        merged.append(intervals[i])
        i += 1
    while i < len(intervals) and new_interval[end] >= intervals[i][start]:
        new_interval[start] = min(new_interval[start], intervals[i][start])
        new_interval[end] = max(new_interval[end], intervals[i][end])
        i += 1
    merged.append(new_interval)
    while i < len(intervals):
        merged.append(intervals[i])
        i += 1
    return merged


def main():
    print("Intervals after inserting the new interval: " +
          str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
    print("Intervals after inserting the new interval: " +
          str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
    print("Intervals after inserting the new interval: " +
          str(insert([[2, 3], [5, 7]], [1, 4])))


main()
