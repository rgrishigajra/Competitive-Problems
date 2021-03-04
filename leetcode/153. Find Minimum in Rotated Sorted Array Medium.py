class Solution:
    def findMin(self, arr: List[int]) -> int:
        l, h = 0, len(arr)-1
        while l <= h:
            mid = (l+h)//2
            if mid < h and arr[mid] >= arr[mid + 1]:
                return arr[mid+1]
            if mid > l and arr[mid] < arr[mid-1]:
                return arr[mid]
            if arr[mid] > arr[l]:
                l = mid+1
            else:
                h = mid-1

        return arr[0]
