class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(s, i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i+1:j]
        lcs = ''
        for i in range(len(s)):
            lcs = max(lcs, helper(s, i, i), helper(s, i, i+1), key=len)
        return lcs
