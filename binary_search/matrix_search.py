class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        m = len(A)
        n = len(A[0])
        lo = 0
        hi = m * n - 1
        while lo <= hi:
            mid = lo + (hi-lo)//2
            i, j = divmod(mid, n)
            if A[i][j] == B:  return 1
            elif A[i][j] < B:  lo = mid + 1
            else:   hi = mid - 1
        return 0