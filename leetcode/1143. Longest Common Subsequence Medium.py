class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        t1 = len(text1)
        t2 = len(text2)
        dp = [[0 for _ in range(t2+1)] for k in range(t1+1)]
        for c1 in range(1, t1+1):
            for c2 in range(1, t2+1):
                if text1[c1-1] == text2[c2-1]:
                    dp[c1][c2] = 1+dp[c1-1][c2-1]
                else:
                    dp[c1][c2] = max(dp[c1-1][c2], dp[c1][c2-1])
        return dp[t1][t2]
