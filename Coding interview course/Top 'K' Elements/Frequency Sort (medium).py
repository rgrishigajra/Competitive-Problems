from collections import defaultdict
from heapq import *


def sort_character_by_frequency(str):
    char_freq = defaultdict(int)
    for char in str:
        char_freq[char] += 1
    min_heap = []
    for key in char_freq.keys():
        heappush(min_heap, (-char_freq[key], key))
    ans = ''
    while len(min_heap):
        char = heappop(min_heap)
        ans += char[1]*-char[0]
    return ans


def main():

    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("Programming"))
    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("abcbab"))


main()
