from heapq import *


def minimum_cost_to_connect_ropes(ropeLengths):
    result = 0
    min_heap = []
    for i in ropeLengths:
        heappush(min_heap, -i)
    n = len(min_heap)-1
    for itr in range(n):
        rope1 = -min_heap.pop()
        rope2 = -min_heap.pop()
        combined_rope = rope1+rope2
        heappush(min_heap, -combined_rope)
        result += combined_rope
    return result


def main():

    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))


main()
