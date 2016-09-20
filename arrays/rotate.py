class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        n = len(A)
        for i in range(n//2):
            for j in range(i, n-1-i):
                A[i][j], A[n-1-j][i], A[n-1-i][n-1-j], A[j][n-1-i] = A[n-1-j][i], A[n-1-i][n-1-j], A[j][n-1-i], A[i][j]
        return A