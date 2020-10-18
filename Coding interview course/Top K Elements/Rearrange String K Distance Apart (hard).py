from heapq import *
from collections import defaultdict


def reorganize_string(str, k):
    if k <= 1:
        return str

    max_heap = []
    feq_map = defaultdict(int)
    for char in str:
        feq_map[char] += 1
    for key in feq_map.keys():
        heappush(max_heap, [-feq_map[key], key])
    # [prev_char_freq, prev_char] = heappop(max_heap)
    que = []
    result_str = ''
    while max_heap:
        [next_char_freq, next_char] = heappop(max_heap)
        result_str += next_char
        next_char_freq += 1
        que.append([next_char_freq, next_char])
        if len(que) >= k:
            [next_char_freq, next_char] = que.pop(0)
            if next_char_freq < 0:
                heappush(max_heap, [next_char_freq, next_char])
    if len(str) != len(result_str):
        return ''
    return result_str


def main():
    print("Reorganized string: " + reorganize_string("Programming", 3))
    print("Reorganized string: " + reorganize_string("mmpp", 2))
    print("Reorganized string: " + reorganize_string("aab", 2))
    print("Reorganized string: " + reorganize_string("aapa", 3))


main()
