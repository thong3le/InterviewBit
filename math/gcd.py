class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        return A if B == 0 else self.gcd(B, A%B)