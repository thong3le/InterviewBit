class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def convert(self, A, B):
        if B <= 1:
            return A
        n = len(A)
        result = [''] * B
        row, step = 0, 1
        for c in A:
            result[row] += c
            if row == 0:
                step = 1
            if row == B - 1:
                step = -1
            row += step
        return ''.join(result)