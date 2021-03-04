class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, h = 0, len(nums)-1
        while l <= h:
            mid = (l+h)//2
            low, high, midnum = nums[l], nums[h], nums[mid]
            if nums[mid] == target:
                return True
            while l < mid and nums[l] == nums[mid]:  # tricky part
                l += 1
            if nums[mid] >= nums[l]:
                if nums[l] <= target and target < nums[mid]:
                    h = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target and target <= nums[h]:
                    l = mid + 1
                else:
                    h = mid - 1
        return False
