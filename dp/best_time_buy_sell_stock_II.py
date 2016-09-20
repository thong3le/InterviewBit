class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        N = len(A)
        opt = 0
        for n in range(1, N):
            opt = max(A[n] - A[n-1] + opt, opt)
        return opt