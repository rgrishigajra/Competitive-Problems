class Solution:
    def checkInclusion(self, pattern: str, str1: str) -> bool:
        s = [0 for i in range(26)]
        start = 0
        pat = [0 for i in range(26)]
        for idx, char in enumerate(pattern):
            pat[ord(char)-ord('a')] += 1
        start = 0
        for end, char in enumerate(str1):
            if end - start + 1 > len(pattern):
                s[ord(str1[start])-ord('a')] -= 1
                start += 1
            s[ord(char)-ord('a')] += 1
            if pat == s:
                return True
        return False
