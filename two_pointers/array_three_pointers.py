class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, A, B, C):
        i, j, k = 0, 0, 0
        ans = float('inf')
        while i < len(A) and j < len(B) and k < len(C):
            t = min(A[i], B[j], C[k])
            ans = min(ans, max(A[i], B[j], C[k]) - t)
            if A[i] == t:
                i += 1
            elif B[j] == t:
                j += 1
            else:
                k += 1
        return ans