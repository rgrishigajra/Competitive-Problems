def find_string_anagrams(str, pattern):
    result_indexes = []
    # TODO: Write your code here
    pat = [0 for i in range(26)]
    s = [0 for i in range(26)]
    start = 0
    for i in pattern:
        pat[ord(i) - ord('a')] += 1
    for end, char in enumerate(str):
        s[ord(char) - ord('a')] += 1
        if end - start + 1 > len(pattern):
            s[ord(str[start])-ord('a')] -= 1
            start += 1
        if s == pat:
            result_indexes.append(start)
    return result_indexes


def main():
    print(find_string_anagrams("ppqp", "pq"))
    print(find_string_anagrams("abbcabc", "abc"))


main()
