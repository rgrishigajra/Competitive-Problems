class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums)-1
        while l <= h:
            mid = (l+h)//2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[l]:
                if nums[mid] > target and target >= nums[l]:
                    h = mid - 1
                else:
                    l = mid+1
            else:
                if nums[mid] < target and nums[h] >= target:
                    l = mid+1
                else:
                    h = mid-1
        return -1
