class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        return bin(int(A, 2) + int(B, 2))[2:]