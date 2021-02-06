class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        visited = [[1 for _ in range(n)] for _ in range(m)]
        for row in range(1,m):
            for col in range(1,n):
                visited[row][col] = visited[row-1][col] + visited[row][col-1]
        return visited[-1][-1]

    def uniquePathsMath(self, m: int, n: int) -> int:
        return math.factorial(m+n -2)//(m-1) //(n-1)
                    