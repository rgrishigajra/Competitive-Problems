class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums2, nums1 = nums1, nums2
        x = len(nums1)
        y = len(nums2)
        l = 0
        h = len(nums1)
        m = math.inf
        while l <= h:
            px = (l+h)//2
            py = (x+y+1)//2 - px
            lx = -m if px <= 0 else nums1[px-1]
            rx = m if px >= x else nums1[px]
            ly = -m if py <= 0 else nums2[py-1]
            ry = m if py >= y else nums2[py]
            if lx <= ry and ly <= rx:
                if (x+y) % 2 == 0:
                    return (max(lx, ly)+min(rx, ry))/2
                else:
                    return (max(lx, ly))
            if lx > ry:
                h = h - 1
            else:
                l = l + 1
