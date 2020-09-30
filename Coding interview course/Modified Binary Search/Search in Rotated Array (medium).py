def search_rotated_array(arr, key):
    l, h = 0, len(arr)-1
    while l <= h:
        mid = (l+h)//2
        if arr[mid] == key:
            return mid
        if arr[mid] >= arr[l]:
            if key < arr[mid] and key > arr[l]:
                h = mid -1 
            else:
                l = mid + 1
        else:
            if key > arr[mid] and key < arr[h]:
                l = mid + 1
            else:
                h = mid -1
    return mid


def main():
    print(search_rotated_array([10, 15, 1, 3, 8], 15))
    print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))


main()
