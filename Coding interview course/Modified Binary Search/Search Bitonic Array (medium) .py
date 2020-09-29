#  Given a Bitonic array, find if a given ‘key’ is present in it
# Problem Challenge 1


def search_bitonic_array(arr, key):
    max_key = find_max(arr, key)
    key_index = binary_search(arr, key, 0, max_key)
    if key_index != -1:
        return key_index
    return binary_search(arr, key, max_key+1, len(arr)-1)


def find_max(arr, key):
    l, h = 0, len(arr)-1
    while l < h:
        mid = (l+h)//2
        if arr[mid] > arr[mid+1]:
            h = mid
        else:
            l = mid + 1
    return l


def binary_search(arr, key, l, h):
    while l <= h:
        mid = (l+h) // 2
        if key == arr[mid]:
            return mid
        if arr[l] < arr[h]:  # ascending order
            if key < arr[mid]:
                h = mid - 1
            else:
                l = mid + 1
        else:
            if key > arr[mid]:
                h = mid - 1
            else:
                l = mid + 1
    return -1


def main():
    print(search_bitonic_array([1, 3, 8, 4, 3], 4))
    print(search_bitonic_array([3, 8, 3, 1], 8))
    print(search_bitonic_array([1, 3, 8, 12], 12))
    print(search_bitonic_array([10, 9, 8], 10))


main()
