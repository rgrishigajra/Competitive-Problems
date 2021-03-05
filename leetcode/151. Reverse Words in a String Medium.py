class Solution:
    def reverseWords(self, s: str) -> str:
        def trim_spaces(s: str) -> list:
            left, right = 0, len(s) - 1
            # remove leading spaces
            while left <= right and s[left] == ' ':
                left += 1

            # remove trailing spaces
            while left <= right and s[right] == ' ':
                right -= 1

            # reduce multiple spaces to single one
            output = []
            while left <= right:
                if s[left] != ' ':
                    output.append(s[left])
                elif output[-1] != ' ':
                    output.append(s[left])
                left += 1

            return output

        s = trim_spaces(s)
        itr = 0
        l = len(s)-1
        while itr < l//2:
            s[itr], s[l-itr] = s[l-itr], s[itr]
            itr += 1
        itr = 0
        while itr < l:
            if s[itr] == ' ':
                itr += 1
                continue
            itr2 = itr
            while itr2 <= l and s[itr2] != ' ':
                itr2 += 1
            itr2 -= 1
            end = itr2
            while itr < itr2:
                s[itr], s[itr2] = s[itr2], s[itr]
                itr += 1
                itr2 -= 1
            itr = end+1
        print(s)
        return ''.join(s)
