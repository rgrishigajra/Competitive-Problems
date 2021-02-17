class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        idx = 0
        while idx < len(nums):
            j = nums[idx]-1
            if j >= 0 and j < len(nums) and nums[j] != nums[idx]:
                nums[idx], nums[j] = nums[j], nums[idx]
            else:
                idx += 1
        for idx in range(len(nums)):
            if idx+1 != nums[idx] or nums[idx] == 0:
                return idx+1
        return len(nums)
