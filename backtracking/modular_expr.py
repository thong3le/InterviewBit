class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def Mod(self, A, B, C):
        if A == 0:
            return 0
        ans = 1
        while B > 0:
            if B%2:
                ans = (ans * A) % C
            B//=2
            A = (A*A) % C
        return ans