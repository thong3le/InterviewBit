class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        if len(A) == 1:
            return ord(A) - ord('A') + 1
        return self.titleToNumber(A[-1]) + 26 * self.titleToNumber(A[:-1])
