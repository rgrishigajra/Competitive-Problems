class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        multi = False
        line = ''
        for block in source:
            itr = 0
            while itr < len(block):
                char = block[itr]
                if itr < len(block)-1:
                    nex = block[itr+1]
                    if multi and char == '*' and nex == '/':
                        char = ''
                        multi = False
                        itr += 1
                    elif not multi and char == '/':
                        if nex == '*':
                            multi = True
                            itr += 1
                        elif nex == '/':
                            break
                itr += 1
                if not multi:
                    line += char
            if not multi and line != '':
                res.append(line)
                line = ''
        return res
