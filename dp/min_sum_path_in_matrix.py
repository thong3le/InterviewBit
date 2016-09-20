class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minPathSum(self, A):
        n = len(A)
        m = len(A[0])
        row = list(A[0])
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    row[j] += row[j-1]
                elif j == 0:
                    row[j] += A[i][0]
                else:
                    row[j] = min(row[j-1], row[j]) + A[i][j]
        return row[m-1]
