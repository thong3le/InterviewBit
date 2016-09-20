class Solution:
    # @param A : list of list of integers
    # @return an integer
    def adjacent(self, A):
        A = zip(A[0], A[1])
        n = len(A)
        if n == 0:
            return 0
        M = [0] * (n+1)
        M[1] = max(A[0])
        for i in range(2, n+1):
            M[i] = max(max(A[i-1]) + M[i-2], M[i-1])
        return M[n]
        