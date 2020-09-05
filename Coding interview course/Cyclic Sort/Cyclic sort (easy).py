def cyclic_sort(nums):
    itr = 0
    while itr < len(nums):
        print(nums)
        if nums[itr] != itr+1:
            nums[nums[itr]-1], nums[itr] = nums[itr], nums[nums[itr]-1]
        else:
            itr += 1
    return nums


def main():
    print(cyclic_sort([3, 1, 5, 4, 2]))
    print(cyclic_sort([2, 6, 4, 3, 1, 5]))
    print(cyclic_sort([1, 5, 6, 4, 3, 2]))


main()
