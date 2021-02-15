class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        for idx, char in enumerate(haystack):
            if char != needle[0]:
                continue
            if idx >= len(haystack)-len(needle)+1:
                break
            flag = False
            idx1 = idx
            for n_idx, need in enumerate(needle):
                char = haystack[idx1]
                if char != need:
                    flag = True
                    break
                idx1 += 1
            if not flag:
                return idx
        return -1


class Solution:
    def strStr(self, s: str, p: str) -> int:
        if not p:
            return 0

        if len(p) > len(s):
            return -1

        lps = build_lps(p)
        i = j = 0
        while i < len(s):
            if s[i] == p[j]:
                i += 1
                j += 1
                if j == len(p):
                    return i - len(p)
            else:
                if j > 0:
                    j = lps[j - 1]
                else:
                    i += 1

                return -1

        def build_lps(s: str) -> List[int]:
            lps = [0] * len(s)
            j, i = 0, 1
            while i < len(s):
                if s[i] == s[j]:
                    lps[i] = j + 1
                    i += 1
                    j += 1
                else:
                    if j > 0:
                        j = lps[j-1]
                    else:
                        i += 1

            return lps
