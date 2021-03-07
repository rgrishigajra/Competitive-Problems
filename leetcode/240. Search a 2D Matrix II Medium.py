class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_itr = len(matrix)-1
        col_itr = 0
        while row_itr >= 0 and col_itr < len(matrix[0]):
            if matrix[row_itr][col_itr] == target:
                return True
            if matrix[row_itr][col_itr] > target:
                row_itr -= 1
            else:
                col_itr += 1
        return False
