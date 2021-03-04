def flip_and_invert_image(matrix):
    # TODO: Write your code here.
    c = len(matrix[0])
    for row in range(len(matrix)):
        for col in range((c+1)//2):
            matrix[row][col], matrix[row][c - col -
                                          1] = matrix[row][c - col - 1] ^ 1, matrix[row][col] ^ 1
    return matrix


def main():
    print(flip_and_invert_image([[1, 0, 1], [1, 1, 1], [0, 1, 1]]))
    print(flip_and_invert_image(
        [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))


main()
