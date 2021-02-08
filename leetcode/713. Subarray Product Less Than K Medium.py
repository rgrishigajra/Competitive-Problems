class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        start = 0
        curr = 1
        count = 0
        for end, num in enumerate(nums):
            curr = curr*num
            while curr >= k:
                curr /= nums[start]
                start += 1
            count += end-start+1
        return count
