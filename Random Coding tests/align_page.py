lines = [['hello','world'],['How','areyou','doing'],['please look','and align','to right']]
aligns = ['LEFT','RIGHT','RIGHT']
width = 16
def justifyNewsPaperText(lines,aligns,width):
    ans = ['*'*(width+2)]
    print(ans)
    for line_no,line in enumerate(lines):
        curr_line='*'
        for word_no,word in enumerate(line):
            if len(curr_line)+ len(word) > width:
                if aligns[line_no]=='LEFT':
                    curr_line += ' '*(width-len(curr_line)+1)
                else:
                    curr_line = '*'+' '*(width-len(curr_line)+1)+curr_line[1:]
                curr_line +='*'
                ans.append(curr_line)
                curr_line = '*'

            if curr_line != '*':
                curr_line += ' '+str(word)
            else:
                curr_line += str(word)
        if aligns[line_no]=='LEFT':
            curr_line +=' '*(width-len(curr_line)+1)
        else:
            curr_line = '*'+' '*(width-len(curr_line)+1)+curr_line[1:]
        curr_line+='*'
        ans.append(curr_line)
    ans.append('*'*(width+2))
    return ans
ans = justifyNewsPaperText(lines,aligns,width)
for arr in ans:
    print(arr)