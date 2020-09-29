def find_max_in_bitonic_array(arr):
    l, h = 0, len(arr)-1
    while l < h:
        mid = (l+h)//2
        if arr[mid] > arr[mid+1]:
            h = mid
        else:
            l = mid+1
    return arr[h]


def main():
    print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
    print(find_max_in_bitonic_array([3, 8, 3, 1]))
    print(find_max_in_bitonic_array([1, 3, 8, 12]))
    print(find_max_in_bitonic_array([10, 9, 8]))


main()
