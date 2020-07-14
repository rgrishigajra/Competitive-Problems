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

#below solution instrad of removing the charac from the map, just remembers the last position of the character. So no need to traverse the window start pointer

def non_repeat_substring_efficient(str1):
    window_start = 0
    max_length = 0
    char_index_map = {}
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in char_index_map:
            window_start = max(window_start, char_index_map[right_char]+1)
        char_index_map[right_char]=window_end
        max_length=max(max_length,window_end-window_start+1)
    return max_length


def main():
    print("Length of the longest substring: " +
          str(non_repeat_substring("aabccbb")))
    print("Length of the longest substring: " +
          str(non_repeat_substring("abbbb")))
    print("Length of the longest substring: " +
          str(non_repeat_substring("abccde")))


main()
