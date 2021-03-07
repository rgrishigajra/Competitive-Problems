class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            if matrix[row][-1]>=target:
                break
        l,h=0,len(matrix[0])-1
        while l<=h:
            mid = (l+h)//2
            if matrix[row][mid]==target:
                return True
            if matrix[row][mid]>target:
                h = mid-1
            else:
                l = mid+1
        return False