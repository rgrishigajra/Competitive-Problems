class Solution:
    def backspaceCompare(self, str1: str, str2: str) -> bool:
        idx = 0
        slow = 0
        str1 = list(str1)
        str2 = list(str2)
        while idx < len(str1):
            if str1[idx] == '#':
                slow -= 1
            else:
                str1[slow] = str1[idx]
                slow += 1
            idx += 1
            slow = max(slow, 0)
        idx2 = 0
        slow2 = 0
        while idx2 < len(str2):
            if str2[idx2] == '#':
                slow2 -= 1
            else:
                str2[slow2] = str2[idx2]
                slow2 += 1
            slow2 = max(slow2, 0)
            idx2 += 1
        idx1, idx2 = 0, 0
        while idx1 < slow or idx2 < slow2:
            if str1[idx1] != str2[idx2]:
                return False
            idx1 += 1
            idx2 += 1
        if slow != slow2:
            return False
        return True
