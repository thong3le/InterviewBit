from bisect import bisect_left, bisect_right
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def findCount(self, A, B):
        lo = 0
        hi = len(A) - 1
        while lo < hi:
            mid = (lo + hi)//2
            if A[mid] < B:
                lo = mid + 1
            else: 
                hi = mid
        if A[lo] != B:
            return 0
        left = lo
        hi = 
            
    def findCount1(self, A, B):
        left = bisect_left(A, B)
        if left == len(A) or A[left] != B:
            return 0
        right = bisect_right(A, B)
        return right - left
