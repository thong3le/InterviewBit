class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        s = []
        while A > 0:
            d, r = divmod(A-1, 26)
            s.append(chr(ord('A') + r))
            A = d
        return ''.join(s[::-1])