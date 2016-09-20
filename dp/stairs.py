class Solution:
    # @param A : integer
    # @return an integer
    def climbStairs(self, A):
        if A == 1:
            return 1
        if A == 2:
            return 2
        M = [0] * (A + 1)
        M[1] = 1
        M[2] = 2
        for i in range(3, A+1):
            M[i] = M[i-1] + M[i-2]
        return M[A]
