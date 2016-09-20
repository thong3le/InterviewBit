class Solution:
    # @param A : list of integers
    # @return an integer
    def canJump(self, A):
        n = len(A)
        if n <= 1:
            return 1
        pos = n-1
        for i in range(n-2, -1, -1):
            result = False
            if pos <= i + A[i]:
                result = True
                pos = i
        return result
