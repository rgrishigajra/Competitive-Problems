from heapq import *
from collections import defaultdict


def rearrange_string(str):
    max_heap = []
    feq_map = defaultdict(int)
    for char in str:
        feq_map[char] += 1
    for key in feq_map.keys():
        heappush(max_heap, [-feq_map[key], key])
    [prev_char_freq, prev_char] = heappop(max_heap)
    result_str = ''
    while max_heap:
        result_str += prev_char
        prev_char_freq += 1
        [next_char_freq, next_char] = heappop(max_heap)
        if prev_char_freq < 0:
            heappush(max_heap, [prev_char_freq, prev_char])
        prev_char_freq, prev_char = next_char_freq, next_char
    if prev_char_freq == -1:
        return result_str+prev_char
    else:
        return '' 


def main():
    print("Rearranged string:  " + rearrange_string("aappp"))
    print("Rearranged string:  " + rearrange_string("Programming"))
    print("Rearranged string:  " + rearrange_string("aapa"))


main()
