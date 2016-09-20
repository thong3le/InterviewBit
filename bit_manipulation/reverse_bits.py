class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        n = 32
        for i in range(n//2):
            lo, hi = (A>>i) & 1, (A>>(n-1-i)) & 1
            if lo^hi:
                A ^= (1 << i) | (1 << (n-1-i))
        return A
