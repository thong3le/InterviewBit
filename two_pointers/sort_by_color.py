class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        n = len(A)
        r, b = 0, n-1
        i = 0
        while i <= b:
            if A[i] == 0:
                A[r], A[i] = A[i], A[r]
                r += 1
            elif A[i] == 2:
                A[b], A[i] = A[i], A[b]
                b -= 1
                i -= 1
            i += 1
        return A