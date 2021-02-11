class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeroes = 0
        for idx in range(len(nums)):
            if nums[idx] != 0:
                nums[zeroes] = nums[idx]
                zeroes += 1
        while zeroes < len(nums):
            nums[zeroes] = 0
            zeroes += 1
