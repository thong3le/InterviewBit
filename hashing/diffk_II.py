class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        S = set(A)
        if B == 0:
            return 0 if len(S) == len(A) else 1
        for e in A:
            if e + B in S or e - B in S:
                return 1
        return 0
