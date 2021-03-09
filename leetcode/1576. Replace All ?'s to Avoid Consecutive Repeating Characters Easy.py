class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        for i in range(0, len(s)):
            if s[i] == '?':
                while (i > 0 and s[i] == s[i-1]) or (i < len(s)-1 and s[i] == s[i+1]) or s[i] == '?':
                    s[i] = random.choice(string.ascii_lowercase)
        return s
