class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        m, n = len(A[0]), len(A)
        for i in range(m):
            for j in range(1, n):
                if i >= len(A[j]) or A[0][i] != A[j][i]:
                    return A[0][:i]
        return A[0]