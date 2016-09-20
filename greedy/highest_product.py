class Solution:
    # @param A : list of integers
    # @return an integer
    def maxp3(self, A):
        A.sort()
        return max(A[0] * A[1] * A[-1], A[-1] * A[-2] * A[-3])
