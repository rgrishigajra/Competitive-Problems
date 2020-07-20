# Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.


def make_squares(arr):
    positive_ptr = len(arr)-1
    negative_ptr = 0
    squares = [0 for x in range(len(arr))]
    ptr = len(squares)-1
    while positive_ptr >= negative_ptr:
        pos_sq, neg_sq = arr[positive_ptr]**2, arr[negative_ptr]**2
        if pos_sq > neg_sq:
            squares[ptr] = pos_sq
            ptr -= 1
            positive_ptr -= 1
        else:
            squares[ptr] = neg_sq
            ptr -= 1
            negative_ptr += 1
    return squares


def main():

    print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
    print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


main()
