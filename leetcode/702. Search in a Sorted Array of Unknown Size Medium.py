# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        if target > 10000:
            return -1
        l,h = 0,1
        while reader.get(h) < target:
            nl = h
            h += (h-l+1)**2
            l = nl
        while l <= h:
            mid = (l+h)//2
            mid_val = reader.get(mid)
            if mid_val == target:
                return mid
            elif mid_val < target:
                l = mid +1
            else:
                h = mid - 1
        return -1
        