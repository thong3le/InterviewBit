class Solution:
    # @param A : list of list of integers
    # @return an integer
    def uniquePathsWithObstacles(self, A):
        n, m = len(A), len(A[0])
        dp = [[0] * m for _ in range(n)]
        for j in range(m):
            if A[0][j] == 1:
                break
            dp[0][j] = 1
        for i in range(n):
            if A[i][0] == 1:
                break
            dp[i][0] = 1
        for i in range(1, n):
            for j in range(1, m):
                if A[i][j] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[n-1][m-1]