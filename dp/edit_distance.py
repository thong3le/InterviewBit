class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A, B):
        n, m = len(A), len(B)
        M = [[0] * (m+1) for _ in range(n+1)]
        for i in range(n+1):
            M[i][0] = i
        for i in range(m+1):
            M[0][i] = i
        for i in range(1, n+1):
            for j in range(1, m+1):
                if A[i-1] == B[j-1]:
                    M[i][j] = M[i-1][j-1]
                else:
                    M[i][j] = min(1 + M[i-1][j-1], 1 + M[i-1][j], 1 + M[i][j-1])
        return M[n][m]

A = "aac"
B = "abac"
print(Solution().minDistance(A, B))
