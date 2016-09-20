class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        count = [0] * 32
        for i in range(32):
            for e in A:
                if (e >> i) & 1:
                    count[i] += 1
        res = 0
        for i in range(32):
            if count[i] % 3:
                res |= (1 << i)
        return res