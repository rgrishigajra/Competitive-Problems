class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        zeroes = 0
        start = 0
        max_len = 0
        for end, num in enumerate(A):
            if num == 0:
                zeroes += 1
            while zeroes > K:
                if A[start] == 0:
                    zeroes -= 1
                start += 1
            if max_len < end-start+1:
                max_len = end-start+1
        return max_len
