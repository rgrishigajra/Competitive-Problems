# Given a string, find the length of the longest substring in it with no more than K distinct characters.


def longest_substring_with_k_distinct(str, k):
    dic = {}
    result_len = 0
    start_ptr = 0
    for char in range(len(str)):
        if str[char] not in dic:
            if len(dic) < k:
                dic[str[char]] = 1
                result_len = max(result_len, char-start_ptr + 1)
            else:
                del dic[str[start_ptr]]
                while True:
                    start_ptr += 1
                    if str[start_ptr] != str[start_ptr-1]:
                        break
                dic[str[char]] = 1
                result_len = max(result_len, char-start_ptr + 1)
        else:
            result_len = max(result_len, char-start_ptr + 1)
    return result_len


def main():
    print("Length of the longest substr1ing: " +
          str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substr1ing: " +
          str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substr1ing: " +
          str(longest_substring_with_k_distinct("cbbebi", 3)))


main()
