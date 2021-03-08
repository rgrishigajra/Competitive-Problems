class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        start = 0
        max_sum = -math.inf
        curr_sum = -math.inf
        for i in range(len(nums)):
            curr_sum += nums[i]
            if nums[i] > curr_sum:
                curr_sum = nums[i]
            if curr_sum > max_sum:
                max_sum = curr_sum
        return max_sum
