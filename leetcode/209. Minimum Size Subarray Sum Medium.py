class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        max_sum = 0
        min_len = math.inf
        curr_sum = 0
        for end, num in enumerate(nums):
            curr_sum += num
            while curr_sum >= target:
                if min_len > end-start+1:
                    min_len = end-start+1
                curr_sum -= nums[start]
                start += 1
        return min_len if min_len != math.inf else 0
