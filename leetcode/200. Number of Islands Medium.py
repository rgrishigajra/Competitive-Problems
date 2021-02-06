class Solution:
    def numIslandsdfs(self, grid: List[List[str]]) -> int:
        def dfs(row, col):
            if row < len(grid) and row > -1 and col > -1 and col < len(grid[0]):
                if grid[row][col] != '1':
                    return
                grid[row][col] = '0'
                dfs(row-1, col)
                dfs(row+1, col)
                dfs(row, col-1)
                dfs(row, col+1)
            return
        if not grid:
            return 0
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    dfs(row, col)
                    count += 1
        return count

    def numIslandsbfs(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m, n, count = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    stack = [(i, j)]
                    for ii, jj in stack:
                        if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] == "1":
                            grid[ii][jj] = "2"
                            stack.extend(
                                [(ii+1, jj), (ii-1, jj), (ii, jj-1), (ii, jj+1)])
        return count
