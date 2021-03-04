class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, h = 0, len(arr)-1
        while l < h:
            mid = (l+h)//2
            if arr[mid] > arr[mid+1]:
                h = mid
            else:
                l = mid + 1
        return l
