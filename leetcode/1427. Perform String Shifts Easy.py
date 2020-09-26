class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        i=0
        for sh in shift:
            if sh[0]:
                i-=sh[1]
            else:
                i+=sh[1]
        i=i%len(s)
        return s[i:]+s[:i]
        