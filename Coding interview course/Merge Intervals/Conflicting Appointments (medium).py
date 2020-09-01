# Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.
def can_attend_all_appointments(intervals):
    start, end = 0, 1
    for i, interval in enumerate(intervals):
        iterator = i + 1
        while iterator < len(intervals):
            if interval[start] >= intervals[iterator][start] and interval[start] <= intervals[iterator][end]:
                return False
            if interval[end] >= intervals[iterator][start] and interval[end] <= intervals[iterator][end]:
                return False
            iterator += 1
    return True


def can_attend_all_appointments(intervals):
    intervals.sort(key=lambda x: x[0])
    start, end = 0, 1
    for i in range(1, len(intervals)):
        if intervals[i][start] < intervals[i-1][end]:
            return False
    return True


def main():
    print("Can attend all appointments: " +
          str(can_attend_all_appointments([[1, 4], [2, 5], [7, 9]])))
    print("Can attend all appointments: " +
          str(can_attend_all_appointments([[6, 7], [2, 4], [8, 12]])))
    print("Can attend all appointments: " +
          str(can_attend_all_appointments([[4, 5], [2, 3], [3, 6]])))


main()
