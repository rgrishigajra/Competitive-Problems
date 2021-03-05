class Solution:
    def isValid(self, s: str) -> bool:
        ma = {')': '(', '}': '{', ']': '['}
        itr = 0
        stack = []
        while itr < len(s):
            if s[itr] in ma:
                if not stack or stack[-1] != ma[s[itr]]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(s[itr])
            itr += 1
        return True if not stack else False
