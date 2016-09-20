class Solution:
    # @param A : string
    # @return an integer
    def cnttrue(self, A):
        n = (len(A) + 1)//2
        M = [[0]*n for _ in range(n)]
        S = [[0]*n for _ in range(n)]
        for i in range(n):
            S[i][i] = 1
            M[i][i] = 1 if A[2*i] == 'T' else 0
        for k in range(1, n):
            for i in range(n-k):
                j = i + k
                for p in range(i, j):
                    S[i][j] = (S[i][j] + (S[i][p] * S[p+1][j])) % 1003
                    if A[2*p+1] == '|':
                        M[i][j] = M[i][j] + M[i][p] * S[p+1][j]
                        M[i][j] = M[i][j] + (S[i][p] - M[i][p]) * M[p+1][j]
                    elif A[2*p+1] == '&':
                        M[i][j] = M[i][j] + M[i][p] * M[p+1][j]
                    else:
                        M[i][j] = M[i][j] + M[i][p] * (S[p+1][j] - M[p+1][j])
                        M[i][j] = M[i][j] + (S[i][p] - M[i][p]) * M[p+1][j]
                M[i][j] = M[i][j] % 1003
        return M[0][n-1]


A = 'T|F&T^F'
print(Solution().cnttrue(A))