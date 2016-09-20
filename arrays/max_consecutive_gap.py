import math
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        n = len(A)
        minE = min(A)
        maxE = max(A)
        if len(A) <= 1 or minE == maxE:
            return 0
        gap = int(math.ceil(float(maxE-minE)/(n-1)))
        bucket = [[None, None] for _ in range((maxE - minE)//gap + 1)]
        for e in A:
            b = bucket[(e-minE)//gap]
            b[0] = e if b[0] is None else min(b[0], e)
            b[1] = e if b[1] is None else max(b[1], e)
        bucket = [b for b in bucket if b[0] is not None]
        return max(bucket[i][0] - bucket[i-1][1] for i in range(1, len(bucket)))
   