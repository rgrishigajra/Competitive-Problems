class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x1, x2 = 0, 0
        for i in range(len(nums)+1):
            x1 = x1 ^ i
        for i in nums:
            x2 = x2 ^ i
        return x1 ^ x2
