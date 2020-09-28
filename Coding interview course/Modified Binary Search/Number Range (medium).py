def find_range(arr, key):
    result = [- 1, -1]
    result[0] = binary_search(arr, key, True)
    if result[0] != -1:
        result[1] = binary_search(arr, key, False)
    return result


def binary_search(arr, key, find_start_index):
    l, h = 0, len(arr)-1
    key_index = -1
    while l <= h:
        mid = (h+l) // 2
        if key < arr[mid]:
            h = mid-1
        elif key > arr[mid]:
            l = mid+1
        else:  # key == arr[mid]
            key_index = mid
            if find_start_index:
                h = mid - 1
            else:
                l = mid + 1
    return key_index


def main():
    print(find_range([4, 6, 6, 6, 9], 6))
    print(find_range([1, 3, 8, 10, 15], 10))
    print(find_range([1, 3, 8, 10, 15], 12))


main()
