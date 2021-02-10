class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        low = 0
        while low < len(nums)-1 and nums[low+1] >= nums[low]:
            low += 1
        if low == len(nums) - 1:
            return 0
        high = len(nums) - 1
        while high > 1 and nums[high-1] <= nums[high]:
            high -= 1

        mini = math.inf
        maxi = -math.inf
        for idx in range(low, high+1):
            if mini > nums[idx]:
                mini = nums[idx]
            if maxi < nums[idx]:
                maxi = nums[idx]
        while low > 0 and nums[low-1] > mini:
            low -= 1
        while high < len(nums)-1 and nums[high+1] < maxi:
            high += 1
        return high - low + 1
