# We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’. The array has only one duplicate but it can be repeated multiple times. Find that duplicate number without using any extra space. You are, however, allowed to modify the input array.
def find_duplicate(nums):
    itr = 0
    while itr < len(nums):
        if nums[itr] != itr + 1:
            if nums[nums[itr] - 1] != nums[itr]:
                nums[nums[itr] - 1], nums[itr] = nums[itr], nums[nums[itr] - 1]
            else:
                return nums[itr]
        else:
            itr += 1
    return -1


def main():
    print(find_duplicate([1, 4, 4, 3, 2]))
    print(find_duplicate([2, 1, 3, 3, 5, 4]))
    print(find_duplicate([2, 4, 1, 4, 4]))


main()
