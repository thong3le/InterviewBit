from bisect import bisect_left
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        lo = 0
        hi = len(A) - 1
        while lo <= hi:
            mid = (lo + hi)//2
            if A[mid] == B:
                return mid
            elif A[mid] < B:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo