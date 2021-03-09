class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        def helper(t, b, l, r):
            for col in range(l, r+1):
                yield (t, col)
            for row in range(t+1, b+1):
                yield (row, r)
            if t < b and l < r:
                for col in range(r-1, l, -1):
                    yield (b, col)
                for row in range(b, t, -1):
                    yield (row, l)
        if n == 0:
            return []
        matrix = [[0 for _ in range(n)] for i in range(n)]
        t, b = 0, n - 1
        l, r = 0, n - 1
        itr = 1
        while t <= b and l <= r:
            for i, c in helper(t, b, l, r):
                matrix[i][c] = itr
                itr += 1
            t += 1
            b -= 1
            l += 1
            r -= 1
        return matrix
