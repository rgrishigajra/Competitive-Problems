
def search_min_diff_element(arr, key):
    if key < arr[0]:
        return arr[0]
    if key > arr[len(arr) - 1]:
        return arr[len(arr) - 1]
    l, h = 0, len(arr)-1
    while l <= h:
        mid = (l+h)//2
        if arr[mid] == key:
            return arr[mid]
        elif key < arr[mid]:
            h = mid - 1
        else:
            l = mid + 1
    if abs(arr[l]-key) < abs(arr[h]-key):
        return arr[l]
    else:
        return arr[h]


def main():
    print(search_min_diff_element([4, 6, 10], 7))
    print(search_min_diff_element([4, 6, 10], 4))
    print(search_min_diff_element([1, 3, 8, 10, 15], 12))
    print(search_min_diff_element([4, 6, 10], 17))


main()
