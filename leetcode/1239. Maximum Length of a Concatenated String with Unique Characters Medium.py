
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        m = [0]

        def backtrack(idx, s):
            for itr in range(idx, len(arr)):
                if len(s+arr[itr]) == len(set(s+arr[itr])):
                    m[0] = max(m[0], len(s+arr[itr]))
                    backtrack(itr, s+arr[itr])
        backtrack(0, '')
        return m[0]
