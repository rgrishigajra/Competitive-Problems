def find_permutation(str, pattern):
    print(str, pattern)
    s = [0 for i in range(26)]
    start = 0
    pat = [0 for i in range(26)]
    for idx, char in enumerate(pattern):
        pat[ord(char)-ord('a')] += 1
    start = 0
    for end, char in enumerate(str):
        if end - start + 1 > len(pattern):
            s[ord(str[start])-ord('a')] -= 1
            start += 1
        s[ord(char)-ord('a')] += 1
        if pat == s:
            return True
    return False


def main():
    print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
    print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
    print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
    print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))


main()
