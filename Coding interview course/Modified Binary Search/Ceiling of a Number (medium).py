def search_ceiling_of_a_number(arr, key):
    l, h = 0, len(arr)-1
    if arr[h] < key:
        return -1
    while l <= h:
        mid = (l+h) // 2
        if key == arr[mid]:
            return mid
        if key <= arr[mid]:
            h = mid-1
        else:
            l = mid + 1
    return l


def main():
    print(search_ceiling_of_a_number([4, 6, 10], 6))
    print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
    print(search_ceiling_of_a_number([4, 6, 10], 17))
    print(search_ceiling_of_a_number([4, 6, 10], -1))


main()
