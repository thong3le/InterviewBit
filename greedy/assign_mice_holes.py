class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def mice(self, A, B):
        A.sort()
        B.sort()
        ans = 0
        for a, b in zip(A, B):
            ans = max(ans, abs(a-b))
        return ans
