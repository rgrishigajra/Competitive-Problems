class Solution:
    def candyCrush(self, board):
        crushed = False
        number_of_rows = len(board)
        number_of_columns = len(board[0])
        while True:
            crush_check = False
            for row in range(number_of_rows):
                for column in range(number_of_columns-2):
                    value = abs(board[row][column])
                    if value == 0:
                        continue
                    if (value == abs(
                            board[row][column + 1])) and (value == abs(board[row][column + 2])):
                        board[row][column] = board[row][column +
                                                        1] = board[row][column+2] = -value
                        crush_check = True
            for column in range(number_of_columns):
                for row in range(number_of_rows-2):
                    value = abs(board[row][column])
                    if value == 0:
                        continue
                    if (value == abs(
                            board[row + 1][column])) and (value == abs(board[row + 2][column])):
                        board[row][column] = board[row +
                                                   1][column] = board[row + 2][column] = -value
                        crush_check = True
            if not crush_check:
                break
            for column in range(number_of_columns):
                value = board[0][column]
                if value < 0:
                    board[0][column] = 0
            for column in range(number_of_columns):
                for row in range(1, number_of_rows):
                    value = board[row][column]
                    if value < 0:
                        for iterator in range(row, 0, -1):
                            board[iterator][column] = board[iterator-1][column]
                        board[0][column] = 0
        return board


solution = Solution()
# board = [[110, 5, 112, 113, 114], [210, 211, 5, 213, 214], [310, 311, 3, 313, 314], [410, 411, 412, 5, 414], [
#     5, 1, 512, 3, 3], [610, 4, 1, 613, 614], [710, 1, 2, 713, 714], [810, 1, 2, 1, 1], [1, 1, 2, 2, 2], [4, 1, 4, 4, 1014]]
board = [[5, 5, 5, 3, 2], [3, 4, 3, 2, 4], [
    3, 2, 3, 4, 2], [1, 1, 2, 3, 1], [5, 3, 4, 4, 3]]
solution.candyCrush(board)
