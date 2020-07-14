# Given a string, find the length of the longest substring which has no repeating characters.


def non_repeat_substring(str):
    max_string_length = 0
    current_string_length = 0
    start_ptr = 0
    characters = {}
    for char in range(len(str)):
        if str[char] in characters:
            while start_ptr != char:
                del characters[str[start_ptr]]
                start_ptr += 1
            characters[str[char]] = 1
            max_string_length = max(len(characters), max_string_length)
        else:
            characters[str[char]] = 1
            max_string_length = max(max_string_length, len(characters))
    return max_string_length


def main():
    print("Length of the longest substring: " +
          str(non_repeat_substring("aabccbb")))
    print("Length of the longest substring: " +
          str(non_repeat_substring("abbbb")))
    print("Length of the longest substring: " +
          str(non_repeat_substring("abccde")))


main()
