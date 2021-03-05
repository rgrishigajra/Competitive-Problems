class Solution:
    def rotate(self, A):
        def transpose(A):
            for i in range(len(A)):
                for j in range(i, len(A)):
                    A[j][i], A[i][j] = A[i][j], A[j][i]

        def reflect(A):
            for i in range(len(A)):
                for j in range(len(A)//2):
                    A[i][j], A[i][len(A)-j-1] = A[i][len(A)-j-1], A[i][j]
        for row in A:
            print(row)
        transpose(A)
        for row in A:
            print(row)
        reflect(A)
        for row in A:
            print(row)
        return A
