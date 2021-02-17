def find_corrupt_numbers(nums):
    # TODO: Write your code here
    idx = 0
    while idx < len(nums):
        j = nums[idx]-1
        print(j, idx)
        if nums[idx] != nums[j]:
            nums[idx], nums[j] = nums[j], nums[idx]
        else:
            idx += 1
    for idx, num in enumerate(nums):
        if idx+1 != num:
            print(nums)
            return [idx+1, num]
    return [-1, -1]
