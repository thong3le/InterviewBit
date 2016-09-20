class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        if len(A) == 0:
            return 0
        p = 0
        m = A[0]
        for i in range(1, len(A)):
            m = min(m, A[i])
            p = max(p, A[i] - m)
        return p
