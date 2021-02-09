def backspace_compare(str1, str2):
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
    idx2 = 0
    slow2 = 0
    while idx2 < len(str2):
        if str2[idx2] == '#':
            slow2 -= 1
        else:
            str2[slow2] = str2[idx2]
            slow2 += 1
        idx2 += 1
    idx1, idx2 = 0, 0
    # if slow != slow2:
    #   return False
    print(str1[:slow], str2[:slow2])
    while idx1 < slow and idx2 < slow2:
        print(str1[idx1], str2[idx2])
        if str1[idx1] != str2[idx2]:
            return False
        idx1 += 1
        idx2 += 1
    return True


print(backspace_compare('xywrrmu#p','xywrrmp'))
