class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx1, idx2 = m-1, n-1
        for end in range(m+n-1, -1, -1):
            if idx2 == -1:
                break
            if nums1[idx1] < nums2[idx2] or idx1 == -1:
                nums1[end] = nums2[idx2]
                idx2 -= 1
            else:
                nums1[end] = nums1[idx1]
                idx1 -= 1
