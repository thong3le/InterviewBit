class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        s = str(A)
        if A < 0:
            A = - int(s[1:][::-1])
        else:
            A = int(s[::-1])
        if abs(A) > 2**31:
            return 0
        return A