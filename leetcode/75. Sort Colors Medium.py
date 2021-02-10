def sortColors(nums) -> None:
    """
        Do not return anything, modify nums in-place instead.
        """
    start = 0
    end = len(nums) - 1
    idx = 0
    while idx <= end:
        if nums[idx] == 0:
            nums[idx], nums[start] = nums[start], nums[idx]
            start += 1
            idx += 1
        elif nums[idx] == 2:
            nums[idx], nums[end] = nums[end], nums[idx]
            end -= 1
        else:
            idx += 1
    print(nums)


sortColors([2,0,1])
