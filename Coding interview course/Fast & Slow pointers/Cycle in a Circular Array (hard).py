def circular_array_loop_exists(arr):
    idx = 0
    a = len(arr)
    s = set()
    for idx, num in enumerate(arr):
        dir = bool(num >= 0)
        slow = fast = idx
        # te = set()
        while True:
            if fast in s or slow in s:
                break
            slow = (arr[slow] + slow) % a
            temp = (arr[fast] + fast) % a
            fast = (arr[temp] + temp) % a
            # te.update([fast, temp])
            if (dir and (arr[slow] < 0 or arr[fast] < 0)) or (not dir and (arr[slow] >= 0 or arr[fast] >= 0)) or (fast == temp):
                # s = s.union(te)
                break
            if fast == slow:
                return True
    return False

    return False


def main():
    print(circular_array_loop_exists([1, 2, -1, 2, 2]))
    print(circular_array_loop_exists([2, 2, -1, 2]))
    print(circular_array_loop_exists([2, 1, -1, -2]))


main()
