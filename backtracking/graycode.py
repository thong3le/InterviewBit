import math
class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        if A == 1:
            return [0,1]
        S = self.grayCode(A-1)
        result = [s for s in S]
        result.extend([2**(A-1) + s for s in S[::-1]])
        return result

print(Solution().grayCode(3))