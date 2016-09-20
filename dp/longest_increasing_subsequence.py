from bisect import bisect_left
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis1(self, A):
        piles = []
        for i in range(len(A)):
            k = bisect_left(piles, A[i])
            if k >= len(piles):
                piles.append(A[i])
            else:
                piles[k] = A[i]
        return len(piles)

    def lis(self, A):
        opt = [1] * len(A)
        for i in range(len(A)):
            for j in range(i):
                if A[j] < A[i]:
                    opt[i] = max(opt[i], opt[j] + 1)
        return max(opt)