class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minimumTotal(self, A):
        n = len(A)
        dp = list(A[-1])
        for i in range(n-2, -1, -1):
            for j in range(i+1):
                dp[j] = min(dp[j],dp[j+1]) + A[i][j]
        return dp[0]