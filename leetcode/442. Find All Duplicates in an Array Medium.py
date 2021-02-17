class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        idx = 0
        while idx < len(nums):
            j = nums[idx] - 1
            if nums[j] != nums[idx]:
                nums[idx], nums[j] = nums[j], nums[idx]
            else:
                idx += 1
        ans = []
        for idx, num in enumerate(nums):
            if idx+1 != num:
                ans.append(num)
        return ans
