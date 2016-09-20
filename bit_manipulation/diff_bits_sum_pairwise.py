class Solution:
    # @param A : list of integers
    # @return an integer
    def cntBits(self, A):
        n = len(A)
        ans = 0
        for i in range(32):
            ones = 0
            for a in A:
                if a & (1 << i):
                    ones += 1
            ans = (ans + 2*ones*(n-ones)) % 1000000007
        return ans