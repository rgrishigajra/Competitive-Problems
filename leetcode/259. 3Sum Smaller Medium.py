class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        for idx, num1 in enumerate(nums):
            left, right = idx+1, len(nums)-1
            while left < right:
                curr = num1+nums[left]+nums[right]
                if curr < target:
                    count += right - left
                    left += 1
                else:
                    right -= 1
        return count
