class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for n_itr in range(n+1):
            dp[0][n_itr] = n_itr
        for m_itr in range(m+1):
            dp[m_itr][0] = m_itr
        for n_itr in range(1, n+1):
            for m_itr in range(1, m+1):
                if word1[n_itr-1] != word2[m_itr-1]:
                    prev_step = min(dp[m_itr-1][n_itr], dp[m_itr]
                                    [n_itr-1], dp[m_itr-1][n_itr-1]) + 1
                else:
                    prev_step = dp[m_itr-1][n_itr-1]
                dp[m_itr][n_itr] = prev_step
        return dp[m_itr][n_itr]
