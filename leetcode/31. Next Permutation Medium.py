class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-1
        # find first increasing number from last
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        # nums[i-1] is that number
        # swap all ahead
        j = i
        k = len(nums)-1
        while j < k:
            nums[j], nums[k] = nums[k], nums[j]
            j += 1
            k -= 1
        if i > 0:
            k = i
            i -= 1
            # find the first number greater than our selected number
            while nums[k] <= nums[i]:
                k += 1
            nums[k], nums[i] = nums[i], nums[k]
