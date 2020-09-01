def merge(intervals_a, intervals_b):
    result = []
    a, b, start, end = 0, 0, 0, 1
    while a < len(intervals_a) and b < len(intervals_b):
        is_intersection = intervals_a[a][start] <= intervals_b[b][start] and intervals_a[a][end] >= intervals_b[b][
            start] or intervals_a[a][start] >= intervals_b[b][start] and intervals_a[a][start] <= intervals_b[b][end]
        if is_intersection:
            result.append([max(intervals_a[a][start], intervals_b[b][start]), min(
                intervals_a[a][end], intervals_b[b][end])])
        if intervals_a[a][end] > intervals_b[b][end]:
            b += 1
        else:
            a += 1
    return result


def main():
    print("Intervals Intersection: " +
          str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
    print("Intervals Intersection: " +
          str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


main()
