class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            'I':   1,
            'V':   5,
            'X':  10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        total = 0 if not s else mapping[s[-1]]
        itr = len(s)-1
        while itr >= 0:
            if itr < len(s)-1 and mapping[s[itr]] >= mapping[s[itr+1]]:
                total += mapping[s[itr]]
            elif itr < len(s)-1 and mapping[s[itr]] < mapping[s[itr+1]]:
                total -= mapping[s[itr]]
            itr -= 1
        return total
