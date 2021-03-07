class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums)-1
        while l < h:
            mid = (l+h)//2
            if nums[l] == nums[mid] == nums[h]:
                l += 1
                h -= 1
            elif nums[mid] <= nums[h]:
                h = mid
            else:
                l = mid+1
        return nums[l]
