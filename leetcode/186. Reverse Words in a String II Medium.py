class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(s, start, end):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
        reverse(s, 0, len(s)-1)
        itr = 0
        while itr < len(s)-1:
            if s[itr] == ' ':
                itr += 1
                continue
            itr2 = itr
            while itr2 < len(s) and s[itr2] != ' ':
                itr2 += 1
            reverse(s, itr, itr2-1)
            itr = itr2
        return s
