class Solution:
    def minWindow(self, S: str, T: str) -> str:
        ans = ''
        j = 0
        i = 0
        while i < len(S):
            if S[i] == T[j]:
                j += 1
                if j >= len(T):
                    end = i+1
                    j -= 1
                    while j >= 0:
                        if S[i] == T[j]:
                            j -= 1
                        i -= 1
                    i += 1
                    temp = S[i:end]
                    if len(ans) == 0 or len(temp) < len(ans):
                        ans = temp
                    j = 0
            i += 1
        return ans
